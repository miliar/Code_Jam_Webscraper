//============================================================================
// Name        : testGCJ1.cpp
// Author      : Takatera Toshiki
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdio>
using namespace std;
int kaisu,line,dust,t=0,ans;
int a[4],b[4];
int main(){
	scanf("%d",&kaisu);
	for(int i=1;i<=kaisu;i++){
		t=0;
		scanf("%d",&line);
		for(int j=1;j<5;j++){
			for(int k=0;k<4;k++){
				if(j==line){
					scanf("%d",&a[k]);
				}else{
					scanf("%d",&dust);
				}
			}
		}
		scanf("%d",&line);
		for(int j=1;j<5;j++){
			for(int k=0;k<4;k++){
				if(j==line){
					scanf("%d",&b[k]);
					for(int l=0;l<4;l++){
						if(b[k]==a[l]){t++;ans=a[l];}
					}
				}else{
					scanf("%d",&dust);
				}
			}
		}
		printf("\nCase #%d: ",i);
		if(t==1){printf("%d",ans);}
		else if(t==0){printf("Volunteer cheated!");}
		else{printf("Bad magician!");}

	}
	return 0;
}
