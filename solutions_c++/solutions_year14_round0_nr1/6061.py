// Problem A. Magic Trick.cpp : 定义控制台应用程序的入口点。
//
#include<cstdio>
using namespace std;
int main(){
	int T;
	int n,m;
	int a[4][4],b[4][4];
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int cas = 1;cas<=T;cas++){
		scanf("%d",&n);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&m);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&b[i][j]);
			}
		}
		int k = 0;
		int tmp;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(a[n-1][i] == b[m-1][j]){
					tmp = a[n-1][i];
					k++;
				}
			}
		}
		if(k == 1){
			printf("Case #%d: %d\n",cas,tmp);
		}else if(k == 0){
			printf("Case #%d: Volunteer cheated!\n",cas);
		}else{
			printf("Case #%d: Bad magician!\n",cas);
		}
	}
	return 0;
}