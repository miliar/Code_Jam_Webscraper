#include<iostream>
#include<string>
#include<vector>
#define mod(n) ( (n) < (0) ? (-1*n) : (n) )
using namespace std;
string removeDuplicates(string S,vector <int> * t)
{
string O;
int i,j=0;
for(i=0;i<S.length();i++)
{
if(i==0)
{O=O+S[i]; }
else if(S[i]!=S[i-1])
{O=O+S[i]; (*t).push_back(j); j=0;}
j++;
}
(*t).push_back(j);
return O;
}
int main()
{
int t,l;
cin>>t;
l=t;
while(t--)
{
int n;
cin>>n;
vector <vector<int> > s;
vector <string> S,R;
int ans=0,count=0;
for(int i=0;i<n;i++)
{
string p;
cin>>p;
S.push_back(p);
vector<int> o;
p=removeDuplicates(S[i],&o);
R.push_back(p);
s.push_back(o);
}
int f=1;
for(int i=0;i<n-1;i++)
{
if(R[i]!=R[i+1])
{
f=0;
break;
}
}
cout<<"Case #"<<l-t<<": ";
if(f!=0)
{
for(int i=0;i<R[0].size();i++)
{
ans+=mod((s[1][i]-s[0][i]));
}
cout<<ans<<endl;
}
else
cout<<"Fegla Won\n";
}
return 0;
}