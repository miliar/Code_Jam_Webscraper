//Author: Vipul Gaur
//I'll not bow, I'll not break, I'll shut the world away; I'll not fall, I'll not fake, I'll take your breath away...
#include<cstdio>
#include<vector>
#include<set>
#include<utility>
#include<map>
#include<cstring>
#include<string>
#include<algorithm>
#include<bitset>
#include<iostream>
#include<stack>
#include<queue>
#include<cmath>

#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pb push_back
#define mp make_pair
#define vi vector<int>
const int mod=1000000007;

using namespace std;

string values;

int main()
{
	int i,t,n,m,p,s, ctr, flag, success, x,sum=0,k,maxt=0,j, present, ans;
	freopen("inp1.in", "r", stdin);
	freopen("outl.txt", "w", stdout);

	cin>>n;

	for(i=0;i<n;i++)
    {
        cin>>s; present=0; ans=0;
        cin>>values;

        present+=(values[0]-'0');
        for(j=1; j<values.length(); j++)
        {
            if(present<j && values[j] != '0')
            {
                ans+=(j-present); present+=(j-present);
            }
               present+=(values[j]-'0');
        }

        cout<<"Case #"<<i+1<<": "<<ans<<endl;


    }

	return 0;
}
