#include <bits/stdc++.h>
#include <stdio.h>
using namespace std;

int main()
{
	int test,smax,a[1005],j=1;
	string str;
	cin>>test;

	while(test--)
	{
		int sum=0,frnd=0,powc;
		cin>>smax;
		cin>>str;
		// str= '1'+str;
		// cout<< str;
		
		// int value = atoi(str.c_str());
		int i=0;
		// int rem = value;
		// rem = remainder (rem, pow(10,powc+1));
		powc=smax;
		
		while(powc+1)
		{
			// a[i]= rem / pow(10,powc);
			// rem = rem % (int)pow(10,powc);
			a[i]=str[i]-'0';

			i++;
			powc--;
		}

		for (int i = 0; i <= smax; ++i)
		{
			if(a[i]!=0)
			{
				if (sum < i)
				{
					frnd += i-sum;
					sum += i-sum + a[i];
				}
				else
					sum += a[i];
			}
		}


		cout<<"Case #"<<j<<": "<<frnd<<endl;
		j++;

		

	}

}