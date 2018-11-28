#include <vector>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <bitset>
#include <map>
#include <queue>
#include <climits>
#include <bitset>
#define LL long long
#define INFI 100000000000
#define D double
using namespace std;
#include <iomanip>


int main()
{
	
	LL t;
	cin>>t;
	LL tt=0;
	while(tt<t)
	{
		LL n;
		cin>>n;
		string s;
		cin>>s;
		LL ans=s[0]-'0';
		LL m = 0;
		for(LL i=1; i<s.size(); i++)
		{
			if(ans < i)
			{
				m = max(m,abs(i-ans));
			}
			ans+=s[i]-'0';
		}
			
		//cout<<endl;
		
		cout<<"Case #"<<tt+1<<": "<<m<<endl;
		tt++;
	}
	return 0;
	
}


//6 4
//1 3 2 3 4 1