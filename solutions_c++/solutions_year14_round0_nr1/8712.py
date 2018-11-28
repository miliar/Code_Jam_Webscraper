#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<iostream>
#include<string.h>
#include<limits.h>
#include<functional>
#include<vector>
#include<utility>
#include<stdlib.h>
#define mem(a) memset(a,0,sizeof(a))
#define pb push_back
#define bx(i) binary_search(x.begin(),x.end(),i)
#define bo(i) binary_search(o.begin(),o.end(),i)
using namespace std;
inline int fastRead()
      {
        int a=0;
       char c= getchar();
         
            while (c < '0' || c>'9') c=getchar();
        
            while( c >= '0' && c <= '9' )
             {
               a = (a<<3)+(a<<1) + c-'0';
               c=getchar();
             }
        return a;
       
      }
//cout<<"Case #"<<number<<": Game has not completed"<<endl;
int main()
{
	freopen("H:\\input.txt","r",stdin);
	freopen("H:\\output.txt","w",stdout);
	int tc = fastRead();
	for(int number=1;number<=tc;number++)
	{
		int v = fastRead();
		int a[6][6];
		mem(a);
		int i,j;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			a[i][j] = fastRead();
		}
		vector<int> x;
		x.pb(a[v][1]);
		x.pb(a[v][2]);
		x.pb(a[v][3]);
		x.pb(a[v][4]);
		mem(a);
		v = fastRead();
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			a[i][j] = fastRead();
		}
		int ans=0;
		sort(x.begin(),x.end());
		for(i=1;i<=4;i++)
		{
			if(bx(a[v][i]))
			ans++;
		}
//		cout<<"ANS "<<ans<<endl;
		if(ans==0)
		cout<<"Case #"<<number<<": Volunteer cheated!"<<endl;
		else if(ans!=1)
		cout<<"Case #"<<number<<": Bad magician!"<<endl;
		else
		{
			for(i=1;i<=4;i++)
			{
				if(bx(a[v][i]))
				{
					cout<<"Case #"<<number<<": "<<a[v][i]<<endl;
					break;
				}
			}
		}
		
	}
}
