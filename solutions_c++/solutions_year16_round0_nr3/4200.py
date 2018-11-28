#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <map>
#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807LL
#define INF 2000000000
#define PI acos(-1.0)
#define inf INT_MAX
using namespace std;
typedef long long int LL;
LL valueinbase[40000][12];
vector<int > primes;
int is_prime[10000010];
void seive(){
for(int i=0;i<=10000005;i++)
	is_prime[i] = 1;
is_prime[1] = 0;
is_prime[0] = 0;
for(long long int j=2;j<=10000000;j++){
	if(is_prime[j]==1){
		primes.push_back(j);
		for(long long int k=(j*j);k<=10000000;k+=j)
			is_prime[k] = 0;
	}
}
}
int prime(long long int x)
{if(x<=1)return 0;if(x<=3)return 1;if(x%6==1||x%6==5)
{long long int y=sqrt(x),i;for(i=2;i<=y;i++)if(x%i==0)return 0;return 1;} return 0;}


LL base_power[12][60];



int main()
{

//declarations
int N , J , test;

//code for precalculating some values
for(int i=0;i<12;i++)
	base_power[i][0] = 1;

for(int i=1;i<60;i++){
	for(int base=2;base<=10;base++)
		base_power[base][i] = (base_power[base][i-1] * base);
}


seive();
scanf("%d",&test);
scanf("%d %d",&N,&J);
for(int i=0;i<base_power[2][N-1]+20;i++){
	for(int j=0;j<=12;j++)
		valueinbase[i][j] = 0;
}


int flag = 0;
int counter = 1;

printf("Case #1: \n");
for(int i=1;i<pow(2 , N-1) && counter<=J;i+=2)
{

	for(int j=15;j>=0;j--){
		if((i&(1<<j))!=0){
			for(int base=2;base<=10;base++)
				valueinbase[i][base]+=pow(base , j);
		}
	}
	flag = 0;
	for(int base=2;base<=10 && flag==0;base++)
	{
		valueinbase[i][base]+=pow(base , N-1);
		if(valueinbase[i][base]<=10000000)
			flag = (flag | is_prime[valueinbase[i][base]]);
		else
			flag = (flag | prime(valueinbase[i][base]));		
	}
	if(flag==0){
			// printf("$$$%d##%lld##%lld$$$\n", counter , valueinbase[i][9] , valueinbase[i][10]);	
		printf("%lld ", valueinbase[i][10]);
		for(int base=2;base<=10;base++){
			for(int factor=2;;factor++){
				if(valueinbase[i][base]%factor == 0){
					printf("%d ",factor );
					break;
				}
			}
		}
		printf("\n");
		counter++;
	}

}

return 0;
}


























