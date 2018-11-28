#include <iostream>
using namespace std;
#define MAX 1000000

int main()
{
	FILE *in,*out;
	in=fopen("A.in","r");
	out=fopen("A.out","w");

	int n, T,nval,chn,con;
	bool name[MAX]={0};
	char c;
	fscanf(in,"%d",&T);
	for(int t=0;t<T;t++)
	{
		chn=0;
		nval=0;
		c=0;
		for(int i=0;i<MAX;i++)
		name[i]=0;
		while(c!=' ')
		{

			fscanf(in,"%c",&c);
			if(c=='a'|| c=='e' || c=='i' || c=='u' || c=='o') name[chn]=1;
			if(c==' ')break;
			if(c!=' ' && c!='\n') chn++;
		}
		con=0;
		fscanf(in,"%d",&n);
		for(int i=0;i<chn;i++)
		{
			con=0;
			for(int j=i;j<chn;j++)
			{
				if(!name[j])con++;
				if(name[j] && con<n)con=0;
				if(con>=n) nval++;
			}

		}

		fprintf(out,"Case #%d: %d\n",t+1,nval);
	}



	return 0;
}