#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<fstream>
using namespace std;


int a[11],ans;

void calc(int x){
	memset(a,0,sizeof(a));
	int t = 0, times = 0, tmp;
	ans = 0;
	while(times<=10000){
		ans += x;
		tmp = ans;
		while(tmp){
			if(a[tmp%10] ==0){
				a[tmp%10] =1;
				t++;
			}
			tmp/=10;
		}
		times++;
		if(t==10) break;
	}
	if(t!=10) ans = -1;
}

int main()
{
	int N,n,T;
	ofstream cout("1.txt");
	scanf("%d",&N);
	while(N--){
		scanf("%d",&n);
		printf("Case #%d: ",++T);
		if(n==0) printf("INSOMNIA\n");
		else{
			calc(n);
			printf("%d\n",ans);
		}
	}
	return 0;
}
