#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
#define re(i,s,t) for(int i=s;i<=t;i++)

int a[5][5],b[17];
int t,r;
vector<int> q;

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	cin >>t;
	int w=0;
	while(t--)
	{
		w++;
		memset(b,0,sizeof(b));
		cin >>r;
		re(i,1,4) re(j,1,4) cin >>a[i][j];
		re(i,1,4) b[a[r][i]]++;
		cin >>r;
		re(i,1,4) re(j,1,4) cin >>a[i][j];		
		re(i,1,4) b[a[r][i]]++;
		q.clear();
		re(i,1,16)
		 if(b[i]>1)q.push_back(i);
		printf("Case #%d: ",w);
		if(!q.size())cout <<"Volunteer cheated!"<<endl;
		if(q.size()>1)cout <<"Bad magician!"<<endl;
		if(q.size()==1)cout <<q.front()<<endl;
	}
	return 0;
}
