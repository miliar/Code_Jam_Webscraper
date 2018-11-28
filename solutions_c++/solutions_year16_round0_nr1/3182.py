//
//  main.cpp
//  CountingSheep
//
//  Created by MichelleShieh on 4/9/16.
//  Copyright (c) 2016 MichelleShieh. All rights reserved.
//

//#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>

using namespace std;

ifstream cin ("/Users/michelleshieh/Google Code Jam/CountingSheep/A-large.in.txt");
ofstream cout ("/Users/michelleshieh/Google Code Jam/CountingSheep/A-large.out.txt");

void divide(long long n, vector<int> &a) {
    a.clear();
    while (n!=0) {
        a.push_back(n%10);
        n/=10;
    }
}

bool check(unordered_map<int,bool> hash) {
    for (int i=0;i<10;i++) {
        if (hash[i]==false) {
            return false;
        }
    }
    return true;
}

int main() {
    unordered_map<int, bool> hash;
    int t;
    cin >> t;
    //fin >> t1>>t2;
    //fout<< t << t1 << t2 <<endl;
    long long n;
    vector <int> a;
    for (int i=1;i<=t;i++) {
        cin>>n;
        if (n == 0) {
            cout << "Case #"<<i<<": INSOMNIA"<<endl;

        }
        else {
            for (int i = 0; i < 10; i++) {
                hash[i]=false;
            }
            long long k;
            for (k = 1; check(hash)==false; k++) {

                divide(k*n,a);
                for (int j=0;j<a.size();j++) {
                    hash[a[j]]=true;
                    if (check(hash)==true) {
                        break;
                    }
                }
                //cout<<(k-1)*n<<endl;
            }
            cout << "Case #"<<i<<": "<<(k-1)*n<<endl;

        }
        
    }
    cin.close();
    cout.close();
    return 0;
}
