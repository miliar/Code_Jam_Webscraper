#include <cstring>
#include <cstdio>
#include <iostream>
#include <set>
#include <iterator>
using namespace std;
int T;
multiset<int>s;
multiset<int>::iterator p,pp;
int n;
int x,t;
int main(){
	scanf("%d",&T);
	int ca=1;
	while(T--){
		s.clear();
		scanf("%d%d",&n,&x);
		for (int i=0;i<n;i++){
			scanf("%d",&t);
			s.insert(t);
		}
		int ans=0;
		while(!s.empty()){
			p=s.begin();
			int tmp=(*p);
			s.erase(p);
			pp=s.upper_bound(x-tmp);
			if(pp==s.begin()) {
				ans++;
				continue;
			}
			else {
				pp--;
				ans++;
				s.erase(pp);
			}
		}
		printf("Case #%d: %d\n",ca++,ans);
	}
	return 0;
}
