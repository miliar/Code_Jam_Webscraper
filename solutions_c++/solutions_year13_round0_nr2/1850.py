#include<iostream>
#include<cstdio>
#include<vector>

using namespace std;

int main(){
	/*freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);*/
	int TC,n,m;
	cin>>TC;
	for(int tc=1; tc<=TC; tc++){
		cin>>n>>m;
		int mat[n][m];
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
				cin>>mat[i][j];
		bool sirve=true;
		for(int i=0; i<n && sirve; i++){
			for(int j=0; j<m; j++){
				bool puede_fila=true,puede_col=true;				
				//pruebo la fila				
				for(int col=0; col<m; col++){
					if(j!=col && mat[i][col]>mat[i][j]){
						puede_fila=false;						
					}						
				}
				//prueba la columna
				for(int fil=0; fil<n; fil++){
					if(i!=fil && mat[fil][j]>mat[i][j]){
						puede_col=false;
					}
				}
				if(!puede_fila && !puede_col){
					sirve=false;
				}
			}
		}
		cout<<"Case #"<<tc<<": ";
		if(sirve){
			cout<<"YES";			
		}
		else{
			cout<<"NO";
		}
		cout<<endl;
	}
}
