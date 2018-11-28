#include <iostream>
#include <cstdio>
using namespace std;

int T,a[20],k,x;

int main(){
	scanf("%d",&T);
	for (int tt=1; tt<=T; tt++){
		for (int i=1; i<=16; i++) a[i]=0;
		scanf("%d",&x);
		for (int i=1; i<=4; i++)
			for (int j=1;j<=4; j++){
				scanf("%d",&k);
				if (x==i) a[k]++;
			}
			
		scanf("%d",&x);
		for (int i=1; i<=4; i++)
			for (int j=1;j<=4; j++){
				scanf("%d",&k);
				if (x==i) a[k]++;
			}
		
		int cnt=0, maxv=0, here=0;
		for (int i=1; i<=16; i++){
			if (a[i]>=maxv){
				if (a[i]>maxv){
					maxv=a[i]; cnt=0; here=i;
				}
				cnt++;
			}
		}
		
		printf("Case #%d: ",tt);
		if (maxv==2 && cnt==1) printf("%d\n", here);
		else if (maxv==2 && cnt>1) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
}
