#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;

int flips(string s)
{
 int inv[100],invc=0;
 for(int i=0;i<s.size()-1;i++)
    {
     if(s[i]!=s[i+1]){inv[invc]=i+1; invc++;}
    }
if(s[s.size()-1]=='-')return invc+1;
return invc;
}

int main()
{
int t;
int res;
string s;
scanf("%d",&t);
for(int i=0;i<t;i++){
cin>>s;
res=flips(s);
cout<<"Case #"<<i+1<<": "<<res<<endl;
}

return 0;
}
