#include <cstdlib>
#include <iostream>
#include <string.h>

using namespace std;

char S[1001],r[1001];
int pos;
   	
void sort(char *S, int qnt) {
	int max,l;
	char c=0;
	
	for (l=0;l<qnt;l++) 
	  if (S[l]>=c) {
	  	c=S[l]; max=l;
	  }
	
	r[pos++]=S[max];
	if (max>0) sort(S,max);
	max++;
	qnt-=max;
	for(;qnt>0;qnt--,max++) r[pos++]=S[max];
}


int main(int argc, char** argv) {
	
   	int T;
   	int l;
	pos=0;


//	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-large.in","rt",stdin);
//	freopen("A-sample.in","rt",stdin);
	freopen("A.out","wt",stdout);	

	scanf("%d",&T);
	for (int l = 0; l < T; l++) {
		scanf("%s\n",S);
		pos=0; sort(S,strlen(S));
		r[pos]=0;
		printf("Case #%d: %s\n",l+1,r);
    }

    //system("PAUSE");
    return EXIT_SUCCESS;
}
