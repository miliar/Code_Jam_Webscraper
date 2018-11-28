#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<bitset>

using namespace std;

int map[1000005];
void _test(){
	bitset<10> s;
	for(long long i=1;i<1000000;i++){
		s.reset();
		for(int j=1;j<=1000000;j++){
			long long tmp = i*j;
			while(tmp){
				s.set(tmp%10);
				tmp/=10;
			}
			if(s.all()){
				map[i] = j;
				break;
			}
		}
			
	}
	for(int i=1;i<1000000;i++)
		if(map[i] > 100 || map[i] == 0){
			printf("%d\n",i);
		}
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,x;
	bitset<10> s;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
		scanf("%d",&x);
		if(x == 0){
			printf("Case #%d: INSOMNIA\n",cas);
			continue;
		}
		s.reset();
		for(int i=1;i<=100;i++){
			int tmp=i*x;
			while(tmp){
				s.set(tmp%10);
				tmp=tmp/10;
			}
			if(s.all()){
				printf("Case #%d: %d\n",cas,x*i);
				break;
			}
		}
	}
	
	
	return 0;
} 
