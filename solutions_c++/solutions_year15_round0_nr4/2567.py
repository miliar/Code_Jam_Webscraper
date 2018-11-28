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

int main()
{
	int i,t,n,m,p,r,c, ans=0, ctr, flag, success, x,sum=0,k,maxt=0,j;
	freopen("inp4.in", "r", stdin);
	freopen("outl.txt", "w", stdout);
    string answer;


	cin>>n;

	for(i=0;i<n;i++)
    {
        cin>>x>>r>>c;
        if(x==1) answer="GABRIEL";
        else if(x==2)
        {
            if(r%2 == 1 && c%2 == 1)
                answer="RICHARD";
            else answer="GABRIEL";
        }
        else if(x==3)
        {
            if((r==2 && c==3) || (r==3 && c==3) || (r==4 && c==3)|| (c==2 && r==3) || (c==4 && r==3)) answer="GABRIEL";
            else  answer="RICHARD";
        }
        else if(x==4)
        {
            if((r==3 && c==4) || (r==4 && c==3) || (r==4 && c==4)) answer = "GABRIEL";
            else answer="RICHARD";
        }


        cout<<"Case #"<<i+1<<": "<<answer<<endl;

    }

	return 0;
}
