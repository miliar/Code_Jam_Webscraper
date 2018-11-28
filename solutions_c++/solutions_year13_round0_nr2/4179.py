#include <cstdio>
using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int k=1;k<=T;k++){
		int n;int m;
		scanf(" %d %d",&n,&m);
		int a[n][m];
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf(" %d",&a[i][j]);
		bool flag2 = false;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				bool flag1=true;
				bool flag3=true;
				int max = a[i][j];
				for(int p=0;p<n;p++)
					if (a[p][j]>max)
						flag1=false;
				for(int q=0;q<m;q++)
					if(a[i][q]>max)
						flag3=false;
				if (flag3==false && flag1==false){
					flag2 = true;
					break;
				}
			}
			if (flag2==true) break;
		}
		if (flag2==false) printf("Case #%d: YES\n",k);
		else printf("Case #%d: NO\n",k);
	}
}
