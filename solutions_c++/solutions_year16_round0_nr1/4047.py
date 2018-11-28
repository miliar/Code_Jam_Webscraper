#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;


int main(int argc, char *argv[]) {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	
	int t;
	cin>>t;
	for(int Case=1;Case<=t;Case++)
	{
		int n;
		cin>>n;
		cout<<"Case #"<<Case<<": ";
		if(!n) puts("INSOMNIA");
		else 
		{
			int book[10]={};
			for(long long i=1;;i++)
			{
				long long now = i*n;
				while(now) book[now%10] = 1 , now/=10;
				
				bool ok = true;
				for(int i=0;i<10;i++) if(!book[i]) { ok = false; break; }
				if(ok) { cout<<i*n<<endl; break; }
			}
		}
	}
	
	return 0;
}