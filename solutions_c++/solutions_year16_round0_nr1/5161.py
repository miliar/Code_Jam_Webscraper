#include <bits/stdc++.h>

using namespace std;

int n,f[11];

int main(){
	int T;
	cin >> T;
	for (int ti=1;ti<=T;ti++){
		scanf("%d",&n);
		memset(f,0,sizeof(f));
		printf("Case #%d: ",ti);
		if (n==0) puts("INSOMNIA");
			else{
				int x=n;
				while (1){
					int y=x;
					while (y){
						f[y%10]=1;
						y/=10;
					}
					int bo=1;
					for (int i=0;i<10;i++)
						if (f[i]==0){bo=0;break;}
					if (bo) break;
					x+=n;
				}
				printf("%d\n",x);
			}
	}
	return 0;
}