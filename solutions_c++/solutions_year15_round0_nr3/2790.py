

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int tableop[4][4] = {{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
char text[10000];
int value[10000];
int x, l;
bool ok;

int op(int x, int y) {
	int signX = x/abs(x);
	int signY = y/abs(y);
	
	return signX*signY*tableop[abs(x)-1][abs(y)-1];
}

bool possible(int target, int s, int steps) {
	int var = 1;
	//printf("Start possible %d %d %d\n",target,s,steps);
	//for (int i=0;i<steps;i++){
	//	var = op(var,text[(s+i)%x]-'i'+2);
		//printf("--In possible - %d %c %d - sol %d\n",
		//(s+i)%x,text[(s+i)%x],text[(s+i)%x]-'i'+2,var);	
	//}
	//if (var==target)
	//printf("Return true\n");
	
	//if ((s+steps-1)<x) {
	
	//printf("-%d %d %d\n",target,s,steps);
	if (s==0) var = value[steps-1]; else 
	{
		//printf("in\n");
		var = -op(value[s-1],value[s+steps-1]);
		if (abs(value[s-1])==1) var=-var;
		//printf("out\n");
	}
	/*
	} else {
		if (s==0) var1 = value[x-1]; else {
			var1 = -op(value[s-1],value[x-1]);
			if (abs(value[s-1])==1) var=-var;
		}
		var2 = 1;
		for (int i=0;i<(steps-(x-s))/x; i++) {
			var2=op(var2,value[x-1]);
		}
		var3 = value[(steps-(x-s))%x -1];
		
		var = op(var1,var2);
		var = op(var,var3);
	}*/
	
	if (var==target) return true; else return false;
}

int main(int argc, char **argv)
{
	FILE* f;
	FILE* g;
	int tests;
	int cnt;
	
	f = fopen("input.txt","r");
	g = fopen("output.txt","w");
	
	fscanf(f,"%d",&tests);
	for (int tt=1;tt<=tests;tt++) {
		fscanf(f,"%d%d",&x,&l);
		fscanf(f,"%s",text);
		
		//printf("test %d\n",tt);
		value[0]=text[0]-'i'+2;
		for (int i=1;i<x*l;i++) {
			value[i] = op(value[i-1],text[i%x]-'i'+2); 
			//printf("%c ",text[i%x]);
			//printf("calc %d %d\n",i,value[i]);
		}
		
		//printf("In test %d - %d %d %s\n",tt,l,x,text);
		cnt = 0;
		if (strstr(text,"i")==NULL) cnt++;
		if (strstr(text,"j")==NULL) cnt++;
		if (strstr(text,"k")==NULL) cnt++;
		
		ok = false;
		if (cnt<=1) {
		for (int i=1;i<=x*l;i++) {
			if (possible(2,0,i)) {
				for (int j=1; j<=x*l-i; j++) {
					if (possible(3,i%x,j)) {
						if (possible(4,(j+i)%x,x*l-i-j)) {
							fprintf(g,"Case #%d: YES\n",tt);
							ok = true;
						}
					}
					if (ok) break;
				}
			}
			if (ok) break;
		}
		}
		
		if (!ok) fprintf(g,"Case #%d: NO\n",tt);
		//printf("Case #%d: NO\n",tt);
							
	}
	return 0;
}

