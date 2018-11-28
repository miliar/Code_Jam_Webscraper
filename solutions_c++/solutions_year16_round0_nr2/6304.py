#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cassert>

using namespace std;

class pancake{
public:
string S;

pancake(string s)
{
S=s;
}
int eff(int start)
{
if(S[start]=='-')
{
int i;
for(i=start;S[i]=='-';i++)
{}
return 1+eff(i);
}
else if(S[start]=='+')
{
int j;
for(j=start;S[j]=='+';j++)
{}
if(j==S.length())
return 0;
else
return 1+eff(j);
}
}
};

int main()
{
FILE *fin=freopen("B-large.in","r",stdin);
assert(fin!=NULL);
FILE *fout=freopen("B-large.out","w",stdout);
int T;
cin>>T;
for(int t=1;t<=T;t++)
{
string s;
cin>>s;
pancake p(s);
int sol=p.eff(0);
cout<<"Case #"<<t<<": "<<sol<<endl;


} 
return 0;
}
