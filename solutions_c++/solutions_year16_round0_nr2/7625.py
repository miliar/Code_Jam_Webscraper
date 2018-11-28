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
	freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
	ios_base::sync_with_stdio(false);

	int t;
	cin>>t;

	for(int casenum=1;casenum<=t;casenum++)
	{
		string s;
		cin>>s;

		int ans=0;
		char lookingFor = '+';

		for(int i=0;i<s.length();i++)
        {
            if(s[i] == '-')
            {
                ans++;
                ans+=(i!=0);
                while(i<s.length()&&s[i]=='-')
                    i++;
                i--;
            }
        }

		cout<<"Case #"<<casenum<<": "<<ans<<endl;
	}

	return 0;
}
