//
//  main.cpp
//  CodeJam
//
//  Created by akhilesh chaudhary on 11/04/15.
//  Copyright (c) 2015 Codenation. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <set>
using namespace std;

int main(int argc, const char * argv[]) {
    ofstream cout;
    ifstream cin;
    cin.open("//Users//akhileshchaudhary//Desktop//in1.in",ios::in);
    cout.open("//Users//akhileshchaudhary//Desktop//out.txt",ios::out);
    int t,D;
    int a[1005];
    cin>>t ;
    int cnt=0 ;
    while (t--) {
        cnt++;
        cin>>D;
        int min =1000000;
        for (int i=0; i<D; i++) {
            cin>>a[i];
        }
        sort(a,a+D);
        for (int i=1; i<=a[D-1]; i++) {
            int total =0;
            for (int j=0; j<D; j++) {
                if(a[j]%i)
                total +=(a[j]/i);
                else
                total +=(a[j]/i-1);
            }
            if(total+i<min)
            min=total+i;
        }
        cout <<"Case #"<<cnt<<": " <<min<<endl;
    }
    return 0;
}
