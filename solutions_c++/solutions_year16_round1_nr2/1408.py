#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
#define inf 1000000


int main()
{
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);
	int tcase,t,i,len,n,num,j;
	scanf("%d",&tcase);
	map<int,int>my;
	vector<int>v;
	set<int>st;
	set<int>::iterator it;
	for(t=1;t<=tcase;t++)
	{
		my.clear();
		v.clear();
		st.clear();
		scanf("%d",&n);
		for(i=1;i<=2*n-1;i++)
		{
			for(j=1;j<=n;j++)
			{
				scanf("%d",&num);
			    v.push_back(num);
			    my[num]++;
			}
		}
		len = v.size();
		for(i=0;i<len;i++)
		{
			if(my[v[i]]%2==1)
			{
				st.insert(v[i]);
			}
		}
		
		
		printf("Case #%d: ",t);
		for(it=st.begin();it!=st.end();it++)
		{
			cout<<*it<<" ";
		}
		cout<<endl;
		
	}
}

