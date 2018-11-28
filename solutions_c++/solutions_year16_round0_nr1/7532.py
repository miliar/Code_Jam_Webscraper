#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<deque>
#include<cstring>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	ios_base::sync_with_stdio(false);

	int t;
	cin>>t;

	for(int casenum=1;casenum<=t;casenum++)
	{
		long long n;
		cin>>n;

		if(n==0)
        {
            cout<<"Case #"<<casenum<<": INSOMNIA"<<endl;
            continue;
        }

		long long num=0, flag=0;
		do
		{
            num+=n;
		    long long temp=num;
		    while(temp!=0)
            {
                flag|=(1<<(temp%10));
                temp/=10;
            }
		}while(flag!=1023);

		cout<<"Case #"<<casenum<<": "<<num<<endl;
	}

	return 0;
}
