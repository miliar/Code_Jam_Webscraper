#include<bits/stdc++.h>

using namespace std;

string s[3],s1,s2,s3;
int n,R,P,S,t[3];

int solve()
{
  for(int i=n-1;i>-1;i--)
    {
      if(max(max(t[0],t[1]),t[2])*2>t[0]+t[1]+t[2])
	return -1;
      int k=(1<<i);
      int a=t[0]+t[1]-k,b=t[1]+t[2]-k,c=t[0]+t[2]-k;
      t[0]=a,t[1]=b,t[2]=c;
      s1=min(s[0]+s[1],s[1]+s[0]),s2=min(s[1]+s[2],s[2]+s[1]),s3=min(s[0]+s[2],s[2]+s[0]);
      s[0]=s1,s[1]=s2,s[2]=s3;
    }
  for(int i=0;i<3;i++)
    if(t[i]==1)
      return i;
}


int main()
{
  int qw;
  cin>>qw;
  for(int q=1;q<=qw;q++)
    {
      cin>>n>>R>>P>>S;
      t[0]=P,t[1]=R,t[2]=S;
      s[0]='P',s[1]='R',s[2]='S';
      int tmp=solve();
      cout<<"Case #"<<q<<": ";
      if(tmp==-1) cout<<"IMPOSSIBLE\n";
      else
	cout<<s[tmp]<<endl;
    }
}
