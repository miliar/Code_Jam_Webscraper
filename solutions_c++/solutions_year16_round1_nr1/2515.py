#include<iostream>
#include<string>
using namespace std;
int main()
{
string s1;
char s2[4100];
int t,f,l,len,i,j,k;
cin>>t;
for(i=0;i<t;i++){
    cin>>s1;
    len=s1.size();
    l=f=2000+len/2+1;
    s2[l]=s1[0];
for(j=1;j<len;j++){
    if(s1[j]>=s2[f]){s2[--f]=s1[j];}
    else{ s2[++l]=s1[j];}
    }
cout<<"Case #"<<i+1<<": ";
for(k=f;k<=l;k++){cout<<s2[k];}
cout<<endl;
s1.clear();
}
return 0;
}
