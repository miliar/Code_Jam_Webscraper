#include<stdio.h>
#include<stdlib.h>

int k, c, s;

bool data[101];
int64_t res[101];
int resCount=0;

int64_t follow(int64_t pos, int level) {
	if(level==c) return pos;
	return 0;
}

void simpleProcess() {
	for(int i=0;i<k;++i) {
		for(int j=0;j<k;++j) data[j]=false;
		data[i]=true;
		
		int64_t v=follow(i, 1);
		bool found=false;
		for(int j=0;j<resCount;++j) {
			if(res[j]==v) {
				found=true;
				break;
			}
		}
		if(!found) {
			res[resCount++]=v;
		}
	}
}



int main(int argc, char** argv) {
	int tsts;
	
	scanf("%d", &tsts);
	
	for(int t=1;t<=tsts;++t) {
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", t);
		if(k==s) {
			for(int i=1;i<=k;++i) printf(" %d", i);
		}
		
		printf("\n");
	}
	return 0;
}