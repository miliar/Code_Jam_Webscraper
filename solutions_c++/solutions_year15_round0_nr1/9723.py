#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("standings.in","r",stdin);
	freopen("standings.out","w",stdout);
    int t,s,i,z,len,au[10000],tambah;
    string si;
    cin>>t;
    for (z=1; z<=t; z++){
        tambah=0;
        memset(au,0,sizeof(au));
        cin>>s;
        cin>>si;
        for (i=0; i<=s; i++){
            if (si[i]=='0'){
                tambah++;
            }
            else{
                si[i+1]=si[i+1]+si[i]-'1';
            }
        }
        cout<<"CASE #"<<z<<": ";
        cout<<tambah<<endl;
    }
}
