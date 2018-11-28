#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <queue>
#include <functional>
#include <list>
#include <set>
#include <sstream>
#define ll long long

using namespace std;

int main()
{
	ios::sync_with_stdio(false);

	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		int n,ans,vn=0;
		cin>>n;
		if(n==0){
			cout<<"Case #"<<cas<<": INSOMNIA"<<endl;
			continue;
		}
		int vis[10]={0};
		for(ans=n;;ans+=n)
		{
			int t=ans;
			while(t)
			{
				if(!vis[t%10])
					vis[t%10]=1,vn++;
				t/=10;
			}
			if(vn==10)break;
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
		//cout<<"Case "<<cas<<": ";
	}

	return 0;
}
