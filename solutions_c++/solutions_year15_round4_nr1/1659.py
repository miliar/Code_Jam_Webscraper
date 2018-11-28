#include <bits/stdc++.h>
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define ll long long
#define pb push_back
#define mp make_pair
using namespace std;
char grid[101][101];
int r,c;
int l(int x,int y)
{
	 int ff=0;
	  for(int j=y-1;j>=1;--j)
	  if(grid[x][j]!='.')
	    ff=1;
	 return ff;
}

int ri(int x,int y)
{
	 int ff=0;


  for(int j=y+1;j<=c;++j)
	  if(grid[x][j]!='.')
	    ff=1;
	 return ff;
}

int to(int x,int y)
{
	 int ff=0;


  for(int j=x-1;j>=1;--j)
	  if(grid[j][y]!='.')
	    ff=1;
	 return ff;
}

int dn(int x,int y)
{
	 int ff=0;


  for(int j=x+1;j<=r;++j)
	  if(grid[j][y]!='.')
	    ff=1;
	 return ff;
}

int value(char ch)
{
	if(ch=='<')
	return 0;
	else if(ch=='>')
	return 1;
	else if(ch=='^')
	return 2;
	else
	return 3;
}
int main() {
	//freopen("C:\Documents and Settings\TAPAN\Desktop\abc.txt","r",stdin);
 //

//freopen("output.txt","w",stdout);

    int t,i,j,k;
    cin>>t;
    for(k=1;k<=t;++k)
    {
    	cout<<"Case #"<<k<<": ";

    cin>>r>>c;
    for(i=1;i<=r;++i)
    	for(j=1;j<=c;++j)
    	 scanf(" %c",&grid[i][j]);

    	 int f=1;
    	 int ans=0;
    	 for(i=1;i<=r;i++)
    	 	for(j=1;j<=c;++j)
    	 		{


		if(grid[i][j]=='.')
                 continue;
            else
                {
                  //cout<<grid[i][j]<<endl;
    	 			  	 int a=l(i,j);
    	 			     int b=ri(i,j);
    	 			  	 int c=to(i,j);
    	 			  	 int d=dn(i,j);
    	 			  	// cout<<a<<" "<<b<<c<<d<<endl;
    	 			  	 if(a==0 && b==0 && c==0 && d==0)
    	 			  	 f=0;
    	 			  	 int val = value(grid[i][j]);

                         if(val==0 && a==0)
    	 			  	 	ans++;
    	 			  	 if(val==1 && b==0)
    	 			  	 	ans++;
    	 			  	 if(val==2 && c==0)
                              ans++;
    	 			  	 if(val==3 && d==0)
                            ans++;
                  }
    	 		}



    	 	if(f)
    	 		cout<<ans<<endl;
    	 	else


cout<<"IMPOSSIBLE"<<endl;
    }
	return 0;
}
