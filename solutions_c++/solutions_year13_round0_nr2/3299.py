#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int N;
int M;
int p(int r,int c){return r*M+c;}
bool isRowFlat(int **g, int r,int c){
	int v=g[r][c];	
	for(int i=0;i<M;i++){
		if(g[r][i]!=v&&g[r][i]!=-1)return false;
	}
	return true;
}
bool isColumnFlat(int** g, int r, int c){
	int v=g[r][c];	
	for(int i=0;i<N;i++){
		if(g[i][c]!=v&&g[i][c]!=-1)return false;
	}
	return true;
}
void raiserow(int** g, int r){
	for(int i=0;i<M;i++){
		g[r][i]=-1;
	}
}
void raisecolumn(int** g,int c){
	for(int i=0;i<N;i++){
		g[i][c]=-1;
	}
}
void findlowestcell(int** g, int* _r,int* _c){
	int v=1000;
	for(int r=0;r<N;r++){
		for(int c=0;c<M;c++){
			if(g[r][c]<v&&g[r][c]!=-1){
				v=g[r][c];
				*_r=r;
				*_c=c;
			}
		}
	}
}
bool isAllRaised(int** g){
	for(int r=0;r<N;r++){
		for(int c=0;c<M;c++){
			if(g[r][c]!=-1)return false;
		}
	}
	return true;		
}
bool test(int** g){
	if(isAllRaised(g))return true;
	int r,c;
	findlowestcell(g, &r, &c);
	//printf("lowest cell %d %d\n",r,c);
	if(isRowFlat(g,r,c))raiserow(g,r);
	else if(isColumnFlat(g,r,c))raisecolumn(g,c);
	else return false;
	test(g);
}
	
			

int main(){
	freopen("B-large.in","r",stdin);freopen("b-large.out","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	//freopen("C-large-practice.in","r",stdin);freopen("C-large-practice.out","w",stdout);
	int numIter;
	scanf("%d",&numIter);
	for(int t=0;t<numIter;t++){
		scanf("%d %d",&N,&M);
		int* g_onedim=new int[N*M];
		int** g=new int*[N];
		for(int r=0;r<N;r++){
			g[r]=&g_onedim[r*M];
			for(int c=0;c<M;c++){
				int h;
				cin>>h;
				g[r][c]=h;
			}
		}
		/*for(int r=0;r<N;r++){
			for(int c=0;c<M;c++){
				cout<<g[r][c]<<" ";
			}
			cout<<endl;
		}*/
		bool ret=test(g);
		cout<<"Case #"<<t+1<<": "<<(ret?"YES":"NO")<<endl;
		delete[] g;
		delete[] g_onedim;
	}
	return 0;
}
