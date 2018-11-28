#include <cstdio>

using namespace std;

int CountSheep(int n){
	bool digit[10] = {0};
	for(int j=n,k=j; ;j+=n,k=j ){
		while( k ){
			int last_num = k % 10;
			k /= 10;
			digit[last_num] = true;
		}
		for(k=0; k<10; ++k)	if( !digit[k] )	break;
		if( k==10 )	return j;
	}
}

int main(void){
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int c, cc=0, n, ans;
	
	scanf("%d", &c);
	while( c-- ){
		scanf("%d", &n);
		printf("Case #%d: ", ++cc);
		if( n==0 )	puts("INSOMNIA");
		else		printf("%d\n", CountSheep(n));
	}
	
	return 0;
}

