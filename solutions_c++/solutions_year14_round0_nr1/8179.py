#include <iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

int main() {
int t,m,i,j,n,v;
int c[100];
int a[100][100];
int b[100][100];
scanf("%d",&t);
int s=1;
while(t--){
int count=0;
	scanf("%d",&m);
	
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			

scanf("%d",&a[i][j]);
			
		}
	}
	

scanf("%d",&n);
	for(i=0;i<4;i++){
		

for(j=0;j<4;j++){
			

scanf("%d",&b[i][j]);

		}
	

}

v=0;

for(i=0;i<4;i++){
for(j=0;j<4;j++){ 
		

		if(a[m-1][i]==b[n-1][j]){
		
			

count++;
			c[v]=a[m-1][i];
v++;			
		

	}
			
	

	}
	}
	
	

if(count==1){
	printf("Case #%d: %d\n",s,c[0]);
	}
	else if(count>1){
	printf("Case #%d: Bad magician!\n",s);
	}
	else{
	

printf("Case #%d: Volunteer cheated!\n",s);
	

}
	s++;
	}
	}