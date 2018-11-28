#include <stdio.h>
#include <string.h>


char str[105][105];
int lrow[105];
int rrow[105];
int ucol[105];
int dcol[105];

int mmin(int a,int b)
{
	return a<b?a:b;
}

int mmax(int a,int b)
{
	return a>b?a:b;
}

int main()
{
	int cas;
	int r,c;
	freopen("A-large.in","r",stdin);
	freopen("pa.out","w",stdout);
	scanf("%d",&cas);
	for(int T=1; T<=cas; T++){
		scanf("%d %d",&r,&c);
		for(int i=0; i<r; i++){
			scanf("%s",str[i]);
		}
		memset(lrow,0x3f,sizeof(lrow));
		memset(rrow,-1,sizeof(rrow));
		memset(ucol,0x3f,sizeof(ucol));
		memset(dcol,-1,sizeof(dcol));
		for(int i=0; i<r; i++){
			for(int j=0; j<c; j++){
				if(str[i][j]!='.'){
					lrow[i]=mmin(lrow[i],j);
					rrow[i]=mmax(rrow[i],j);
					ucol[j]=mmin(ucol[j],i);
					dcol[j]=mmax(dcol[j],i);
				}
			}
		}
		bool fail=false;
		int ans=0;
		for(int i=0; i<r; i++){
			for(int j=0; j<c; j++){
				switch(str[i][j]){
					case '^':
						if(ucol[j]>=i)
							ans++;
						break;
					case 'v':
						if(dcol[j]<=i)
							ans++;
						break;
					case '<':
						if(lrow[i]>=j)
							ans++;
						break;
					case '>':
						if(rrow[i]<=j)
							ans++;
						break;
				}
				if(str[i][j]!='.' && ucol[j]>=i && dcol[j]<=i && lrow[i]>=j && rrow[i]<=j){
					fail=true;
				}
			}
		}
		printf("Case #%d: ",T);
		if(fail==true){
			printf("IMPOSSIBLE\n");
		}else{
			printf("%d\n",ans);
		}
	}
	return 0;
}
