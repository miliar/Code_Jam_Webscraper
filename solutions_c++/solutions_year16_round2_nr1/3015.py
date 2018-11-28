#include <bits/stdc++.h>
//#include<iostream>
using namespace std;
typedef long long int lli;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
#define read() freopen("A-large(1).in", "r", stdin)
#define write() freopen("output.txt", "w", stdout)
int main()
{
    read(); write();
    int t, x, n;
     cin>>t; x=t;
     while(t--){
        map<char, int> M;
        string a; cin>>a; n=a.length(); string b;
        for(int i =0; i<n; i++){
            M[a[i]]++;
        }
        if(M['Z']>0){
            for(int i=0; i<M['Z']; i++) b+='0';
            M['E']-=M['Z'];
            M['R']-=M['Z'];
            M['O']-=M['Z'];
            M['Z']-=M['Z'];
        }
        if(M['U']>0){
            for(int i=0; i<M['U']; i++) b+='4';
            M['F']-=M['U'];
            M['O']-=M['U'];
            M['R']-=M['U'];
            M['U']-=M['U'];
        }
        if(M['W']>0){
            for(int i=0; i<M['W']; i++) b+='2';
            M['T']-=M['W'];
            M['O']-=M['W'];
            M['W']-=M['W'];
        }
        if(M['X']>0){
            for(int i=0; i<M['X']; i++) b+='6';
            M['S']-=M['X'];
            M['I']-=M['X'];
            M['X']-=M['X'];
        }
        if(M['G']>0){
            for(int i=0; i<M['G']; i++) b+='8';
            M['E']-=M['G'];
            M['I']-=M['G'];
            M['H']-=M['G'];
            M['T']-=M['G'];
            M['G']-=M['G'];
        }
        if(M['O']>0){
            for(int i=0; i<M['O']; i++) b+='1';
            M['N']-=M['O'];
            M['E']-=M['O'];
            M['O']-=M['O'];
        }
        if(M['T']>0){
            for(int i=0; i<M['T']; i++) b+='3';
            M['H']-=M['T'];
            M['R']-=M['T'];
            M['E']-=(2*M['T']);
            M['T']-=M['T'];
        }
        if(M['F']>0){
            for(int i=0; i<M['F']; i++) b+='5';
            M['I']-=M['F'];
            M['V']-=M['F'];
            M['E']-=M['F'];
            M['F']-=M['F'];
        }
        if(M['S']>0){
            for(int i=0; i<M['S']; i++) b+='7';
            M['E']-=(2*M['S']);
            M['V']-=M['S'];
            M['N']-=M['S'];
            M['S']-=M['S'];
        }
        if(M['I']>0){
            for(int i=0; i<M['I']; i++) b+='9';
            M['N']-=(2*M['I']);
            M['E']-=M['I'];
            M['I']-=M['I'];
        }
        sort(b.begin(), b.end());
        cout<<"Case #"<<x-t<<": "<<b<<endl;
        M.clear();
     }
}
