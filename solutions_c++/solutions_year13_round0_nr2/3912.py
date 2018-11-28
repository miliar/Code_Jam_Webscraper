#include<iostream>
#include<cstdlib>
#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int tab[110][110];
int ini[110][110];
int maxim[110];
int main(){

	int t;	
	scanf("%d",&t);
	int n,m;
	for(int p=0;p<t;p++){
		printf("Case #%d: ",p+1);

		scanf("%d %d",&n,&m);

		for(int x=0;x<n;x++)
			for(int y=0;y<m;y++)
				scanf("%d",&tab[x][y]),ini[x][y]=100;
		
		int mas = -1;
		for(int x=0;x<n;x++){
			maxim[x]=mas;
			for(int y=0;y<m;y++){
				maxim[x]=max(maxim[x],tab[x][y]);
			}
			for(int y=0;y<m;y++)
				ini[x][y]=maxim[x];
		}

		for(int y=0;y<m;y++){
			maxim[y]=mas;
			for(int x=0;x<n;x++){
				maxim[y]=max(maxim[y],tab[x][y]);
			}
			for(int x=0;x<n;x++)
				ini[x][y]=min(ini[x][y],maxim[y]);
		}

		bool resp = true;


		for(int x=0;x<n && resp;x++){
			for(int y=0;y<m && resp;y++)
				resp=resp && ini[x][y]==tab[x][y];
		}


		if(resp) printf("YES");
		else printf("NO");

		if(p!=t-1)
			printf("\n");
	}
	return 0;
}
