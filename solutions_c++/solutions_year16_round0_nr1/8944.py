#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    ifstream fin("A-large.in");
    ofstream fout("output.txt");
int t;
fin>>t;
int j=1;
while(t--){
    long long n;
    fin>>n;
    if(n==0){
      fout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
    j++;
    continue;
    }
    long long m=n;
    bool arr[10]={0};
    int count=0;
    int i=2;
    long long save;
    while(count!=10){
            save=m;
        while(m!=0){
            int a=m%10;
            if(arr[a]==0){
            arr[a]=1;
            count++;
            }
            m/=10;
        }
        m=i*n;
        i++;
    }
    fout<<"Case #"<<j<<": "<<save<<endl;
    j++;
}
}
