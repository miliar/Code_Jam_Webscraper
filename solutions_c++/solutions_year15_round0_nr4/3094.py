#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
#include <queue>
#include <vector>
#include <math.h>

using namespace std;

bool Func(int x,int r,int c){
	//true GABRIEL
	if(x==1)
		return true;

	if((r*c)%x!=0)
		return false;

	if(x==4 && r+c==6)
		return false;


	if(x>r && x>c)
		return false;
	if(x>2 && (r==1||c==1))
		return false;

}

int main(){
	int tc;
	scanf("%d",&tc);

	FILE *f;

	f=fopen("a.txt","w");
	for(int a=0;a<tc;a++){
				int x,r,c;

		scanf("%d %d %d",&x,&r,&c);


		if(Func(x,r,c)){
			fprintf(f,"Case #%d: GABRIEL\n",a+1);
			//printf("Case #%d: GABRIEL\n",a+1);

		}
		else{
			fprintf(f,"Case #%d: RICHARD\n",a+1);
			//printf("Case #%d: RICHARD\n",a+1);

		}
	}
	fclose(f);
}