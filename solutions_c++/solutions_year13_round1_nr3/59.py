#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

set<int>x[626];
int T,r,n,m,k;
int w[10];

int main(){
	scanf("%d",&T);
	int h,i,j,l,a,b,c;
	for(h=1;h<=T;h++){
		scanf("%d%d%d%d",&r,&n,&m,&k);
		for(a=2;a<=5;a++)
			for(b=2;b<=5;b++)
				for(c=2;c<=5;c++){
					i=a*36+b*6+c;
					x[i].insert(a);
					x[i].insert(b);
					x[i].insert(c);
					x[i].insert(b*c);
					x[i].insert(a*b);
					x[i].insert(a*c);
					x[i].insert(a*b*c);
					x[i].insert(1);
				}
		printf("Case #%d:\n",h);
		for(i=0;i<r;i++){
			for(j=0;j<k;j++){
				scanf("%d",&w[j]);
			}
			for(j=0;j<220;j++){
				for(l=0;l<k;l++){
					if(x[j].find(w[l])==x[j].end())break;
				}
				if(l==k){
					printf("%d%d%d\n",j/36,(j%36)/6,j%6);
					break;
				}
			}
		}
	}
	return 0;
}
