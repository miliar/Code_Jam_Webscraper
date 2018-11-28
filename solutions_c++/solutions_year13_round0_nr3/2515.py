#include<fstream>
#include<iostream>
#include<sstream>
#include<bitset>
#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<iterator>
#include<string>
#include<cassert>
#include<cctype>
#include<climits>
#include<cmath>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>

using namespace std;

unsigned long long int inp[39]=
{1, 2, 3, 11, 22,101, 111, 121, 202, 212,1001, 1111, 2002, 10001, 10101,10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111,200002, 1000001, 1001001, 1002001, 1010101,1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002};
unsigned long long int  ou[39];

 unsigned long long int m,n;

int fair_sq(){
	int count=0;
//	printf("%llu,%llu\n",m,n);
for(int i=0;i<39;i++)
	if(m<=ou[i] && n>=ou[i])
		count++;
		return count;
}


int main(){
	int T=0;
	scanf("%d",&T);
	for(int t=0;t<39;t++){
		 ou[t]=(unsigned long long int) inp[t]*inp[t];
 //       printf("%llu\n",ou[t]);
	}	
	 for(int t=1;t<=T;t++){
		 scanf("%llu %llu" ,&m,&n);		
        printf("Case #%d: %d\n",t,fair_sq());
	}	
	return 0;
}