#include<iostream>
#include<set>
using namespace std;

int main()
{
  int t;
  long long n,temp;
  cin>>t;
  for(int i = 1; i <=t; i++)
  {
     cin>>n;
     if(n == 0)
     {
       cout<<"Case #"<<i<<": INSOMNIA"<<endl;
       continue;
     }
     int j = 1;
     set<int> digits;
     while(true)
     {
	temp = n * j;
	while(temp > 0)
	{
	  digits.insert(temp%10);
	  temp /= 10;
	}
	if(digits.size() == 10)
	{
	  cout<<"Case #"<<i<<": "<<n*j<<endl;
          break;
	}
	j++;
     }
  }
}
