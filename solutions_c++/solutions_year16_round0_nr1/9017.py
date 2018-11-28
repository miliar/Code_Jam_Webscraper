#include <iostream>

using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin>>T;
	int digit[10];
	int i,j;
	for(int t=0;t<T;t++){
		int n;
		int p;
		cin >> n;
		p=n;
		if(n==0){
			printf("Case #%d: INSOMNIA\n", t+1);
		}
		else{
			for(i=0;i<10;i++){
				digit[i] = 0;
			}
			int x = n;
			int cnt = 0;
			while(x>0){
				if(digit[x%10]==0)cnt++;
				digit[x%10]=1;
				x/=10;
			}
			while(cnt < 10){
				n += p;
				x = n;
				while(x>0){
					if(digit[x%10]==0)cnt++;
					digit[x%10]=1;
					x/=10;
				}
			}
			printf("Case #%d: %d\n", t+1, n);
		}
	}

}