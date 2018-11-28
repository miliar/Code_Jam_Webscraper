#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<stack>
#include<queue>
#include<map>
#include<algorithm>
#include<string.h>
#include<vector>
#include<math.h>
#include<limits.h>
#include<deque>
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define ss(n) scanf("%s",n)
#define sf(n) scanf("%f",&n)

#define pi(n) printf("%d\n",n)
#define pl(n) printf("%lld\n",n)
#define ps(n) printf("%s\n",n)
#define pf(n) printf("%f\n",n)

#define ll long long int
#define r0 return 0
#define INF INT_MAX
#define FR(i,a,b) for(i=a;i<b;i++)
#define decit int i,j,k
int M=1000000000+7;
using namespace std;

int main()
{
    int t,it;
    si(t);

	FR(it,1,t+1)
	{
		ll ans=0,i;
		deque<char> q;
		string s,a;
		cin>>s;
		q.push_back(s[0]);
		cout<<"Case #"<<it<<": ";
		FR(i,1,s.size())
		{
			if(q.front() <= s[i])
				q.push_front(s[i]);
			else
				q.push_back(s[i]);
		}

		/*q.push_back('C');
			q.push_back('D');
			q.push_front('A');
		*/
			while(!q.empty())
			{
				char ch=q.front();
				q.pop_front();
				cout<<ch;
			}
			cout<<endl;
	}
	return 0;
}