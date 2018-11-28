#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define f(a,b,c)                for(int a=b;a<c;a++)
#define s(x)                    scanf("%d",&x);
int main(){
	int t;
	s(t);
	int a[10000];
	f(i1,1,t+1){
		int x,r,c;
		s(x);
		s(r);
		s(c);
		int pro = r*c;
		if(pro%x){
			printf("Case #%d: %s\n",i1,"RICHARD");
		}
		else{
			int minc = min(r,c);
			if(x==3){
				if(minc == 1)
					printf("Case #%d: %s\n",i1,"RICHARD");
				else 
					printf("Case #%d: %s\n",i1,"GABRIEL");
			}
			else if(x==4){
				if(minc == 1 || minc == 2)
				    printf("Case #%d: %s\n",i1,"RICHARD");
				else 
					printf("Case #%d: %s\n",i1,"GABRIEL");
			}
			else 
				printf("Case #%d: %s\n",i1,"GABRIEL");
		}
		
	}
}