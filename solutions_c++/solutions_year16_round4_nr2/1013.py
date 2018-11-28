//
//  main.cpp
//  FHC_Pattern
//
//  Created by Andriy Medvid on 11.01.15.
//  Copyright (c) 2015 Andriy Medvid. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

#define MAX_NUM 1000000000

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ/Round_2/B.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ/Round_2/B.out")

//#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ/Round_2/B-large.in")
//#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ/Round_2/B-large.out")

#define IN_NAME ("/Users/andriymedvid/Desktop/GCJ/Round_2/B-small-attempt0.in")
#define OUT_NAME ("/Users/andriymedvid/Desktop/GCJ/Round_2/B-small-attemp0.out")


// [person][selected number][yes number] = probability

#define MAX_NUM 18

int N, K;

double probabiities[MAX_NUM];

void OutCase(int caseNum) {
    cout << "Case #" << (caseNum+1) << ": ";
}

//   4 3 2
//

double p[MAX_NUM];

vector<double> getProbabilities(int a) {
    vector<double> probs;
    
    int i = 0;
    while (a > 0) {
        
        if(a&1)
            probs.push_back(probabiities[i]);
        
        a /= 2;
        i++;
    }
    
    return probs;
}



double getProbability(int a) {
    double result[MAX_NUM][MAX_NUM];
    
    for(int i = 0; i <= K; i++)
        for(int j = 0; j <= K/2; j++)
            result[i][j] = 0;
    
    result[0][0] = 1;
    
    vector<double> probs = getProbabilities(a);
    
    for(int i = 1; i <= probs.size(); i++)
        for(int j = 0; j <= i && j <= K/2; j++) {
            result[i][j] = result[i-1][j] * (1- probs[i-1]);
            if(j > 0)
                result[i][j] += result[i-1][j-1] * probs[i-1];
        }
    
    return result[K][K/2];
}

int getOnes(int a) {
    int res = 0;
    while (a > 0) {
        if(a&1)
            res++;
        a /= 2;
    }
    return res;
}

void iteration() {
    
    cin >> N >> K;
    
    for(int i = 0; i < N; i++)
        cin >> probabiities[i];
    
    double maxx = 0;
    
    for(int i = 0; i < (1 << N); i++)
        if(getOnes(i) == K) {
            double res = getProbability(i);
            if(res > maxx)
                maxx = res;
        }
    
    cout << maxx;
    
}

int main(int argc, const char * argv[]) {
    
    freopen(IN_NAME, "r", stdin);
    freopen(OUT_NAME, "w", stdout);
    
    int T;
    
    cin >> T;
    
    for(int tIter = 0; tIter < T; tIter++) {
        
        
        OutCase(tIter);
        
        iteration();
        
        cout << endl;
    }
    
    return 0;
}


