//
//  main.cpp
//  Deceitful War
//
//  Created by Kotsur on 13.04.14.
//  Copyright (c) 2014 Dmytro Kotsur. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <fstream>
#include <limits>

#define MAX_N 1001

using namespace std;

int T, N;
double Naomi[MAX_N], Ken[MAX_N];
bool used[MAX_N];

ifstream in("/Users/userMac/Projects/Contests/Google Code Jam 2014/Qualification_Round/Deceitful War/google_test.txt");
ofstream out("/Users/userMac/Projects/Contests/Google Code Jam 2014/Qualification_Round/Deceitful War/out.txt");


int play_war();
int play_deceitful_war();


int main(int argc, const char * argv[])
{
    in >> T;
    for (int t = 1; t <= T; ++t) {
        in >> N;
        for (int i = 0; i < N; ++i) {
            in >> Naomi[i];
        }
        for (int i = 0; i < N; ++i) {
            in >> Ken[i];
        }
        for (int i = 0; i < N; ++i) {
            used[i] = false;
        }
        
        sort(Naomi, Naomi + N);
        sort(Ken, Ken + N);
        
        out << "Case #" << t << ": ";
        out << play_deceitful_war() << " ";
        for (int i = 0; i < N; ++i) {
            used[i] = false;
        }
        
        out << play_war() << endl;
    }

    
    return 0;
}

int play_deceitful_war() {
    
    int NaomiScores = 0, KenScores = 0;
    for (int i = 0; i < N; ++i) {
        
        int max_i = -1;
        double max_v = numeric_limits<double>::infinity();
        for (int j = 0; j < N; ++j) {
            if (!used[j] && Naomi[j] > Ken[i] && max_v > Naomi[j]) {
                max_v = Naomi[j];
                max_i = j;
            }
        }
        
        if (max_i != -1) {
            used[max_i] = true;
            NaomiScores++;
        }
        
    }
    return NaomiScores;
}

int play_war() {
    
    int NaomiScores = 0, KenScores = 0;
    for (int i = 0; i < N; ++i) {
        
        int min_i = -1;
        double min_v = numeric_limits<double>::infinity();
        for (int j = 0; j < N; ++j) {
            if (!used[j] && Ken[j] > Naomi[i] && Ken[j] < min_v) {
                min_v = Ken[j];
                min_i = j;
            }
        }
        
        if (min_i == -1) {
            min_i = 0;
            while (used[min_i]) min_i++;
        }
        
        used[min_i] = true;
        //cout << "Naomi: " << Naomi[i] << ", Ken: " << Ken[min_i];
        if (Naomi[i] > Ken[min_i]) {
          //  cout << "; Naomi wins! ";
            NaomiScores++;
        } else {
           // cout << "; Ken wins! ";
            KenScores++;
        }
        //cout << endl;
        
    }
    
    
    return NaomiScores;
    
}
