//In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
ifstream fin("1.txt");
ofstream fout("A.txt");
#define cin fin
#define cout fout

int main()
{
  int t;
  cin>>t;
  for(int i=1;i<=t;i++)
    {
      int n;
      cin>>n;
      char s[1100];
      for(int j=0;j<=n;j++)
	cin>>s[j];
      int sum=0,ans=0;
      for(int j=0;j<=n;j++)
	if(s[j]!='0')
	  {
	    if(j<=sum)
		sum+=s[j]-'0';
	    else
	      {
		ans+=j-sum;
		sum+=j-sum+s[j]-'0';
	      }
	  }
      cout<<"Case #"<<i<<": "<<ans<<endl;
    }
  return 0;
}
