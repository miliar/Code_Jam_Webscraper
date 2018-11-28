#include <iostream>
#include <vector>
#include <string>
#include <algorithm>



using namespace std;


int main()
{
  ios::sync_with_stdio(false);
  int T;
  cin>>T;
  int I=1;
  while(I<=T)
    {
      int n,s;
      cin>>n>>s;
      vector <int> num;
      for(int i=0;i<n;i++)
	{
	  int tmp;
	  cin>>tmp;
	  num.push_back(tmp);
	}
      sort(num.begin(),num.end());
      int tedad =0;
      int flag1=0,flag2=n-1;
      while(flag1<=flag2)
	{
	  if(flag1==flag2)
	    {
	      tedad++;
	      flag1++;
	    }
	  else
	    {
	      if(num[flag1]+num[flag2]<=s)
		{
		  tedad++;
		  flag1++;
		  flag2--;
		}
	      else
		{
		  tedad++;
		  flag2--;
		}
	    }
	}
      cout<<"Case #"<<I<<": "<<tedad<<endl;
      I++;
    }
  return 0;
}
