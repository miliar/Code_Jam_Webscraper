#include<cstdio>

int T,a,b,x;

bool liczby[20];
int ilosc,res;

int main(){
	scanf("%d",&T);
	
	for(int q=0;q<T;q++){
		scanf("%d",&a);
		a--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&x);
				if(i == a)liczby[x] = 1;
			}
		}
		
		scanf("%d",&b);
		b--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&x);
				if(i == b){
					if(liczby[x] == 1){
						ilosc++;
						res = x;	
					}
				}
			}
		}
		printf("Case #%d: ",q+1);
		if(ilosc == 0)printf("Volunteer cheated!\n");
		else if(ilosc > 1)printf("Bad magician!\n");
		else printf("%d\n",res);
		
		res = 0;
		ilosc = 0;
		for(int i=1;i<=16;i++)liczby[i] = 0;
	}


return 0;
}
