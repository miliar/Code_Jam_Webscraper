#include<stdio.h>
#include<math.h>
#include<string.h>

using namespace std;

int main(){
	char file[32] = "A-small-attempt1";
	freopen(strcat(file,".in"),"r",stdin);
	freopen(strcat(file,".out"),"w",stdout);      
	long long T, cnt=1;
	long long k = 1, r, t;
	long long result = 0;
	scanf("%lld",&T);
	while(T-->0){
		scanf("%lld %lld",&r,&t);
		while(true){
			if(t >= (2*k*(k+1)+k*(2*r-3))){
				result++;
				k++;
				continue;
			}
			break;
		}
		printf("Case #%lld: %lld\n", cnt++,result);
		result = 0;
		k = 1;
	}
}