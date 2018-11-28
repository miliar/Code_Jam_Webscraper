#include<cstdio>

#define N 105
using namespace std;

int tc,n,m;
int data[N][N];
int main(){
	int i,j,k,l,c;
	freopen("b2.in", "r", stdin);
	freopen("b2.out","w",stdout);
	scanf("%d",&tc);
	for(int tcc=1;tcc<=tc;tcc++){
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				scanf("%d", &data[i][j]);
		c=1;
		for(i=0;i<n && c;i++){
			for(j=0;j<m && c;j++){
				for(k=0;k<n;k++)
					if (data[i][j]<data[k][j])
						break;
				for(l=0;l<m;l++)
					if (data[i][j]<data[i][l])
						break;
				if (k!=n && l!=m)
					c=0;
			}
		}
		printf("Case #%d: %s\n",tcc,(c)? "YES":"NO");
	}
	return 0;
}

/*


Input 
 	
Output 
 
3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1
Case #1: YES
Case #2: NO
Case #3: YES

*/