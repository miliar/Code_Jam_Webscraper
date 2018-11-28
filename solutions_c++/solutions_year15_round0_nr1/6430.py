#include <cstdio>

using namespace std;


const int MAXN = 1010;


int t;
int n;
char c[MAXN];

int main(){

	scanf("%d", &t);

	for(int q=0; q<t; q++){
		scanf("%d", &n);

		scanf("%s", c);
		int ppl=0;
		int fri=0;
		for(int i=0; i<=n; i++){
			if(c[i] == '0')	continue;
			if(ppl >= i){
				ppl+=c[i]-'0';
			}else{
				fri+=i - ppl;
				ppl = i + c[i] - '0';
			}
		}
	printf("Case #%d: %d\n", q+1, fri);
	}
	return 0;
}
