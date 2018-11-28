#include<stdio.h>
#include<string.h>


int main()
{
	int i,j,k,t,n;
	
	
	
	scanf("%d",&n);
	char s[4][5],temp;
	for(k=1;k<=n;k++)
	{
		j=0,t=0;
		for(i=0;i<4;i++)
		{
			scanf("%s",s[i]);
			s[i][4]='\0';
		}
		for(i=0;i<4;i++)
		if(strcmp(s[i],"XXXX")==0||strcmp(s[i],"XXXT")==0||strcmp(s[i],"XXTX")==0||strcmp(s[i],"XTXX")==0||strcmp(s[i],"TXXX")==0)
		{
			t=1;
			break;
		} 
		else if(strcmp(s[i],"OOOO")==0||strcmp(s[i],"OOOT")==0||strcmp(s[i],"OOTO")==0||strcmp(s[i],"OTOO")==0||strcmp(s[i],"TOOO")==0)
		{
			t=2;
			break;
		}
		char p[5],q[5],r[5],m[5];
		p[0]=s[0][3],p[1]=s[1][2],p[2]=s[2][1],p[3]=s[3][0],p[4]='\0';
		while(t==0&&j<2)
		{
			if(strcmp(p,"XXXX")==0||strcmp(p,"XXXT")==0||strcmp(p,"XXTX")==0||strcmp(p,"XTXX")==0||strcmp(p,"TXXX")==0)
			{
				t=1;
				break;
			} 
			else if(strcmp(p,"OOOO")==0||strcmp(p,"OOOT")==0||strcmp(p,"OOTO")==0||strcmp(p,"OTOO")==0||strcmp(p,"TOOO")==0)
			{
				t=2;
				break;
			}
			j++;
			if(t==0)
			p[0]=s[0][0],p[1]=s[1][1],p[2]=s[2][2],p[3]=s[3][3],p[4]='\0';			
		}
		if(t==0)
		{
			for(i=0;i<4;i++)
			p[i]=s[i][0];p[4]='\0';
			for(i=0;i<4;i++)
			q[i]=s[i][1];q[4]='\0';
			for(i=0;i<4;i++)
			r[i]=s[i][2];r[4]='\0';
			for(i=0;i<4;i++)
			m[i]=s[i][3];m[4]='\0';
				strcpy(s[0],p);
					strcpy(s[1],q);
						strcpy(s[2],r);
							strcpy(s[3],m);

			for(i=0;i<4;i++)
			if(strcmp(s[i],"XXXX")==0||strcmp(s[i],"XXXT")==0||strcmp(s[i],"XXTX")==0||strcmp(s[i],"XTXX")==0||strcmp(s[i],"TXXX")==0)
			{
				t=1;
				break;
			} 
			else if(strcmp(s[i],"OOOO")==0||strcmp(s[i],"OOOT")==0||strcmp(s[i],"OOTO")==0||strcmp(s[i],"OTOO")==0||strcmp(s[i],"TOOO")==0)
			{
				t=2;
				break;
			}
		}
		if(t==1)
		{
			printf("Case #%d: X won\n",k);
		}
		
		else if(t==2)
		{
			printf("Case #%d: O won\n",k);
		}
		
		else if(t==0)
		{
			for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				if(s[i][j]=='.')
				t=3;
				break;
			}
		}
		
		if(t==0)
		printf("Case #%d: Draw\n",k);
		
		else if(t==3)
		printf("Case #%d: Game has not completed\n",k);
		
	}
	
	return 0;
}
