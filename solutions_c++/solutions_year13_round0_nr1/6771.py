
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
using namespace std;
int func(string s[],int con)
{ 
	int k1=0,k2=0,t1=0,t2=0;
	for(int i=0;i<4;i++)
	{
	if(s[i][i]=='X')
		k1++;
	else if(s[i][i]=='O')
		k1--;
	else if(s[i][i]=='T')
		t1=1;
	
		
	if(s[i][3-i]=='X')
		k2++;
	else if(s[i][3-i]=='O')
		k2--;
	else if(s[i][3-i]=='T')
		t2=1;
	
	}
	if(k2==4||(k2==3&&t2==1))
		return 1;
	if(k2==-4||(k2==-3&&t2==1))
		return -1;
	if(k1==4||(k1==3&&t1==1))
		return 1;
	if(k1==-4||(k1==-3&&t1==1))
	return -1;
for(int i=0;i<4;i++)
  {k1=0,k2=0,t1=0,t2=0;
		for(int j=0;j<4;j++)
	{
	if(s[i][j]=='X')
		k1++;
	else if(s[i][j]=='O')
		k1--;
	else if(s[i][j]=='T')
		t1=1;
	
	if(s[j][i]=='X')
		k2++;
	else if(s[j][i]=='O')
		k2--;
	else if(s[j][i]=='T')
		t2=1;
	
	
	}
if(k2==4||(k2==3&&t2==1))
		return 1;
	if(k2==-4||(k2==-3&&t2==1))
		return -1;
	if(k1==4||(k1==3&&t1==1))
		return 1;
	if(k1==-4||(k1==-3&&t1==1))
	return -1;
}

return con;

}

int main()
{ FILE*fout=fopen("output.txt","w"); 
FILE*fin=fopen("input.txt","r"); 	
int con,d;
	char l,ig[100];
	fscanf(fin,"%d ",&d);
	for(int k=0;k<d;k++)
	{string c[4];
	con=0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
		{
			fscanf(fin,"%c ",&l);
	
			if(l=='.')
		con=2;
		c[i]+=l;

		}
		
{	int x=func(c,con);		
	if(x== 1)
			fprintf(fout,"Case #%d: X won\n",k+1);
           else if(x== -1)
			fprintf(fout,"Case #%d: O won\n",k+1);
			else if(x== 0)
			fprintf(fout,"Case #%d: Draw\n",k+1);
           else if(x== 2)
			fprintf(fout,"Case #%d: Game has not completed\n",k+1);
		}	//gets(ig);
	}
return 0;
}