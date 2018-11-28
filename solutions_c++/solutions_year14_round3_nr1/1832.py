#include<iostream>
#include<vector>
#include<set>
#include<cstdio>
#include<string>
using namespace std;

bool isPowerOfTwo(int n)
{
  if (n == 0)
    return 0;
  while (n != 1)
  {
    if (n%2 != 0)
      return 0;
    n = n/2;
  }
  return 1;
}

int main()
{
	int t;
	cin>>t;
	string frac="";
	for(int cs = 1; cs <=t ;cs++)
	{
		cin>>frac;
		int a,b;
		sscanf_s(frac.c_str(), "%d/%d", &a, &b);
		if(b%2 == 1 || !isPowerOfTwo(b))
		{
			printf("Case #%d: impossible",cs);
			cout<<endl;
			continue;
		}
		int i;
		for (i = 1; i <= 40; i++)
		{
			double tmp = ((double)a*pow(2,i))/(double)b;
			if(tmp >= 1.0)
			{
				printf("Case #%d: %d",cs,i);
				cout<<endl;
				break;
			}

		}
		if(i>40)
		{
			printf("Case #%d: impossible",cs);
			cout<<endl;
		}
	}
	return 0;
}