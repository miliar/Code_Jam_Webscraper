
#include<fstream.h>
#include<conio.h>
#include<iomanip.h>

long c=1,n1,n2;
ofstream fout("ab.txt");
int checkrow(char a,char c[4][4])
{
    int flag1=0,j=0;
    for(int i=0;i<4;i++)
    {
	int flag;
	if(i<3)
	j=0;
	int count=0;
	do
	{
		flag=0;
		if(c[i][j]==a)
		{
			flag=1;
		}
		if(c[i][j]!=a)
		{
		if(count==0)
		{
			if(c[i][j]=='T')
			{
				flag=1;
				count=1;
			}
			else
			{
				flag1=0;
				break;
			}
		}
		}
		if(j==3 && flag==1)
		{
			flag1=1;
			break;

		}
		j++;
	}while(flag1!=1 && j<4);
	if(flag1==1)
	break;
    }
    return flag1;
}

int checkcolum(char a,char c[4][4])
{
    int flag1=0,j=0;
    for(int i=0;i<4;i++)
    {
	int flag;
	if(i<3)
	j=0;
	int count=0;
	do
	{
		flag=0;
		if(c[j][i]==a)
		{

			flag=1;
		}
		if(c[j][i]!=a)
		{
		if(count==0 || count==1)
		{
			if(c[j][i]=='T' && count==0)
			{
				flag=1;
				count=1;
			}
			else
			{
				flag1=0;
				break;
			}
		}
		}
		if(j==3 && flag==1)
		{
			flag1=1;
			break;

		}
		j++;
	}while(flag1!=1 && j<4);
	if(flag1==1)
	break;
    }
    return flag1;
}
int checkdia(char a,char c[4][4])
{
    if((c[0][0]==c[1][1]==c[2][2]==c[3][3]==a)||(c[0][3]==c[1][2]==c[2][1]==c[3][0]==a))
	return 1;
    else
	return 0;

}


void main()
{
 clrscr();
 int flag,i,j,k=1,flag1=0,flag2=0,flag3=0,p=0,l,w;
 char a[4][4]={'.'},ch;
 ifstream fin("a.txt");
 fin>>n1;
 while(k<=n1)
 {
  for(i=0;i<4;i++)
  {
   for(j=0;j<4;j++)
   {
    fin>>ch;
    a[i][j]=ch;
   }
  }
  flag=checkrow('X',a);

  flag1=checkcolum('X',a);

  flag2=checkdia('X',a);
  if(flag==1 || flag1==1 || flag2==1)
  {
	 fout<<"Case #"<<k<<": X won";
	 flag3=1;
  }
  else
  {

	flag=checkrow('O',a);
	flag1=checkcolum('O',a);
	flag2=checkdia('O',a);
	if(flag==1 || flag1==1 || flag2==1)
	{
		 fout<<"Case #"<<k<<": O won";
		 flag3=1;


	}
	else
	{
		p=0;
		for(w=0;w<4;w++)
		{
			for(l=0;l<4;l++)
			{
				if(a[w][l]=='.')
				p=1;
				break;
			}
		}
		if(p==1)
		fout<<"Case #"<<k<<": Game has not compeleted";
		else
		fout<<"Case #"<<k<<": Draw";
	}

}
k++;
}
}
