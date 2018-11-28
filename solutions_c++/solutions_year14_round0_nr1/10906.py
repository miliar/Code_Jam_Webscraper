#include<cstdio>
bool t[20];
int te, a, x1, x2, x3, x4;
int main(){
	scanf("%d", &te);
	for (int x=1; x<=te; x++){
		for (int pom=1; pom<=16; pom++) t[pom]=false;
			scanf("%d", &a);
			for(int pom=1; pom<5; pom++){
				scanf("%d %d %d %d", &x1, &x2, &x3, &x4);
				if(pom == a){
					for (int i=1; i<=16; i++)
						if(i==x1 || i==x2 || i==x3 || i==x4) t[i]=true;
				}
			}
			scanf("%d", &a);
			for(int pom=1; pom<5; pom++){
				scanf("%d %d %d %d", &x1, &x2, &x3, &x4);
				if(pom == a){
					for (int i=1; i<=16; i++)
						if(t[i] && i!=x1 && i!=x2 && i!=x3 && i!=x4) t[i]=false; 
				}
			}
		printf("Case #%d: ", x);
		int pom = -1;
		for(int i=1; i<17; i++){
			if(t[i]){
				if(pom == -1) pom = i;
				else
				if(pom > 0) pom = -2;
			}
		}
		if (pom == -1) printf("Volunteer cheated!\n");
	      	if (pom == -2) printf("Bad magician!\n");
		if (pom > 0) printf("%d\n", pom);	
	}
}
	
