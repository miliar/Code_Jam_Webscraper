#include<iostream>
using namespace std;
int main()
{
	int t,x,r,c;
	FILE *fpr=fopen("input.txt","r");
	FILE *fpw=fopen("output.txt","w");
	fscanf(fpr,"%d",&t);
	for(int i=1;t-->0;i++)
	{
		fscanf(fpr,"%d %d %d",&x,&r,&c);
		int flag=0;
		if(x==1)
		{
			flag=0;
		}
		else if(x==2)
		{
			if((r==1 && c==1)||(r==1 && c==3)||(r==3 && c==1)||(r==3 && c==3))
			flag=1;
			else
			flag=0;
		}
		else if(x==3)
		{
			if((r==2 && c==3)||(r==3 && c==2)||(r==3 && c==3)||(r==3 && c==4)||(r==4 && c==3))
			flag=0;
			else
			flag=1;
		}
		else if(x==4)
		{
			if((r==3 && c==4)||(r==4 && c==4)||(r==4 && c==3))
			flag=0;
			else
			flag=1;
		}
		if(flag==0)
		fprintf(fpw,"Case #%d: GABRIEL\n",i);
		else
		fprintf(fpw,"Case #%d: RICHARD\n",i);
	}
	return 0;
}
