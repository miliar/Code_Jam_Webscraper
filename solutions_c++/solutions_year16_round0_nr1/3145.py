#include<bits/stdc++.h>
using namespace std;
#define bit (1<<10)-1

int main(){
	freopen ("myfile.txt","w",stdout);
  
	int t,n,i,cal,j,sem;
	scanf("%d",&t);
	for(i=0;i<t;i++){
		scanf("%d",&n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",i+1);
		}
		else{
			cal=0;
			for(j=1;cal<bit;j++){
				sem=n*j;
				while(sem>0){
					cal=cal|(1<<(sem%10));
					sem/=10;
				}
			}
			printf("Case #%d: %d\n",i+1,(j-1)*n);
		}
		
	}
	fclose (stdout);
}
