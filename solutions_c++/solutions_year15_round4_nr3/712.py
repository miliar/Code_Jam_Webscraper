/* -*- Mode: C; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- */

/*  Mafijski praktikum naloga
 *  =========================
 *  Copyright 2015 Domen Ipavec <domen.ipavec@z-v.si>
 *
 *  Licensed under the MIT License (the "License");
 */


#include <iostream>
#include <cmath>
#include <fstream>
#include <random>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <string>
#include <sstream>
#include <stdint.h>
using namespace std;

double epsilon = 0.00001;

int count(unordered_set<string> &english, unordered_set<string> &french) {
    int same_words = 0;
    for (auto it = english.begin(); it != english.end(); ++it) {
        if (french.count(*it) > 0) {
            same_words++;
        }
    }
    return same_words;
}

int branch(vector<vector<string> > &sentences, unordered_set<string> &english, unordered_set<string> &french, int i, int best) {
    if (i == sentences.size()) {
        return count(english, french);
    }
    
    unordered_set<string> english1(english);
    unordered_set<string> french1(french);
    
    for (auto it = sentences[i].begin(); it != sentences[i].end(); ++it) {
        if (english.count(*it) == 0) {
            english.insert(*it);
        }
        if (french1.count(*it) == 0) {
            french1.insert(*it);
        }
    }
    
    if (count(english, french) < best) {
        best = min(branch(sentences, english, french, i+1, best), best);
    }
    
    if (count(english1, french1) < best) {
        best = min(branch(sentences, english1, french1, i+1, best), best);
    }
    
    return best;
}

int main(int argc, char *argv[]) {
    cout.precision(10);
    ifstream input;
   
    if (argc < 2) {
        input.open("data.dat");
    } else {
        input.open(argv[1]);
    }
    
    
    uint64_t n;
    
    string line;
    getline(input, line);
    stringstream linestream_n(line);
    linestream_n >> n;
    
    for (uint64_t u = 0; u < n; u++) {
        cerr << "Start " << u << endl;
        
        int N;
        getline(input, line);
        stringstream linestream_N(line);
        linestream_N >> N;
        
        vector<vector<string> > sentences;
        for (int i = 0; i < N; i++) {
            getline(input, line);
            
            stringstream linestream(line);

            vector<string> words;
            while (!linestream.eof()) {
                string word;
                linestream >> word;
                words.push_back(word);
            }
            
            sentences.push_back(words);
        }
        
        unordered_set<string> english;
        unordered_set<string> french;
        
        for (auto it = sentences[0].begin(); it != sentences[0].end(); ++it) {
            if (english.count(*it) == 0) {
                english.insert(*it);
            }
        }
        for (auto it = sentences[1].begin(); it != sentences[1].end(); ++it) {
            if (french.count(*it) == 0) {
                french.insert(*it);
            }
        }
        
        int i = branch(sentences, english, french, 2, 10000000);
        
        cout << "Case #" << u+1 << ": ";
        cout << i;
        cout << endl;
        cerr << "done" << endl;
    }

    return 0;
}
