#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<bitset>
#include<cstring>
#include<cmath>

using namespace std;

int check(long long x){
	long long lim = sqrt(double(x));
	for(int i=2;i<=lim;i++)
		if(x%i==0)
			return i;
	return 0;
}

long long convert(int x,int base){
	long long tmp=1,ret=0;
	while(x){
		ret+=(x%2)*tmp;
		x/=2;
		tmp*=base;
	}
	return ret;
}

int ans[15];

void print_ans(int x){
	int s[20],tail=0;
	while(x){
		s[++tail] = x%2;
		x/=2;
	}
	while(tail)
		printf("%d",s[tail--]);
	for(int i=2;i<=10;i++)
		printf(" %d",ans[i]);
	printf("\n");
}

int main(){
	//freopen("B-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int t;
	scanf("%d",&t);
	printf("Case #1:\n");
	int tot=1<<17,cnt=50;
	for(int i=(1<<15)+1;i<tot;i+=2){
		bool flag=true;
		for(int j=2;j<=10;j++){
			long long tmp = convert(i,j);
			int tmp1 = check(tmp);
			if(!tmp1){
				flag = false;
				break;
			}
			ans[j]=tmp1;
		}
		if(flag){
			print_ans(i);
			cnt--;
			if(!cnt)
				break;
		}
	}
	
	
	return 0;
} 
