#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>

int T;
__int64 a,b;

bool isPalindrome(__int64 tar){
	char sint[20];
	int len;
	_i64toa(tar, sint, 10);
	len = strlen(sint);

	int s = 0, f = len-1;
	while(s<f){
		if(sint[s] != sint[f])
			break;
		s++; f--;
	}
	if(s<f) return false;
	else return true;
}

int main(void){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		scanf("%I64d %I64d",&a,&b);
		printf("Case #%d: ",i+1);

		__int64 la = (__int64)(sqrt((long double)a));
		__int64 lb = (__int64)(sqrt((long double)b));

		if(la * la != a) la = la + 1;

		int cnt = 0;
		for(__int64 j=la;j<=lb;j++){
			if(isPalindrome(j)){
				if(isPalindrome(j*j)){
					cnt++;
				}
			}
		}
		printf("%d\n",cnt);
	}
}