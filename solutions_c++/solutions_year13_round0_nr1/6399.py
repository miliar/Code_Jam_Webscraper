#include<iostream>
#include<stdio.h>
using namespace std;
int crow(char c[4][4])
{
int i=0,f=0;
while(i<4)
 {
   if((c[i][0]=='X'||c[i][0]=='T')&&(c[i][1]=='X'||c[i][1]=='T')&&(c[i][2]=='X'||c[i][2]=='T')&&(c[i][3]=='X'||c[i][3]=='T'))
	{
		f=1;
		break;
	}
  else if((c[i][0]=='O'||c[i][0]=='T')&&(c[i][1]=='O'||c[i][1]=='T')&&(c[i][2]=='O'||c[i][2]=='T')&&(c[i][3]=='O'||c[i][3]=='T'))
	{
		f=2;
		break;
	}
 i++;
 }
return f;
}
int ccol(char c[4][4])
{
int i=0,f=0;
while(i<4)
 {
   if((c[0][i]=='X'||c[0][i]=='T')&&(c[1][i]=='X'||c[1][i]=='T')&&(c[2][i]=='X'||c[2][i]=='T')&&(c[3][i]=='X'||c[3][i]=='T'))
   	{
		f=1;
		break;
	}
  else if((c[0][i]=='O'||c[0][i]=='T')&&(c[1][i]=='O'||c[1][i]=='T')&&(c[2][i]=='O'||c[2][i]=='T')&&(c[3][i]=='O'||c[3][i]=='T'))
	{
		f=2;
		break;
	}
 i++;
 }
return f;
}
int cdia(char c[4][4])
{
   if((c[0][0]=='X'||c[0][0]=='T')&&(c[1][1]=='X'||c[1][1]=='T')&&(c[2][2]=='X'||c[2][2]=='T')&&(c[3][3]=='X'||c[3][3]=='T'))
	return 1;
else  if((c[0][3]=='X'||c[0][3]=='T')&&(c[1][2]=='X'||c[1][2]=='T')&&(c[2][1]=='X'||c[2][1]=='T')&&(c[3][0]=='X'||c[3][0]=='T'))
	return 1;
else  if((c[0][0]=='O'||c[0][0]=='T')&&(c[1][1]=='O'||c[1][1]=='T')&&(c[2][2]=='O'||c[2][2]=='T')&&(c[3][3]=='O'||c[3][3]=='T'))
	return 2;
else  if((c[0][3]=='O'||c[0][3]=='T')&&(c[1][2]=='O'||c[1][2]=='T')&&(c[2][1]=='O'||c[2][1]=='T')&&(c[3][0]=='O'||c[3][0]=='T'))
	return 2;
else
	return 0;
}
void print(int n)
{
  switch(n)
	{
		case 1:
			cout<<"X won";
			break;
		case 2:
			cout<<"O won";
			break;
		case 3:
			cout<<"Draw";
			break;
		case 4:
			cout<<"Game has not completed";
			break;
	 }
}
int check(char c[4][4])
{
  int p,q,f=3;
  for(p=0;p<4;p++)
    {
    	for(q=0;q<4;q++)
    	  {
    	     if(c[p][q]=='.')
    	        {
    	           f=4;
    	  	   break;
    	  	}
    	  }
    }
 return f;
 }
int main()
{
 char g[4][4];
 int n,fr,fc,fd,c[1001],i,p,q;
 cin>>n;
 for(i=1;i<=n;i++)
   {
   	p=0;
   	while(p<4)
   	 {
   	 	q=0;
   	 	while(q<4)
   	 	{
   	 		cin>>g[p][q];
   	 		q++;
   	 	}
   	 	p++;
   	 }
   	c[i]=check(g);
   	fr=crow(g);
   	fc=ccol(g);
   	fd=cdia(g);
   	if(fr==1||fd==1||fc==1)
   		c[i]=1;
	else if(fr==2||fc==2||fd==2)
		c[i]=2;
   }
 for(i=1;i<=n;i++)
  {
    cout<<"Case #"<<i<<": ";
    print(c[i]);
    cout<<"\n";
  }
return 0;
}
