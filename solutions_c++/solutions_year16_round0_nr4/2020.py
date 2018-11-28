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

	//while(cin>>n)

	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		ll K,C,S;
		cin>>K>>C>>S;
		if(C*S<K){
			cout<<"Case #"<<cas<<": IMPOSSIBLE"<<endl;
			continue;
		}
		cout<<"Case #"<<cas<<":";
		ll now=0;
		for(ll i=0;i<K;i++)
		{
			if(i&&i%C==0){
				cout<<' '<<now+1;
				now=0;
			}
			now*=K;
			now+=i;
		}
		cout<<' '<<now+1<<endl;
		//cout<<"Case "<<cas<<": ";
	}

	return 0;
}
