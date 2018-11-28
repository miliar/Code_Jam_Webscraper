#include <map>

#include <set>

#include <cmath>

#include <ctime>

#include <deque>

#include <queue>

#include <stack>

#include <bitset>

#include <cctype>

#include <cstdio>

#include <vector>

#include <cassert>

#include <complex>

#include <cstdlib>

#include <cstring>

#include <fstream>

#include <iomanip>

#include <sstream>

#include <iostream>
using namespace std;
int main()
{
	freopen("in.in", "r", stdin);
    freopen("out", "w", stdout);
	int t,Smax,count=0,ans,test=1;
	string ar;
	cin>>t;
	while(t--)
	{
		
		count =0,ans=0;
		cin>>Smax;
		cin>>ar;
		
		for(int i=0;i<=Smax;i++)
		{
			
			if(count>=i)
			{
				
				count+=ar[i]-48;
				
				
				
			}
			else
			{
				
				ans++;
				
				count+=1+ar[i]-48;
				;
				
				
			}
		}
		cout<<"Case #"<<test<<": "<<ans<<endl;
		test++;
		//cout<<endl;
	}
	return 0;
	
}
