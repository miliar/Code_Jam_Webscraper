#include <cstdio>
using namespace std;

long double c,x,f,s,s1,p;
int i,j,k,l,t;

int main(){
	scanf("%d", &t);
	for(i=0;i<t;i++){
		scanf("%Lf%Lf%Lf", &c, &f, &x);
		s=x/2;
		l=1;
		s1=c/2+x/(2+f);
		while(s1<s){
			s=s1;
			s1=0;
			l++;
			for(j=1;j<=l;j++){
				p=j;
				s1+=c/(2+(p-1)*f);
			}
			p=l;
			s1+=x/(2+p*f);
		}
		printf("Case #%d: %.7Lf\n", i+1,s);
	}
	return 0;
}
