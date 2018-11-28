#include<stdio.h>
#include<math.h>
#include<string.h>
#define abs(x) ((x)>0?(x):-(x))
#define MOD 1000000007
int main(){
	int t,i,k,j1,j2,a[1001],ans,f11,n;
    char s1[1001];
	FILE *f1,*f2;
	f1=fopen("a11.in","r");
	f2=fopen("a22.out","w");
	fscanf(f1,"%d\n",&t);
	for(i=0;i<t;i++){
		fscanf(f1,"%s",s1);
		fscanf(f1,"%d",&k);
		n = strlen(s1);
		fprintf(f2,"Case #%d: ",i+1);
		for(j1=0;j1<n;j1++){
			a[j1]=0;
		}
		f11=1;
		ans=0;
		for(j1=0;j1<n && f11;j1++){
			if((s1[j1] == '+' && a[j1]%2 == 1) || (s1[j1] == '-' && a[j1]%2 == 0)){
				if((j1+k-1) >= n){
						ans = -1;
						f11 = 0;
				}
				else{
						for(j2=j1;j2<(j1+k);j2++){
								a[j2] = a[j2]+1;
						}
						ans = ans + 1;
				}
			}
		}
		if(ans == -1){
			fprintf(f2,"IMPOSSIBLE\n");
		}
		else{
			fprintf(f2,"%d\n",ans);
		}
    }
	return 0;
}
