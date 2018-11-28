#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<=b;i++)
map<char,int> m;
char s[2009];
int A[20];
int main()
{
freopen("input.in","r",stdin);
freopen("output.txt","w",stdout);
int TT=0,l,T;
cin>>T;
while(T--)
{TT++;m.clear();
cin>>s;
l=strlen(s);
FOR(i,0,l-1)
m[s[i]]++;
A[0]=m['Z'];
A[8]=m['G'];
A[6]=m['X'];
A[2]=m['W'];
A[4]=m['U'];
A[5]=m['F']-A[4];
A[7]=m['V']-A[5];
A[3]=m['R']-A[0]-A[4];
A[1]=m['O']-A[0]-A[2]-A[4];
A[9]=(m['N']-A[1]-A[7])/2;
printf("Case #%d: ",TT);
FOR(i,0,9)
{
if(A[i]!=0)
FOR(j,1,A[i])
cout<<i;

}
cout<<endl;
}
return 0;
}
