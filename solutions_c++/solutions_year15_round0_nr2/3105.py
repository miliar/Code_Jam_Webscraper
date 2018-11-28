//In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <map>
#include <cstdlib>
using namespace std;
ifstream fin("1.txt");
ofstream fout("A.txt");
#define cin fin
#define cout fout
#define mp make_pair
const int MAXN=1e3+10;
int a[MAXN];

int main()
{
  int t;
  cin>>t;
  for(int i=1;i<=t;i++)
    {
      int ans=1e9+10,Max=0;
      int n;
      cin>>n;
      for(int j=1;j<=n;j++)
	{
	  cin>>a[j];
	  Max=max(Max,a[j]);
	}
      for(int j=1;j<=MAXN;j++)
	{
	  int tmp=0;
	  for(int k=1;k<=n;k++)
	    if(a[k]%j)
	      tmp+=a[k]/j;
	    else
	      tmp+=a[k]/j-1;
	  //cerr<<tmp<<endl;
	  tmp+=j;
	  ans=min(ans,tmp);
	}
      cout<<"Case #"<<i<<": "<<ans<<endl;
    }
  return 0;
}
