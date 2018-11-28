#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>
#include <cmath>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int main()
{
	long long T,N,P;
	cin>>T;
	for (long long cs=1;cs<=T;cs++)
	{
		cin>>N>>P;
		long long tmp =1;
		tmp<<=N;
		tmp = tmp-P;
		cout<<"Case #"<<cs<<": ";
		if (tmp==0)
		{
			long long temp = 1;
			temp <<= N;
			cout<<temp-1<<' '<<temp-1<<endl;
			continue;
		}
		long long cnt = 0;
		long long ans = 0;
		for (long long i=N-1;i>=0;i--)
		{
			long long temp = 1;
			temp<<=i;
			if (temp & tmp)
			{
				break;
			}
			else 
			{
				cnt++;
			}
		}
		cnt++;
		long long i = 0;
		for (long long j=cnt;j>0;j--)
		{
			long long temp = 1;
			temp<<=i;
			ans |= temp;
			i++;
		}
		cout<<ans-1<<' ';

		tmp = P;
		cnt=0;
		for (long long i=N-1;i>=0;i--)
		{
			long long temp = 1;
			temp <<=i;
			if (temp & tmp)
			{
				break;
			}
			else 
			{
				cnt++;
			}
		}
		cnt++;
		//cout<<cnt<<endl;
		long long temp = 1;
		temp <<=N;
		long long temp2 = 1;
		temp2 <<=cnt;
		//cout<<temp<<endl;

		ans = temp - temp2;

		cout<<ans<<endl;

	}

	return 0;
}