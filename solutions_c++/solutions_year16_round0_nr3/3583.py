#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<string>
using namespace std;
char A[501][35];
unsigned long long P[11];
unsigned long long D[11];
int T, N, J;
int r;
void convert(unsigned long long num, int index) {
	if (num == 0) return;
	convert(num / 2 , index-1);
	A[r][index] = num % 2 + '0';
}
bool isPrime(unsigned long long cnt, int k, int len){
	for (unsigned long long i = 2; i <= sqrt(cnt); i++){
		if (cnt % i == 0){
			P[k] = i;
			return false;
		}
	}
	return true;
}
bool makeDisit(char * str, int len){
	for (int k = 2; k <= 10; k++){
		unsigned long long cnt = 0;
		for (int i = 1; i <= len; i++){
			cnt += unsigned long long(pow(k, len - i)) * unsigned long long(str[i-1]-'0');
		}
		D[k] = cnt;
		if (isPrime(cnt, k, atoi(str)))
			return false;
	}
	return true;
}
int main(){
	
	freopen("testcaseC.txt", "r", stdin);
	freopen("outputC.txt", "w", stdout);
	
	scanf("%d", &T);
	scanf("%d %d", &N, &J);
	int aaa = 0;
	printf("Case #1:\n");
	for (unsigned long long i = unsigned long long(pow(2, N-1)) + 1; i < unsigned long long(pow(2, N)); i += 2){
		convert(i, N - 1);
		r++;
		if (makeDisit(A[r - 1], strlen(A[r - 1]))){
			printf("%s ",A[r - 1]);
			for (unsigned long long i = 2; i <= 10; i++){
				printf("%llu ",P[i]);
			}
			printf("\n");
			aaa++;
		}

		if (aaa == J)
			break;
	}

}