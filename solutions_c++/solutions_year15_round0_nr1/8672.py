#include<iostream>
#include<string>
#include<algorithm>
#include<math.h>
#include<fstream>

using namespace std;


int t , m , sum , cnt;
string s;
int main()
{
	freopen("111.in", "r", stdin);
	freopen("222.out", "w", stdout);
	cin>>t;
	for(int i = 0 ; i < t ; i++)
	{
		sum = 0;
		cnt = 0;
		cin>>m>>s;
		for(int j = 0 ; j <= m ; j++)
		{
			if(sum < j)
			{
				cnt += j-sum;
				sum += j-sum;
			}
			sum += s[j] - '0';
		}
		cout<<"Case #"<<i+1<<": "<<cnt<<endl;
	}
}





