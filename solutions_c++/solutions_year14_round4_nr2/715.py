#include <iostream>
#include <vector>
#include <string>
#include <algorithm>



using namespace std;

const int MAXn = 1000+17;




int tedad(vector<int>& num)
{
  int n = num.size();
  int s = 0;
  int flag1=0,flag2=n-1;
  for(int i=0;i<n-1;i++)
    {
      int ja = 0;
      int minimum = 1000*1000*1000+1;
      for(int j=flag1;j<=flag2;j++)
	{
	  if(num[j]<minimum)
	    {
	      minimum = num[j];
	      ja = j;
	    }
	}
      if(ja-flag1 <flag2-ja)
	{
	  while(ja!=flag1)
	    {
	      swap(num[ja] , num[ja-1]);
	      ja--;
	      s++;
	    }
	  flag1++;
	}
      else
	{
	  while(ja!=flag2)
	    {
	      swap(num[ja],num[ja+1]);
	      ja++;
	      s++;
	    }
	  flag2--;
	}
    }
  return s;
}
int main()
{
  ios::sync_with_stdio(false);
  int T;cin>>T;int I=1;
  while(I<=T)
    {
      int n;
      cin>>n;
      vector <int> num;
      for(int i=0;i<n;i++)
	{
	  int tmp;
	  cin>>tmp;
	  num.push_back(tmp);
	}
      int minimum = tedad(num);
      cout<<"Case #"<<I<<": "<<minimum<<endl;
      I++;
    }
  return 0;
}
