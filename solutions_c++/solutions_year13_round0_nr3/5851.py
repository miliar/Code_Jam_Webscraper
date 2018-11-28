#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int find(int x) {
	if(x>=484)
		return 5;
	else if(x>=121)
		return 4;
	else if (x>=9)
		return 3;
	else if (x>=4)
		return 2;
	else if (x>=1)
		return 1;
	return 0;
}

int main() {
	int T;
	FILE *in,*out;
	in = fopen("C.in","r");
	out = fopen("C.out","w");
	int a,b;
	int ac,bc;
	fscanf(in,"%d", &T);
	
	for(int t=1; t<=T; t++) {
		ac=bc=0;
		fscanf(in,"%d%d",&a,&b);
		
		ac=find(a-1);
		bc=find(b);
		
		fprintf(out, "Case #%d: %d\n",t,bc-ac);
	}
							
	return 0;			
}
