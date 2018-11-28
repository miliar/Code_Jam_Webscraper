#include<iostream>
using namespace std;
#include<cstring>
#include<stdio.h>
#include<string.h>
int main(){
int T;
cin>>T;
for(int l=1; l<=T; l++){
    string s;
    cin>>s;
int n=0;
for(int i=0; s[i]!='\0'; i++){
    n++;
}
char t[3000];
t[0]=s[0];
int m=1;
for(int i=1; i<n; i++){
    if((int)s[i]>=(int)t[0]){
        for(int j=m; j>0; j--){
            t[j]=t[j-1];
        }
        t[0]=s[i];
        m++;
    }
    else{
        t[m]=s[i];
        m++;
    }
}
t[m]='\0';
cout<<"Case #"<<l<<": "<<t<<endl;
}
return 0;
}
