#include<iostream>
#include<cstdio>
#include<set>

using namespace std;
void program(int t){
	set<int> s;
	for(int i=0; i<10; ++i){
		s.insert(i);
	}
	long long int n;
	scanf("%lld",&n);
	if(n == 0){
		printf("Case #%d: INSOMNIA\n",t);
		return;
	}
	for(long long int i=1; ;++i){
		long long int N = n*i;
		long long int temp = N;
		while(temp > 0){
			s.erase(temp%10);
			temp /= 10;
		}
		if(s.size() == 0){
			printf("Case #%d: %lld\n",t,N);
			break;
		}
	}	
}
int main(){
	int t;
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	int T = t;
	while(t--){
		program(T-t);
	}
}
