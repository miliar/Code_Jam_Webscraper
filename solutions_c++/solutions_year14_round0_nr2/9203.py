#include <cstdlib>
#include <cstdio>
#include <vector>

using namespace std;
int T;
//float c,f,x;
float C,F,X;
float cons=100000.0;

int main()
{
	FILE *fin=freopen("B-large.in","r",stdin);
	FILE *fout=freopen("b2.out","w",stdout);
	scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%f%f%f",&C,&F,&X);
		int n=1;
		C*=100000;F*=100000;X*=100000;
		double ans=X/200000.0;
		for(;;)
		{
			double next=ans-(X/(200000.0+(n-1)*F))+(C/(200000.0+(n-1)*F))+(X/(200000.0+n*F));
			if(next>ans) break;
			else {ans=next;n++;}
		}
		printf("Case #%d: %.7f\n",kase,ans);
	}
	return 0;
}