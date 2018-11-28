#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;
#define ll long long int

int main() {

    ifstream cin("inp.in");
    ofstream cout("out.txt");
    int t;
    cin>>t;
    int c = 1;
    while(t--){
        string S;
        cin>>S;
        string Z;
        Z = S[0];
        string temp ;
        for(int i=1;i<S.size();i++){
            if(S[i]>=Z[0]){
                temp.clear();
                temp = S[i];
                temp += Z;
                Z = temp;
            }
            else{
                Z += S[i];
            }
        }
        cout<<"Case #"<<c++<<": ";
        cout<<Z<<endl;
    }

    return 0;
}
