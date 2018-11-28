#include <iostream>
#include <cstdio>
#include <stdlib.h>

using namespace std;

int main()
{
	FILE* f;
	FILE* p;
	f=fopen("A-large.in","r");
	p=fopen("out.txt","w");
	int t;
	int n,i,j,k,l=1;
	int x,a[10],c;
	fscanf(f,"%d",&t);
	while(l<=t)
	{
		fscanf(f,"%d",&n);
		if(n==0)
			fprintf(p,"Case #%d: INSOMNIA\n",l);
		else
		{
			for(j=0;j<10;j++)
				a[j]=0;
			k=0;
			i=1;
			while(k<10)
			{
				x=n*i;
				while(x>0)
				{
					c=x%10;
					if(a[c]==0)
					{
						a[c]=1;
						k++;
					}
					x=x/10;
				}
				i++;
			}
			//cout<<"case #"<<l<<": "<<(n*(i-1))<<endl;
			fprintf(p,"Case #%d: %d\n",l,(n*(i-1)));
			//cout<<n<<" "<<x<<" "<<i<<" "<<endl;
		}
		l++;
	}
	fclose(f);
	fclose(p);
}
