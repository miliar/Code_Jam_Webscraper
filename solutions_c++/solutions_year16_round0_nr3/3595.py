#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;

long long p[20],q[200000][20];
char s[2000000];

long long bas(int str, int b){
	long long sum=0,bb=1;
	while(str){
		sum += bb*(str&1);
		bb *= b;
		str>>=1;
	}
	return sum;
}

long long div(long long str){
	if (str%2==0) return 2;
	if (str%3==0) return 3;
	for (long long i = 5, d = 2; i <= str/i && i < 10000; i+=d,d=6-d)
		if (str%i==0)
			return i;
	return 1;
}

bool sol(int str){
	for (int i = 2; i < 11; ++i)
	{
		long long d = div(bas(str, i));
		q[str][i]=d;
		if(d==1)
			return false;
	}
	return true;
}

int main(void){

	int g=0;
	memset(s,0,sizeof(s));
	for (int num = 1; num < 1e5; num+=2)
	{
		s[num] = sol(num);
		if(s[num]) {g++;}
		int x =num+1;
		// if((x&x-1)==0) printf("%d: %d\n",num, g);
	}
	// printf("%d\n",g);

    int t=0;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
    	int a,b;
    	scanf("%d%d",&a,&b);

        printf("Case #%d:\n", tt);

        for (int i = (1<<(a-1))+1; i < (1<<a) && b; i+=2)
        {
        	if (s[i])
        	{
        		b--;
        		printf("%lld", bas(i, 10));
       			for (int j = 2; j < 11; ++j)
       			{
       				printf(" %lld", q[i][j]);
       			}
       			printf("\n");
        	}
        }

     //    map<int,int> dict;
    	// while(b){
    	// 	int vic;
    	// 	do{
    	// 		vic = rand();
    	// 	}while(dict.find(vic) != dict.end());
    	// 	dict[vic] = 1;

    	// 	if (sol(vic))
    	// 	{
    	// 		--b;
    	// 		printf("");
    	// 	}
    	// }
    }
    return 0;
}

