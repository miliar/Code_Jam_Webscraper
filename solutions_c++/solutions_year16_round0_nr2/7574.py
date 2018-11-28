#include <iostream>
#include <cstring>
using namespace std;
int main() {
    int i,j,n,ct;
    string a;
    char flag;
    cin>>n;
    for(i=0 ; i<n ; i++){
        cin>>a;
        flag = a[0];
        ct=0;
        for(j=1 ; j<a.length() ; j++){
            if(a[j]!= flag){
                ct++;
                flag=a[j];
            }
        }
        if(a[a.length()-1]=='-') ct++;
        cout<<"Case #"<<i+1<<":"<<ct<<endl;
    }
    return 0;
}
