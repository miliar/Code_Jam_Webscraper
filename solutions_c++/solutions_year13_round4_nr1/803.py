/* 
 * File:   main.cpp
 * Author: tyg3r
 *
 * Created on 1. červen 2013, 15:54
 */

#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <stack>

using namespace std;

struct station {
    long st;
    long o;
    long e;
};

struct stackS {
    long st;
    long p;
};

bool cmpFunc (struct station s1 , struct station s2) { return (s1.st<s2.st); }

int main(int argc, char** argv) {
    
    long T, caseN = 0, N, M, O[107], E[107];
    long real;
    long o, e, p;
    vector<station> sta1, sta2;
    station tmpSta;
    cin >> T;
    while(caseN < T) {
        real = 0;
        cin >> N >> M;
        
        sta1.clear();
        sta2.clear();
        //for(int i = 0; i <= N; i++) {
        //    O[i] = E[i] = 0;
        //}
        for(int m = 0; m < M; m++) {
            cin >> o >> e >> p;
            tmpSta.st = o;
            tmpSta.e = 0;
            tmpSta.o = p;
            sta1.push_back(tmpSta);
            tmpSta.o = 0;
            tmpSta.st = e;
            tmpSta.e = p;
            sta1.push_back(tmpSta);
            //O[o] += p;
            //E[e] += p;
            long tmpSum = ((((e - o) * N - (e - o) * (e - o - 1) / 2) % 1000002013) * p) % 1000002013;
            real += tmpSum;
            real %= 1000002013;
        }
        sort(sta1.begin(), sta1.end(), cmpFunc);
        long lastStation = -1;
        for(long i = 0; i < sta1.size(); i++) {
            if(sta1[i].st != lastStation) {
                sta2.push_back(sta1[i]);
                lastStation = sta1[i].st;
            } else {
                long last = sta2.size()-1;
                sta2[last].e += sta1[i].e;
                sta2[last].o += sta1[i].o;
            }
        }
        
        //for(long sta2I = 0; sta2I < sta2.size(); sta2I++) {
        //    printf("station: %ld o: %ld e: %ld\n", sta2[sta2I].st, sta2[sta2I].o, sta2[sta2I].e);
        //}
        
        long fake = 0;
        stackS tmpStackS;
        stack<stackS> tickets;
        while(!tickets.empty()) tickets.pop();
        for(long sta2I = 0; sta2I < sta2.size(); sta2I++) {
            if(sta2[sta2I].o >= sta2[sta2I].e) {
                tmpStackS.st = sta2[sta2I].st;
                tmpStackS.p = sta2[sta2I].o - sta2[sta2I].e;
                tickets.push(tmpStackS);
                continue;
            }
            long out = sta2[sta2I].e - sta2[sta2I].o;
            
            while(out > 0) {
                tmpStackS = tickets.top();
                tickets.pop();
                long selling;
                if(out >= tmpStackS.p) selling = tmpStackS.p;
                else selling = out;
                e = sta2[sta2I].st;
                o = tmpStackS.st;
                p = selling;
                long tmpSum = ((((e - o) * N - (e - o) * (e - o - 1) / 2) % 1000002013) * p) % 1000002013;
                out -= selling;
                tmpStackS.p -= selling;
                if(tmpStackS.p > 0) tickets.push(tmpStackS);
                fake += tmpSum;
                fake %= 1000002013;
            }
            
        }
        
        //printf("real: %d fake: %d\n", real, fake);
        printf("Case #%ld: %ld\n", ++caseN, (real + 1000002013 - fake) % 1000002013);
        
    }
    
    return 0;
}

