//
//  main.cpp
//  zad1
//
//  Created by Tomasz Krzyżek on 5/4/13.
//  Copyright (c) 2013 Tomasz Krzyżek. All rights reserved.
//

#include<iostream>
#include<algorithm>

using namespace std;

typedef unsigned long long int ulli;
#define REP(i, n) for(int i = 0; i < n; i++)


int ileRuchow(int iloscMotek, int t[], int amin);
int main(){
    ios_base::sync_with_stdio(0);
    int iloscZestawow;
    cin >> iloscZestawow;
    REP(x, iloscZestawow){
        ulli amin, iloscMotek;
        cin >> amin >> iloscMotek;
        int *t = new int[iloscMotek];
        REP(i, iloscMotek){
            int temp;
            cin >> temp;
            t[i] = temp;
        }
        if(amin != 1){
        sort(t, t+iloscMotek);
        int *wyniki = new int[iloscMotek+1];
        for(int i=0; i <= iloscMotek; i++){
            wyniki[i] = ileRuchow(i, t, amin) + iloscMotek-i;
            //cout << "wynik " << wyniki[i] << endl;
        }
        int count = *min_element(wyniki, wyniki+iloscMotek+1);
        delete[] t;
        cout << "Case #" << x+1 << ": " << count << endl;
        }
        else{
            cout << "Case #" << x+1 << ": " << iloscMotek << endl;
        }
    }
    return 0;
}

int ileRuchow(int iloscMotek, int t[], int amin){
    int counter = 0;
    REP(i, iloscMotek){
        if(amin > t[i]){
            amin = amin+t[i];
        }
        else{
            while(amin <= t[i]){
                amin = amin + amin - 1;
                //cout << amin << endl;
                counter++;
            }
            amin = amin+t[i];
        }
    }
    return counter;
}

