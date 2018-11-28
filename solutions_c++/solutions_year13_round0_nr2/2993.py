// B

#include<cstdio>
#include<iostream>
#include<string>
#include<queue>
#include<vector>
using namespace std;

class node {
public:
	int x,y;
	node(int a,int b){
		x=a; y=b;
	}
	node(){
		x=0; y=0;
	}
};

int n,m,a[100][100],num[101],k;

int main() {
	int test,Z=1,i,j,tmp,check,res;

	FILE *fo=fopen("B-large.in","r");
	freopen("output.txt","w",stdout);

	fscanf(fo,"%d",&test);
	while(test--){
		vector<node>oh[101];
		res=0;
		fscanf(fo,"%d %d",&n,&m);
		for ( i=0; i<n; i++ ) {
			for ( j=0; j<m; j++ ) {
				fscanf(fo,"%d",&a[i][j]);
				oh[a[i][j]].push_back(node(i,j));
			}
		}

		for ( i=1; i<=100&&res==0; i++ )  {
			for ( j=0; j<oh[i].size(); j++ ) {
				node tmp=oh[i][j];
				check=0;
				for ( k=0; k<n; k++ ) {
					if ( a[k][tmp.y]>i ) {check++;break;}
				}
				for ( k=0; k<m; k++ ) {
					if ( a[tmp.x][k]>i ) {check++;break;}
				}
				if ( check==2 ) res=1;
			}
		}

		printf("Case #%d: ",Z++);
		if ( res==1 ) printf("NO\n");
		else printf("YES\n");
	}
	return 0;
}