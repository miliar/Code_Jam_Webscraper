#include <cstdio>
#include <set>
using namespace std;

void op(int x){
	set<int> s;
	s.insert(-1);
	int n,a;
	scanf("%d",&n);
	if(n==0){
		printf("Case #%d: INSOMNIA\n",x);
		return;
	}
	for(int i=1;s.size()<11;++i){
		a=i*n;
		while(a){
			s.insert(a%10);
			a/=10;
		}
		a=i*n;
	}
	printf("Case #%d: %d\n",x,a);
	return;
}

int main(){
	int t,i=1;
	scanf("%d",&t);
	while(i<=t){
		op(i);
		++i;
	}
}