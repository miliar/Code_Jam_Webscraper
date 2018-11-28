#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<cmath>
#include<cstring>
#include<climits>

using namespace std;

bool is_sq(int x)
{
  int cool=(int)sqrt((double)x);
  if(cool*cool==x)
    return true;
  else
    return false;
}

bool  is_palin(int x)
{
  if(x%10==x)
    return true;

  vector<int> ck;
  while(x)
    {
      ck.push_back(x%10);
      x/=10;
    }
  bool flag=true;
  for(int i=0;i<ck.size()/2;i++)
    {
      if(ck[i]!=ck[ck.size()-i-1])
	{flag=false;break;}
    }
  return flag;
}

int main()
{
  vector<int> ip;
  vector<int> cm;

  //prec
  ip.push_back(0);
  cm.push_back(0);

  
  for(int i=1;i<=1010;i++)
    {
      bool fst=is_sq(i);
      int cool=(int)sqrt(i);
      if(fst&&is_palin(i)&&is_palin(cool))
	ip.push_back(1);
      else
	ip.push_back(0);
      /*
      if(i<=10)
	{
	  cout<<i<<": "<<fst<<" "<<is_palin(cool)<<" "<<is_palin(i)<<" ";
	  cout<<ip[ip.size()-1]<<"\n";
	  
	}
      */
	  
    }
  
  for(int i=1;i<ip.size();i++)
    cm.push_back(cm[i-1]+ip[i]);
  //..prec done  

  int t;
  cin>>t;
  for(int tt=0;tt<t;tt++)
    {
      int lo,hi;
      cin>>lo>>hi;
      //     
      cout<<"Case #"<<tt+1<<": "<<cm[hi]-cm[lo-1]<<"\n";
    }


  return 0;
}
