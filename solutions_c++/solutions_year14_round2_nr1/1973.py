#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

int t,n;
char str[200][200];
char ch[200];
int cur,tmp;
char curch;
int counter[200][200];
bool ok;
int a[200];
int ans;


int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for ( int i = 1; i <= t; ++ i){
		printf("Case #%d: ",i);
		memset(counter,0,sizeof(counter));
		ok = true;
		scanf("%d\n",&n);
		for ( int j = 1; j <= n; ++ j){
			scanf("%s\n",str[j]);
			if (j == 1){
				cur = 0;
				ch[0] = '!';
				for ( int k = 0; k < strlen(str[j]); ++ k){
					if (str[j][k] != ch[cur]){
						++ cur;
						ch[cur] = str[j][k];
						++ counter[j][cur];
					}
					else ++ counter[j][cur];
				}
				ch[cur+1] = '#';
			}
			else{
				tmp = 0;
				for ( int k = 0; k < strlen(str[j]); ++ k){
					if (str[j][k] != ch[tmp]){
						++ tmp;
						if (str[j][k] != ch[tmp]){
							ok = false;
							break;
						}
					}
					++ counter[j][tmp];
				}
				if (tmp < cur) ok = false;
			}
			if (!ok) break;
		}
		if (!ok){
			printf("Fegla Won");
		}
		else{
			ans = 0;
			for ( int j = 1; j <= cur; ++ j){
				for ( int k = 1; k <= n; ++ k){
					a[k-1] = counter[k][j];
				}
				sort(a,a+n);
				for ( int k = 0; k < n; ++ k)
					ans += abs(a[k] - a[n/2]);
			}
			printf("%d",ans);
		}
		printf("\n");
	}

	return 0;
}
