#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <utility>
#include <stack>
#include <queue>
#include <iomanip>
#include <list>
#include <bitset>
using namespace std;
void personal()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
}
int main()
{
	//personal();
	int t,s;
	string str;
	cin>>t;
	int c=1;
	while(t--)
	{
	long long sum=0;
	long long need=0;
		cin>>s;
		string str;
		cin>>str;
		for(int i=0;i<=s;i++)
		{
         if(sum<i && str[i]-'0'>0)
         {
         	need+=i-sum;
         	sum+=i-sum;
         }
         sum+=str[i]-'0';
		}
		cout<<"Case #"<<c++<<": "<<need<<endl;
	}
}