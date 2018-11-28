#include <stdio.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <stdio.h>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <math.h>
#include <map>

#define MaxLength INT_MAX
#define MaxNode 12
#define MN 20

using namespace std;
unsigned int N,M,X,Y,T;

int mem[MN];


int main(){
	int i,j,k,tt,a,b,c,s,t,n,d,x,y,A,B,C;
	long long res,cur;
	scanf("%d",&T);
	
	for(tt=1; tt<=T; tt++){
		memset(mem,0,sizeof(mem));	
		scanf("%d",&A);
		A--;
		for(i=0; i<4; i++)
			for(j=0; j<4; j++){
				scanf("%d",&a);
				if(i == A)
					mem[a]++;
			}
		scanf("%d",&A);
		A--;
		for(i=0; i<4; i++){
			for(j=0; j<4; j++){
				scanf("%d",&a);
				if(i == A)
					mem[a]++;
			}
		}
		res = -1;
		for (i=1; i<=16; i++){
			if(mem[i] == 2 && res ==-1)
				res = i;
			else if(mem[i] == 2 && res != -1)
				res = -2;
		}
		if(res > 0)
			printf("Case #%d: %d\n",tt,res);
		else if(res == -2)
			printf("Case #%d: Bad magician!\n",tt);
		else
			printf("Case #%d: Volunteer cheated!\n",tt);
	}
	return 0;
}