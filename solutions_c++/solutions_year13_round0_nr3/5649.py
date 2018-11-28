#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define rep(n) REP(i,n)

const int MAXN=1024;
bool palis[MAXN];

int main()
{
	REP(i,9) palis[i+1]=true;
	REP(i,9) palis[(i+1)*10+(i+1)]=true;
	REP(i,9) REP(j,9) palis[(i+1)*100+(j+1)*10+(i+1)]=true;

	int n; cin>>n; rep(n)
	{
		int a,b,ans=0; cin>>a>>b;
		for(int j=1;j*j<=b;++j) if(a<=(j*j))
		{
			if(palis[j]&&palis[j*j]) ++ans;
		}

		cout<<"Case #"<<i+1<<": "<<ans<<endl;;
	}


	return 0;
}
