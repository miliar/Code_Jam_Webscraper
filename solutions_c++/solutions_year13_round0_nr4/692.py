//
//  main.cpp
//  treasure
//
//  Created by John Scholes on 13/04/2013.
//  Copyright (c) 2013 John Scholes. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    int N; cin >> N;
    for(int N1=1; N1<=N; N1++) {
        int K, C, num, keys[401]={}, needs[401], keysin[401][401]={}, nkeysin[401]={};
        int chest[400],i,j,back,opened[401]={},keyshortage;
        cin >> K >> C; // get number of starter keys and number of chests
        for(i=0; i<K; i++) {
            cin >> j;
            keys[j]+=1; // keys[j] gives no. of keys of type j
        }
        for(i=1; i<=C; i++) {
            cin >> needs[i] >> nkeysin[i]; // chest i needs key needs[i] and contains nkeysin[i] keys
            for(j=0; j<nkeysin[i]; j++)
                cin >> keysin[i][j]; // keysin[i][0],...,keysin[i][] is list of keys in chest i
        }
        keyshortage=0;
        for(i=1; i<401; i++) {
            j=keys[i];
            for(int i1=1; i1<=C; i1++) {
                if(needs[i1]==i) j--;
                for(int j1=0; j1<nkeysin[i1]; j1++) if(keysin[i1][j1]==i) j++;
            }
            if(j<0) {keyshortage=1; break;}
        }
        if(keyshortage) {
            cout << "Case #" << N1 << ": IMPOSSIBLE\n";
            continue;
        }
        num=1; i=1; back=0;
        while(1) {
            if(num>C) {
                cout << "Case #" << N1 << ":";
                for(j=1; j<=C; j++) cout << " " << chest[j];
                cout << "\n";
                break;
            }
            if(back) {
                if(num==0) {
                    cout << "Case #" << N1 << ": IMPOSSIBLE\n";
                    break;
                }
                back=0;
                i=chest[num];
                for(j=0; j<nkeysin[i]; j++) keys[keysin[i][j]]-=1;
                keys[needs[i]]+=1;
                opened[i]=0;
                i++;
            }
            if(i>C) {
                back=1;
                num--;
                continue;
            }
            if(opened[i]) {
                i++;
                continue;
            }
            if(keys[needs[i]]) {
                if(keys[needs[i]]==1) {
                    int sum=0;
                    for(j=0; j<nkeysin[i]; j++) if(keysin[i][j]==needs[i]) sum++;
                    if(sum==0) {
                        int moreNeeded=0, moreAvail=0;
                        for(j=1; j<=C; j++) {
                            if(j==i || opened[j]) continue;
                            if(needs[j]==needs[i]) moreNeeded++;
                            else {
                                for(int j1=0; j1<nkeysin[j]; j1++) if(keysin[j][j1]==needs[i]) moreAvail++;
                            }
                        }
                        if(moreNeeded && !moreAvail) {i++; continue; }
                    }
                }
                chest[num]=i;
                keys[needs[i]]-=1;
                opened[i]=1;
                for(j=0; j<nkeysin[i]; j++) keys[keysin[i][j]]+=1;
                num++;
                i=1;
            }
            else i++;
        }
    }
    return 0;
}

