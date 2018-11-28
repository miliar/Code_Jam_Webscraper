#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#define INF 1<<30
using namespace std;
const int MAXN=1050;
double data[MAXN],datb[MAXN],kdat[MAXN];
int main(){
	int tcas,cas;
	while(~scanf("%d",&tcas)){
		for(cas=0;cas<tcas;cas++){
			int tot,resa=0,resb=0;
			scanf("%d",&tot);
			for(int i=0;i<tot;i++)scanf("%lf",&data[i]);
			for(int i=0;i<tot;i++){
				scanf("%lf",&datb[i]);
				kdat[i]=datb[i];
			}
			sort(data,data+tot);
			sort(datb,datb+tot);
		//	for(int i=0;i<tot;i++)printf("%f ",data[i]);putchar('\n');
		//	for(int i=0;i<tot;i++)printf("%f ",datb[i]);putchar('\n');
			for(int i=0;i<tot;i++){
				for(int j=tot-1;j>=0;j--){
					if(data[i]>datb[j]){
						resa++;
						datb[j]=INF;
						break;
					}
				} 
			}
			for(int i=0;i<tot;i++){
				for(int j=tot-1;j>=0;j--){
					if(kdat[i]>data[j]){
						resb++;
						data[j]=INF;
						break;
					}
				} 
			}
			printf("Case #%d: %d %d\n",cas+1,resa,tot-resb);
		}
	}
	return 0;
} 
/*
Input 
4
1
0.5
0.6
2
0.7 0.2
0.8 0.3
3
0.5 0.1 0.9
0.6 0.4 0.3
9
0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458

Output  
Case #1: 0 0
Case #2: 1 0
Case #3: 2 1
Case #4: 8 4
*/