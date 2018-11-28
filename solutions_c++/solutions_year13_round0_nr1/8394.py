#include<stdio.h>
int main()
{
	FILE *f = freopen ("in.in","r",stdin);
	FILE *q = freopen ("out.out","w",stdout);
	int n,i,j,k;
	fscanf(f,"%d",&n);
	fgetchar();
	char a[4][4],t;
	bool flag;
	for(i=0;i<n;i++)
	{
		flag=true;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				fscanf(f,"%c",&a[j][k]);
			}
			fgetchar();
		}
		for(j=0;j<4&&flag;j++)
		{
			if(a[j][0]=='X'||a[j][0]=='O')
			{
				t=a[j][0];
			}
			else if(a[j][0]=='T'&&(a[j][1]=='X'||a[j][1]=='O'))
			{
				t=a[j][1];
			}
			for(k=1;k<4;k++)
			{
				if(a[j][k]!=t&&a[j][k]!='T')
					break;
			}
			if(k==4)
			{
				fprintf(q,"Case #%d: %c won\n",i+1,t);
				fgetchar();
				flag=false;
			}
		}
		for(j=0;j<4&&flag;j++)
		{
			if(a[0][j]=='X'||a[0][j]=='O')
			{
				t=a[0][j];
			}
			else if(a[0][j]=='T'&&(a[1][j]=='X'||a[1][j]=='O'))
			{
				t=a[1][j];
			}
			for(k=1;k<4;k++)
			{
				if(a[k][j]!=t&&a[k][j]!='T')
					break;
			}
			if(k==4)
			{
				fprintf(q,"Case #%d: %c won\n",i+1,t);
				fgetchar();
				flag=false;
			}
		}
		if(flag)
		{
			if(a[0][0]=='X'||a[0][0]=='O')
			{
				t=a[0][0];
			}
			else if(a[0][0]=='T'&&(a[1][1]=='X'||a[1][1]=='O'))
			{
				t=a[1][1];
			}
			for(k=1;k<4;k++)
			{
				if(a[k][k]!=t&&a[k][k]!='T')
					break;
			}
			if(k==4)
			{
				fprintf(q,"Case #%d: %c won\n",i+1,t);
				fgetchar();
				flag=false;
			}
		}
		if(flag)
		{
			if(a[0][3]=='X'||a[0][3]=='O')
			{
				t=a[0][3];
			}
			else if(a[0][3]=='T'&&(a[1][2]=='X'||a[1][2]=='O'))
			{
				t=a[1][2];
			}
			for(k=1;k<4;k++)
			{
				if(a[k][3-k]!=t&&a[k][3-k]!='T')
					break;
			}
			if(k==4)
			{
				fprintf(q,"Case #%d: %c won\n",i+1,t);
				fscanf(f,"\n");
				flag=false;
			}
		}
		if(flag)
		{
			for(j=0;j<4&&flag;j++)
			{
				for(k=0;k<4&&flag;k++)
				{
					if(a[j][k]=='.')
					{
						fprintf(q,"Case #%d: Game has not completed\n",i+1);
						fgetchar();
						flag=false;
					}
				}
			}
		}
		if(flag)
		{
			fprintf(q,"Case #%d: Draw\n",i+1);
			fgetchar();
		}
	}
	fclose(f);
	fclose(q);
	return 0;
}