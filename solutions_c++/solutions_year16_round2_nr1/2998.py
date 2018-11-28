//
//  main.cpp
//  jam2
//
//  Created by KimTaeheon on 4/30/16.
//  Copyright © 2016 t1. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    for (int t=0; t<T; t++) {
        string S, Z;
        int a[200], n[10];
        for (int i=0; i<10; i++) n[i]=0;
        for (int i=0; i<100; i++) a[i]=0;
        cin >> S;
        
        for (int i=0; i<S.length(); i++) {
            a[S[i]]++;
        }
        
        n[0] = a['Z'];
        n[2] = a['W'];
        n[4] = a['U'];
        n[6] = a['X'];
        n[8] = a['G'];
        
        //erase;
        a['Z'] -= n[0];
        a['E'] -= n[0];
        a['R'] -= n[0];
        a['O'] -= n[0];
        
        a['T'] -= n[2];
        a['W'] -= n[2];
        a['O'] -= n[2];
        
        a['F'] -= n[4];
        a['O'] -= n[4];
        a['U'] -= n[4];
        a['R'] -= n[4];
        
        a['S'] -= n[6];
        a['I'] -= n[6];
        a['X'] -= n[6];
        
        a['E'] -= n[8];
        a['I'] -= n[8];
        a['G'] -= n[8];
        a['H'] -= n[8];
        a['T'] -= n[8];
        
        n[1] = a['O'];
        n[3] = a['H'];
        n[5] = a['F'];
        
        a['O'] -= n[1];
        a['N'] -= n[1];
        a['E'] -= n[1];
        
        a['T'] -= n[3];
        a['H'] -= n[3];
        a['R'] -= n[3];
        a['E'] -= n[3];
        a['E'] -= n[3];
        
        a['F'] -= n[5];
        a['I'] -= n[5];
        a['V'] -= n[5];
        a['E'] -= n[5];
        
        n[7] = a['V'];
        
        n[9] = a['I'];
        
        cout << "Case #" << t+1 << ": ";
        for (int i=0; i<10; i++) {
            for (int j=0; j<n[i]; j++)
                cout << i;
        }
        cout << endl;
    }
    return 0;
}
