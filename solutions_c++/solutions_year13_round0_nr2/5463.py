#include <algorithm>
#include <map>
#include <string>
#include <assert.h>
#include <iostream>
using namespace std;

int a[101][101];
int b[101][101];

bool checkRow(int i, int j ,int n, int m)
{
   int row = j;
   for(int k=0;k<n;k++)
   {
	   if(a[k][row] != 1) return false;
   }
   return true;
}

bool checkLine(int i, int j ,int n, int m)
{
   int line = i;
   for(int k=0;k<m;k++)
   {
	   if(a[line][k] != 1) return false;
   }
   return true;
}

int main()
{
	freopen("1.in","r",stdin);
   freopen("1.out","w",stdout);
	int t,n,m;	
   
    cin>>t;
	bool mark =true;
    for (int i=1;i<=t;i++)
    {       
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		cin>>n>>m;
		mark = true;
		for(int ki= 0;ki<n;ki++)
		{
			for(int kj =0;kj<m;kj++)
			{
				cin>>a[ki][kj];
			}
		}

		for(int ki= 0;ki<n;ki++)
		{
			for(int kj =0;kj<m;kj++)
			{
				if(a[ki][kj] == 1)
				{
					if( !(checkRow(ki,kj,n,m) == true || checkLine(ki,kj,n,m) == true))
					{
						mark = false;
						goto end;
					}
				}
			}
		}

end:	
         cout<<"Case #"<<i<<": ";   
		 if(mark) cout<<"YES"<<endl;
		 else cout<<"NO"<<endl;
    }    

    return 1;
}