#include <bits/stdc++.h>

using namespace std;

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define abs(x) ((x)<0?-(x):(x))
#define pii pair<int,int>
#define m_p make_pair(n,m)
#define mod 1000000007
#define pb push_back
#define bp(x) __builtin_popcount(x)
typedef long long int ll;
int main()
{
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	ios::sync_with_stdio(false);cin.tie(0);
	int t,z,i,j;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		string a,ans1,temp2;
		cin>>a;
		ans1="";
		for(i=0;i<a.length();i++)
			ans1+="+";
        queue <string> q;
        map <string,int > dist;
		map <string,int > hash;
		q.push(a);
		hash[a]=1;
		dist[a]=0;
		int value=0;
        while(!q.empty())
        {
        	string temp=q.front();
        	//cout<<temp<<"\n";
        	q.pop();
        	if(temp.compare(ans1)==0)
    		{
    			value=dist[temp];
    			break;
    		}
        	for(j=1;j<=temp.length();j++)
        	{
				temp2=temp.substr(0,j);
				for(int i=0;i<temp2.length();i++)
				{
					if(temp2[i]=='+')
						temp2[i]='-';
					else
						temp2[i]='+';
				}
				reverse(temp2.begin(),temp2.end());
        		temp2=temp2+temp.substr(j,temp.length()-j);
				if(!hash[temp2])
			    {
					hash[temp2]=1;
					dist[temp2]=dist[temp]+1;
					q.push(temp2);   		
	        	}
	        }
        }
        cout<<"Case #"<<z<<": "<<value<<"\n";
	}
	return 0;
}
