#include<stdio.h>
int main()
{
	FILE *infile,*outfile;
	infile = fopen("A-large.in", "r");
	outfile = fopen("ans2.out", "w");
	char arr[4][4],ch;
	int t,i,j,xr,or,x[4],o[4],xd1,xd2,od1,od2,flag,k=1,flag2;
	fscanf(infile,"%d",&t);
	fscanf(infile,"%c",&ch);
	while(k<=t)
	{
		j=0;
		xr=0;
		or=0;
		xd1=xd2=0;
		od1=od2=0;
		flag=flag2=0;
		for(i=0;i<4;i++)
		{
			x[i]=0;
			o[i]=0;
		}
		while(j<4)
		{
			xr=or=0;
			for(i=0;i<=4;i++)
			{
				
				fscanf(infile,"%c",&ch);
				
				switch(ch)
				{
				case 'X':
					xr++;
					x[i]++;
					if(i==j)
					xd1++;
					if((3-i)==j)
					xd2++;
					break;
				case 'O':
					or++;
					o[i]++;
					if(i==j)
					od1++;
					if((3-i)==j)
					od2++;
					break;
				case 'T':
					xr++;
					or++;
					x[i]++;
					o[i]++;
					if(i==j)
					{
						od1++;
						xd1++;
					}
					if((3-i)==j)
					{
						od2++;
						xd2++;
					}
					break;
				case '.':
					flag2=1;
					break;
				default:
					j++;
					break;
				}
				
			}

		
		if(xr==4||xd1==4||xd2==4)
				flag=1;
		else if(or==4||od1==4||od2==4)
				flag=2;
		else
		{
		for(i=0;i<4;i++)
			{
				
				if(x[i]==4)
					flag=1;
				if(o[i]==4)
					flag=2;
			}
		}
		}
		switch(flag)
		{
		case 0:
			if(flag2)
			fprintf(outfile,"Case #%d: Game has not completed\n",k);
			else
			fprintf(outfile,"Case #%d: Draw\n",k);
			break;
		case 1:
			fprintf(outfile,"Case #%d: X won\n",k);
			break;
		case 2:
			fprintf(outfile,"Case #%d: O won\n",k);
			break;
		}
		fscanf(infile,"%c",&ch);
		
		k++;
	}

   return 0;
}
