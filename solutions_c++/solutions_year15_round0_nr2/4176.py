#include <iostream>
#include <stdio.h>

using namespace std;
  
int main(){
	int  t, y[1200], x=1, n, maximo, minimo, temp;
	scanf("%d",&t);
	while(t--){
		cin>>n;
		int j=0;
		while(j<n){
			cin>>y[j];
			maximo = max(maximo,y[j]);
			j++;
		}
		minimo = maximo;
		for(int i=1;i<=maximo;i++){
			temp=i;
			for(int j=0;j<n;j++){
				if(y[j]>i){
					if( y[j]%i == 0){
						temp+=(y[j]/i-1);
					}
					else{
						temp+=(y[j]/i);
					}
				}
			}
			minimo =min(minimo,temp);
		}
		printf("Case #%d: %d\n",x,minimo);
		x++;
	}
return 	0;
}