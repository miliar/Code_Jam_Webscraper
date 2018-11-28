#include <cstdio>
#include <algorithm>
struct val{
	int x,y,z;
};
typedef struct val pro;

bool rowCheck(int x, int z);
bool colCheck(int y, int z);
bool compare(pro a, pro b);


int a[100][100];
pro b[10000];
bool c[100][100];
int N,M;

bool compare(pro a, pro b)
{
	return a.z < b.z ? true : false;
}

int main()
{
	int T,flag;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		flag = 1;
		printf("Case #%d: ",t);
		scanf("%d%d",&N,&M);
		
		for(int i=0,m=0;i<N;i++){
			for(int j=0;j<M;j++){
				scanf("%d",&a[i][j]);
				b[m].x=i;b[m].y=j;b[m++].z=a[i][j];
				c[i][j]=false;
			}
		}

		std::sort(b,b+N*M,compare);

		for(int i=0;i<N*M;i++){
			if(!c[b[i].x][b[i].y]){
				bool p = rowCheck(b[i].x,b[i].z);
				bool q = colCheck(b[i].y,b[i].z);
				if(p==false && q==false){
					flag = 0;
					printf("NO\n");
					break;
				}
			}			
		}

		if(flag){
			printf("YES\n");
		}
	}
	return 0;
}
bool rowCheck(int x, int z){
	for(int i=0;i<M;i++){
		if(!(a[x][i]<=z))
			return false;
	}
	for(int j=0;j<M;j++)
		c[x][j]=true;
	return true;
}
bool colCheck(int y, int z){
	for(int i=0;i<N;i++){
		if(!(a[i][y]<=z))
			return false;
	}
	for(int j=0;j<N;j++)
		c[j][y]=true;
	return true;
}
