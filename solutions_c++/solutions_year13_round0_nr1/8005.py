#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<set>
#include<vector>
#include<stack>
#include<queue>
#include<sstream>
#include<map>
using namespace std;
#define si scanf("%d",&n);

int main()
{
    freopen("a.in","r",stdin);
freopen("output.in","w",stdout);
      
	
	int t;
	cin>>t;
	int n;
     int c=1;
     while(t--)
	{
               
    char a[4][4];
    for(int i=0;i<4;i++)
    {
    for(int j=0;j<4;j++)
    {
    cin>>a[i][j];        
    }        
    }
    int x=0,o=0,dot=0;
    for(int i=0;i<4;i++)
    {
    if(a[i][0]=='O'&& a[i][1]=='O'&& a[i][2]=='O'&& a[i][3]=='O' || a[i][0]=='O'&& a[i][1]=='O'&& a[i][2]=='O'&& a[i][3]=='T' || a[i][0]=='T'&& a[i][1]=='O'&& a[i][2]=='O'&& a[i][3]=='O')
    {
     o=1;
    }
    if(a[i][0]=='X'&& a[i][1]=='X'&& a[i][2]=='X'&& a[i][3]=='X' || a[i][0]=='X'&& a[i][1]=='X'&& a[i][2]=='X'&& a[i][3]=='T' || a[i][1]=='T'&& a[i][1]=='X'&& a[i][2]=='X'&& a[i][3]=='X')
    {
    x=1;
    }
    } 
    
    
    for(int i=0;i<4;i++)
    {
    for(int j=0;j<4;j++)
    {
    if(a[i][j]=='.')        
    {
         dot=1;                   
    }
    }
            
    }
    
    
      for(int j=0;j<4;j++)
    {
    if(a[0][j]=='O'&& a[1][j]=='O'&& a[2][j]=='O'&& a[3][j]=='O' || a[0][j]=='O'&& a[1][j]=='O'&& a[2][j]=='O'&& a[3][j]=='T' || a[0][j]=='T'&& a[1][j]=='O'&& a[2][j]=='O'&& a[3][j]=='O')
    {
     o=1;
    }
    if(a[0][j]=='X'&& a[1][j]=='X'&& a[2][j]=='X'&& a[3][j]=='X' || a[0][j]=='X'&& a[1][j]=='X'&& a[2][j]=='X'&& a[3][j]=='T' || a[0][j]=='T'&& a[1][j]=='X'&& a[2][j]=='X'&& a[3][j]=='X')
    {
     x=1;
    }
    } 
    
    if(a[0][0]=='O'&& a[1][1]=='O'&& a[2][2]=='O' && a[3][3]=='O' || a[0][0]=='O'&& a[1][1]=='O'&& a[2][2]=='O' && a[3][3]=='T' || a[0][0]=='T'&& a[1][1]=='O'&& a[2][2]=='O' && a[3][3]=='O')
    {
                                   o=1; 
    }
    if(a[0][0]=='X'&& a[1][1]=='X'&& a[2][2]=='X' && a[3][3]=='X' || a[0][0]=='X'&& a[1][1]=='X'&& a[2][2]=='X' && a[3][3]=='T' || a[0][0]=='T'&& a[1][1]=='X'&& a[2][2]=='X' && a[3][3]=='X')
                                              {
                                   x=1; 
    }
     if(a[0][3]=='O'&& a[1][2]=='O'&& a[2][1]=='O' && a[3][0]=='O' || a[0][3]=='O'&& a[1][2]=='O'&& a[2][1]=='O' && a[3][0]=='T' || a[0][3]=='T'&& a[1][2]=='O'&& a[2][1]=='O' && a[3][0]=='O')
    {
                                   o=1; 
    }
    if(a[0][3]=='X'&& a[1][2]=='X'&& a[2][1]=='X' && a[3][0]=='X' || a[0][3]=='X'&& a[1][2]=='X'&& a[2][1]=='X' && a[3][0]=='T' || a[0][3]=='T'&& a[1][2]=='X'&& a[2][1]=='X' && a[3][0]=='X')
    {
                                   x=1; 
    }
    cout<<"Case #"<<c<<": ";
    
    if(x==0 && o==0 && dot==0)
    {
      cout<<"Draw"<<endl;       
    }
    else if(x==1 && o==0)
    {
    cout<<"X won"<<endl;     
    }
    else if(o==1 && x==0)
    {
    cout<<"O won"<<endl;     
    }
    else if(x==0 && o==0 && dot==1)
    {
    cout<<"Game has not completed"<<endl;    
    } 
    
    
    c++;
    }     
       //system("pause");
	return 0;
}
