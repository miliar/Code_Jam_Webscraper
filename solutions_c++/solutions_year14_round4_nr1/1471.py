#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		int n,x;
		cin>>n>>x;
		vector<int> v(n);
		for(int i=0;i<n;i++) cin>>v[i];
		sort(v.begin(),v.end());
		int a=0,b=n-1,kolo=0;
		while(a<=b){
			if(v[a]+v[b]<=x){
				a++;
				b--;
				kolo++;
			}
			else{
				kolo++;
				b--;
			}
		}
		printf("Case #%d: %d\n",t+1,kolo);


	}
	return 0;

}
