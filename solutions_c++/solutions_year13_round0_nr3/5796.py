#include <stdio.h>
#include <math.h>

__int64 get(__int64 a){
	int i = 0;
	int b[15];
	while(a){
		b[i++] = a%10;
		a /= 10;
	}
	for(int j = 0; j < i/2; j++)
		if(b[j] != b[i-1-j])
			return 0;
    return 1;
}

__int64 cal(__int64 A,__int64 B){
	__int64 s = sqrt(A);
	__int64 e = sqrt(B);
	__int64 sum = 0;
	if (s*s < A)
		s = s + 1;
	for(__int64 i = s; i <= e; i++){
		if(get(i) && get(i*i)){
			sum++;
		}
	}
	return sum;
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	__int64 A,B;
	scanf("%d",&t);
	for(int k = 1; k <= t; k++){
		scanf("%I64d %I64d",&A,&B);
		printf("Case #%d: %I64d\n",k,cal(A,B));
	}
}