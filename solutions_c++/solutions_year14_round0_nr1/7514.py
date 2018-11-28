#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
	FILE *f,*fout;
	f = fopen("ina.txt","r");
	fout = fopen("outa.txt","w+");
	char c[1024];
	int n;
	fscanf(f,"%d",&n);
	for(int i=0;i<n;++i)
	{
		int a,b[17],d;
		memset(b,0,sizeof(b));
		fscanf(f,"%d",&a);
		for(int j=0;j<4;++j)
		{
			for(int jy=0;jy<4;++jy)
			{
				fscanf(f,"%d",&d);
				if(j+1==a)
				{
					b[d] ++;
				}
			}
		}
		fscanf(f,"%d",&a);
		int cnt2=0,rec2;
		for(int j=0;j<4;++j)
		{
			for(int jy=0;jy<4;++jy)
			{
				fscanf(f,"%d",&d);
				if(j+1==a)
				{
					b[d] ++;
					if(b[d]==2)
					{
						++cnt2;
						rec2 = d;
					}
				}
			}
		}
		if(cnt2==0)
		{
			fprintf(fout,"Case #%d: Volunteer cheated!\n",i+1);
		}
		else if(cnt2==1)
		{
			fprintf(fout,"Case #%d: %d\n",i+1,rec2);
		}
		else
		{
			fprintf(fout,"Case #%d: Bad magician!\n",i+1);
		}
	}
	fclose(f);
	return 1;
}