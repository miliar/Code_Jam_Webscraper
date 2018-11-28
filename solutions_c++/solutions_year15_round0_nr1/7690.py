#include <iostream>
#include <cstdio>

using namespace std;

int t,maxi,ans=0;

int main()
{
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
  cin >> t;
  for(int T=1;T<=t;T++)
    {
      cin >> maxi;
      char S[maxi+1];
      cin >> S;
      long A[maxi+1];
      ans=0;
      for(int i=0;i<maxi+1;i++)
	{
	  A[i]=0;
	  i==0 ? A[i]=(int)(S[i]-'0') : A[i]=A[i-1]+(int)(S[i]-'0');
	}
      for(int i=0;i<maxi;i++)
	{
	  if(S[i+1]!='0' && A[i]+ans<i+1)ans+=i+1-A[i]-ans;
	}
      cout << "Case #" << T << ": "  << ans << '\n';
    }
  return 0;
}
