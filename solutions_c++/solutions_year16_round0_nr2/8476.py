#include <bits/stdc++.h>
using namespace std;

#define ll long long int

int main() {	freopen("input.txt","r",stdin);
	            freopen("output.txt","w",stdout);

	ll t,res,flag,coun,len,i,j,k=1;
	string input;

	scanf("%lld",&t);

	while(t--)
	{
		cin>>input;

		coun = 0;

		len = input.length();

		if(input[0] == '-')
			flag=1;
		else
			flag=0;

		for(i = 0; i< len; i++)
		{
			if(input[i] == '-')
			{
				while(input[i+1] == '-')
					i++;

				coun++;
			}
		}

		res = coun*2;

		if(flag == 1)
			res--;

		printf("Case #%lld: %lld\n",k++,res);

	}

	return 0;
}
