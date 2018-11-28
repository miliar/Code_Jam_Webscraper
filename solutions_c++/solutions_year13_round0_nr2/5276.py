#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int n,m;
char lawni[110][110];

int comprobar(int h,int v){
	
	int res=1;
	
	for(int i=0;i<n;i++){
		if(lawni[i][v]>lawni[h][v]){
			res=0;
			break;
			
		}
	}
	
	if(res){
		return 1;
	}
	
	for(int i=0;i<m;i++){
		if(lawni[h][i]>lawni[h][v]){
			return 0;
		}
	}
	
	
	
	
	return 1;
}












int main(int argc,char**argv){
	
	freopen("lawnmover.txt","r",stdin);
	
	if(argc>1){
		freopen(argv[1],"r",stdin);
	
	
		char auxchar[200]={0};
		strcat(auxchar,argv[1]);
		strcat(auxchar,".out.txt");
	
		freopen(auxchar,"w",stdout);
	}
	
	
	
	int cant;
	scanf("%d",&cant);
	
	for(int no=0;no<cant;no++){
		
		memset(lawni,0,sizeof(char)*110*110);
		
		
		
		scanf("%d %d",&n,&m);
		
		for(int i=0;i<n;i++){
			int j=0;
			for(;j<m-1;j++){
				scanf("%d ",&(lawni[i][j]));
			}
			scanf("%d\n",&(lawni[i][j]));
		}
		
		
		
		int res=1;
		for(int ch=0;ch<n;ch++){
			for(int cv=0;cv<m;cv++){
				if(!res){break;}
				res=comprobar(ch,cv);
			}
		}
		
		printf("Case #%d: %s\n",no+1,res?"YES":"NO");
			
		
		
		
		
		
		
//		for(int i=0;i<n;i++){
//			for(int j=0;j<m;j++){
//				printf("%d ",lawni[i][j]);
//			}
//			printf("\n");
//		}
		
		
		
	}
	
	
	
	
	
	
	
	
	
}
