#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
void main()
{   int n,k;
	FILE *fl1,*fl2;
	fl1=fopen("C:\\input.txt","r");
	fl2=fopen("output.txt","w");
	fscanf(fl1,"%d",&n);
	k=n;
	while (k>0)
	{   
		char a[5][5];
		fgetc(fl1);
		for(int i=0;i<4;i++)
		{ for(int j=0;j<4;j++)
			fscanf(fl1,"%c",&a[i][j]);
		    fgetc(fl1);
		}
                int b[4][4];
		for( int i=0;i<4;i++)
		for( int j=0;j<4;j++)
		{   
			if(a[i][j]=='T') b[i][j]=5;
			else if(a[i][j]=='X') b[i][j]=1;
			else if(a[i][j]=='O') b[i][j]=0;
			else b[i][j]=-100;
		}
		int c[10];
			for(int i=0;i<4;i++)
			{	
				c[i]=b[i][0]+b[i][1]+b[i][2]+b[i][3];
				c[i+4]=b[0][i]+b[1][i]+b[2][i]+b[3][i];
			}
                        c[8]=b[0][0]+b[1][1]+b[2][2]+b[3][3];
			c[9]=b[0][3]+b[1][2]+b[2][1]+b[3][0];
			int l=0,m=0,s=0;
			for(int i=0;i<10;i++)
				cout<<"c["<<i<<"]="<<c[i]<<endl;
			for(int i=0;i<10;i++)
			{
				if(c[i]==8||c[i]==4)
				     m=1; 
				else if(c[i]==0||c[i]==5)
					 s=1;
				else if(c[i]<-20) l=1;
			}
			if(m==1)                    fprintf(fl2,"Case #%d: X won\n",n-k+1);
			if(s==1)                    fprintf(fl2,"Case #%d: O won\n",n-k+1);
			if((m==0)&(s==0)&(l==0)) 	fprintf(fl2,"Case #%d: Draw\n",n-k+1);
			if((m==0)&(s==0)&(l==1))    fprintf(fl2,"Case #%d: Game has not completed\n",n-k+1);
		k--;cout<<k<<endl;
	}
    exit(0);
}

