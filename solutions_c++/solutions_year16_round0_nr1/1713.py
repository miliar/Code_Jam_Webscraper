#include<cstdio>
#include<algorithm>

using namespace std;

int x, n, casos, v[20];

int vale(){
	for(int i=0;i<=9;i++) if(!v[i]) return 0;
	return 1;
}

int main(){
	scanf(" %d", &casos);
	for(int inst=0;inst<casos;inst++){
		scanf(" %d", &n);
		if(n == 0) x = -1;
		else{
			x = n;
			for(int i=0;i<=9;i++) v[i] = 0;
			while(!vale()){
				for(int j=x;j>0;j/=10) v[j%10] = 1;
				x += n;
			}
		}
		
		printf("Case #%d: ", inst+1);
		if(x == -1)	printf("INSOMNIA\n");
		else printf("%d\n", x-n);
	}
	return 0;
}
