#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#define abs(x) ((x)>0?(x):-(x))
#define MOD 1000000007
int main(){
	int n,t,i,j,k,m,l,t1,t2,a[10],s,f23;
    char src[100][3],dest[100][3],c1,c2;
	FILE *f1,*f2;
	f1=fopen("a11.in","r");
	f2=fopen("a22.out","w");
	fscanf(f1,"%d",&t);
	for(i=0;i<t;i++){
		fscanf(f1,"%d",&n);
		for(j=0;j<10;j++){
			a[j]=0;
		}
		l=0;
		s=n;
		fprintf(f2,"Case #%d: ",i+1);
		if(n==0){
			fprintf(f2,"INSOMNIA\n");
		}
		else{
			while(l<10){
				m=n;
				while(m>0){
					if(a[m%10] == 0){
						a[m%10]++;
						l++;
					}
					m=m/10;
				}
				n+=s;
			}
			n-=s;
			fprintf(f2,"%d\n",n);
		}		
    }
	return 0;
}
