#include<conio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,m,n,T,p;
	int r,t;
	scanf("%d",&T);
	for(p=1;p<=T;p++){
		printf("Case #%d: ",p);
		scanf("%d%d",&r,&t);
		int i=0;
		long long count=0;
		while(1){
			count+=r*2+1;
			i++;
			if(count>t){
				count-=r*(r*2+1);
				i--;
				break;
			}
			r+=2;
		}
		printf("%d\n",i);
	}
	getch();
	return 0;
}
