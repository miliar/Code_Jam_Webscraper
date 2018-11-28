#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<fstream>
#include<cstring>
#include<stack>
#include<cstdio>
#include<cmath>
#include<set>
#include<map>
#include<queue>
#define ll long long int
using namespace std;
std::queue<int>q;
ll calc(int x)
{
    ll cnt=0,val1;
    while(!q.empty())
    {
     val1=q.front();
     q.pop();
     if(val1>x)
     {
        if(val1-x>x)
            q.push(val1-x);
        cnt++;
        }
    }
    return cnt;
}
ll t,i,j,a[1000000],ans,n;
int main()
{
    ifstream cin;
	ofstream cout;
	cin.open("C:\\Users\\Admin\\Downloads\\4.in");
	cout.open("C:\\Users\\Admin\\Downloads\\out.txt");
    cin>>t;
    ll x=1;
    while(t--)
    {
    ans=1005;
        cin>>n;
        for(i=0; i<n; i++)
        cin>>a[i];
        for(i=1;i<=1000;i++)
        {
            while(!q.empty())
            q.pop();
            for(j=0;j<n;j++)
            q.push(a[j]);
            ans=min(ans,calc(i)+i);
        }
        cout<<"Case #"<<x++<<": "<<ans<<endl;

    }
    return 0;
}
