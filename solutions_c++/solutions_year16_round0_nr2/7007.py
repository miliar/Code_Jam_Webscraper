#include<iostream>
using namespace std;
#include<cstring>

bool allnotup(string s, int n){
int k=1;
for(int i=0; i<n; i++){
if(s[i]=='-'){
    k=0;
    break;
}
}
if(k==0) return true;
else return false;
}

int main(){
int t;
cin>>t;
for(int loop=1; loop<=t; loop++){
//Solution here:
string s;
cin>>s;
int n=0;
for(int l=0; s[l]!='\0'; l++){n++;}
int i,j,k;
for(i=0; allnotup(s,n); i++){
for(j=n-1; s[j]=='+'; j--){}
for(k=0; k<=j; k++){
if(s[k]=='+') s[k]='-';
else s[k]='+';
}
}
cout<<"Case #"<<loop<<": "<<i<<endl;
}
return 0;
}
