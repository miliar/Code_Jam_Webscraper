#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
#include <cmath>
#include <vector>
#include <queue>
#include <string.h>
#include <time.h>
//#include <unistd.h>
using namespace std;


char line[10000];
	

int main(int argc,char*argv[]) {
	int T,Smax;
	scanf("%d\n",&T);
	
	for (int iter=1;iter<=T;iter++) {
		scanf("%d %s\n",&Smax,line);
	
		
		int stand=0;
		int count=0;
		
		int len=strlen(line);
		for (int j=0;j<len;j++) {
			int value=line[j]-'0';
			
			if (value>0) {
				if (stand<j) {
					count+=j-stand;
					stand=j;
				}
				stand+=value;
			}
		}
		
		
		printf("Case #%d: %d\n",iter,count);
		//printf("***%d %s %d\n",Smax,line,len);
	}
	
	return 0;

}