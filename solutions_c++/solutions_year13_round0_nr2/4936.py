#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

int main()
{
	int numCases, r, c;
	FILE * file;
	file=fopen("qrbs.out", "w");
	scanf("%d", &numCases);
	for (int k=0; k<numCases; k++){
		scanf("%d%d", &r, &c);		
		int **map=(int**)malloc(r*sizeof(int*));	
		int **mapFlag=(int**)malloc(r*sizeof(int*));
		for (int i=0; i<r; i++){
			map[i]=(int*)malloc(c*sizeof(int));	
			mapFlag[i]=(int*)malloc(c*sizeof(int));	
			for (int j=0; j<c; j++){				
				scanf("%d", &map[i][j]);								
				mapFlag[i][j]=0;								
			}
		}
				
		int comp=0, flagX=0, flagY=0;
		for (int x=0; x<r; x++){
			for (int y=0; y<c; y++){				
				comp=map[x][y];
				flagX=0, flagY=0;
				for (int i=0; i<r; i++){
					if (map[i][y]>comp){						
						flagX=1;
						break;
					}
				}
				if (flagX){
					for (int j=0; j<c; j++){
						if (map[x][j]>comp){							
							//printf("Case #%d: NO\n", k+1);
							fprintf(file, "Case #%d: NO\n", k+1);
							flagY=1;
							break;
						}
					}
				}
				if (flagY)
					break;
			}
			if (flagY){
				break;	
			}
		}
		
		if (!flagY)
			//printf("Case #%d: Yes\n", k+1);					
			fprintf(file, "Case #%d: YES\n", k+1);
		
		for (int z=0; z<r; z++){
			free(map[z]);		
			free(mapFlag[z]);
		}
		free(map);
		free(mapFlag);		
	}
		
	
	return 0;
}

