#include<stdio.h>
#include<set>
using namespace std;
int main(){
	int _,T,n;
	scanf("%d",&_);
	for(T=1; T<=_; T++){
		scanf("%d",&n);
		set<int> s;
		for(int i=0; i<2*n-1; i++)
			for(int j=0; j<n; j++){
				int x;
				scanf("%d",&x);
				if(s.count(x))
					s.erase(x);
				else
					s.insert(x);
			}
		printf("Case #%d:",T);
		for(set<int>::iterator it=s.begin(); it!=s.end(); it++)
			printf(" %d",*it);
		puts("");
	}
	return 0;
}
