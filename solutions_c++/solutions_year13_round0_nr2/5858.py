#include <iostream>
#include <cstdio>

using namespace std;

int main( )
{
	int T,t;
	int n,m;
	int x[110][110];
	bool res;
	
	scanf("%d",&T);
	
	for(int t=1;t<=T;t++){
		scanf("%d%d",&n,&m);
		
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				scanf("%d",&x[i][j]);
			}
		}
		
		res = true;
		
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				
				// check horizontally
				bool tRes = true;
				for(int k=0;k<m;k++){
					if(x[i][k]>x[i][j]){
						tRes = false;
					}
				}
				
				if( !tRes ){
					tRes = true;
								
					// check vertically
					for(int k=0;k<n;k++){
						if(x[k][j]>x[i][j]){
							tRes = false;
						}
					}
				}
				
				res = tRes;
				
				if(!res){
					break;
				}
			}
			
			if(!res){
				break;
			}
		}
		
		if(res){
			printf("Case #%d: YES\n",t);
		} else {
			printf("Case #%d: NO\n",t);
		}
	}
	
	return 0;
}
