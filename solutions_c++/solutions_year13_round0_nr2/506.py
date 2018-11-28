#include<cstdio>

int main(){
	int t,tab[100][100],m,n;
	scanf("%d", &t);
	for(int caso=1;caso<=t;caso++){
		scanf("%d %d",&m,&n);
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
				scanf("%d",&tab[i][j]);
		bool ok=1;
	  for(int i=0;i<m;i++)
			for(int j=0;j<n;j++){
				bool l=1,c=1;
				for(int k=0;k<n;k++)
					if(tab[i][k]>tab[i][j])
						l=0;
				for(int k=0;k<m;k++)
					if(tab[k][j]>tab[i][j])
						c=0;
				if(!l&&!c)ok=0;
			}
		if(ok)printf("Case #%d: YES\n",caso);
		else printf("Case #%d: NO\n",caso);
	}
	return 0;
}
