#include<iostream>
using namespace std;

int checkx(char a[][5])
{
 for(int i=0;i<4;i++)
 {
  for(int j=0;j<4;j++)
  {
   if(a[i][j]=='X'||a[i][j]=='T')
   {
    for(int m=j+1;m<4;m++)
	{
	 if(a[i][m]=='X'||a[i][m]=='T')
	 {
	  if(m==3&&(a[i][0]=='X'||a[i][0]=='T')&&(a[i][1]=='X'||a[i][1]=='T')&&(a[i][2]=='X'||a[i][2]=='T')&&(a[i][3]=='X'||a[i][3]=='T'))
	  {
	   return 1;
	  }
	 }
	}
	for(int n=i+1;n<4;n++)
	{
	 if(a[n][j]=='X'||a[n][j]=='T')
	 {
	  if(n==3&&(a[0][j]=='X'||a[0][j]=='T')&&(a[1][j]=='X'||a[1][j]=='T')&&(a[2][j]=='X'||a[2][j]=='T')&&(a[3][j]=='X'||a[3][j]=='T'))
	  {
	   return 1;
	  }
	 }
	}
	for(int x=i+1,y=j+1;x<4&&y<4;x++,y++)
	{
	 if(a[x][y]=='X'||a[x][y]=='T')
	 {
	  if(x==3&&y==3&&(a[0][0]=='X'||a[0][0]=='T')&&(a[1][1]=='X'||a[1][1]=='T')&&(a[2][2]=='X'||a[2][2]=='T')&&(a[3][3]=='X'||a[3][3]=='T'))
	  {
	   return 1;
	  }
	 }
	}
	for(int x=i+1,y=j-1;x<4&&y>=0;x++,y--)
	{
	 if(a[x][y]=='X'||a[x][y]=='T')
	 {
	  if(x==3&&y==0&&(a[0][3]=='X'||a[0][3]=='T')&&(a[1][2]=='X'||a[1][2]=='T')&&(a[2][1]=='X'||a[2][1]=='T')&&(a[3][0]=='X'||a[3][0]=='T'))
	  {
	   return 1;
	  }
	 }
	}
   }
  }
 }
 return 0;
}


int checky(char a[][5])
{
 for(int i=0;i<4;i++)
 {
  for(int j=0;j<4;j++)
  {
   if(a[i][j]=='O'||a[i][j]=='T')
   {
    for(int m=j+1;m<4;m++)
	{
	 if(a[i][m]=='O'||a[i][m]=='T')
	 {
	  if(m==3&&(a[i][0]=='O'||a[i][0]=='T')&&(a[i][1]=='O'||a[i][1]=='T')&&(a[i][2]=='O'||a[i][2]=='T')&&(a[i][3]=='O'||a[i][3]=='T'))
	  {
	   return 1;
	  }
	 }
	}
	for(int n=i+1;n<4;n++)
	{
	 if(a[n][j]=='O'||a[n][j]=='T')
	 {
	  if(n==3&&(a[0][j]=='O'||a[0][j]=='T')&&(a[1][j]=='O'||a[1][j]=='T')&&(a[2][j]=='O'||a[2][j]=='T')&&(a[3][j]=='O'||a[3][j]=='T'))
	  {
	   return 1;
	  }
	 }
	}
	for(int x=i+1,y=j+1;x<4&&y<4;x++,y++)
	{
	 if(a[x][y]=='O'||a[x][y]=='T')
	 {
	  if(x==3&&y==3&&(a[0][0]=='O'||a[0][0]=='T')&&(a[1][1]=='O'||a[1][1]=='T')&&(a[2][2]=='O'||a[2][2]=='T')&&(a[3][3]=='O'||a[3][3]=='T'))
	  {
	   return 1;
	  }
	 }
	}
	for(int x=i+1,y=j-1;x<4&&y>=0;x++,y--)
	{
	 if(a[x][y]=='O'||a[x][y]=='T')
	 {
	  if(x==3&&y==0&&(a[0][3]=='O'||a[0][3]=='T')&&(a[1][2]=='O'||a[1][2]=='T')&&(a[2][1]=='O'||a[2][1]=='T')&&(a[3][0]=='O'||a[3][0]=='T'))
	  {
	   return 1;
	  }
	 }
	}
   }
  }
 }
 return 0;
}


int checkd(char a[][5])
{
 for(int i=0;i<4;i++)
 {
  for(int j=0;j<4;j++)
  {
   if(a[i][j]=='.')
   {
    return 1;
   }
  }
 }
 return 0;
}


int main()
{
 int t,ans[10];
 cin>>t;
 char a[5][5];
 if(t>=1&&t<=10)
 {
  for(int i=0;i<t;i++)
  {
   ans[i]=0;
   for(int j=0;j<4;j++)
   {
    cin>>a[j];
   }
   if(checkx(a))
   {
    ans[i]=1;
	continue;
   }
   if(checky(a))
   {
    ans[i]=2;
	continue;
   }
   if(checkd(a))
   {
    ans[i]=3;
	continue;
   }
  }
  cout<<endl;
  for(int i=0;i<t;i++)
  {
   cout<<"Case #"<<i+1<<": ";
   if(ans[i]==1)
    cout<<"X won"<<endl;
   if(ans[i]==2)
    cout<<"O won"<<endl;
   if(ans[i]==3)
    cout<<"Game has not completed"<<endl;
   if(ans[i]==0)
    cout<<"Draw"<<endl;
  }
 }
 return 0;
}
