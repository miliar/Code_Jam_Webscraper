#include <cstdio>

using namespace std;

int rob(int n)
{
	int r,x,s;
	scanf("%d%d",&r,&s);
	int ria[r];
	int stl[s];
	for(int i=0;i<r;i++) ria[i]=-1;
	for(int i=0;i<s;i++) stl[i]=-1;
	int pole[r][s];
	for(int i=0;i<r;i++){
		for(int j=0;j<s;j++){
			scanf("%d",&x);
			pole[i][j]=x;
			if(x>ria[i]) ria[i]=x;
			if(x>stl[j]) stl[j]=x;
		}
	}
	for(int i=0;i<r;i++){
		for(int j=0;j<s;j++){
			if(pole[i][j]!=ria[i] && pole[i][j]!=stl[j]){
				printf("Case #%d: NO\n",n+1);
				return 0;
			}
		}
	}
	printf("Case #%d: YES\n",n+1);
	return 0;
}

int main()
{
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++) rob(i);

	return 0;
}
