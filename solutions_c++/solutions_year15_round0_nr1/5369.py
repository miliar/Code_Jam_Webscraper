#include<iostream>
using namespace std;

int main()
{
  int t;
  cin>>t;
  int sm, res,count;
  char s[1010];
  for(int cases=1;cases<=t;cases++)
  {
  cin>>sm>>s;
  count = s[0]-'0';
  res=0;
  for(int i=1;i<=sm;i++)
    {
      if(s[i] > '0' && count < i )
	{
	  res += i - count;
	  count = i;
	}
      count += s[i] - '0';
    }
  cout<<"Case #"<<cases<<": "<<res<<endl;
  }
}
