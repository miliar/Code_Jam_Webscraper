#include<fstream>
#include<iostream>
#include<sstream>
#include<bitset>
#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<iterator>
#include<string>
#include<cassert>
#include<cctype>
#include<climits>
#include<cmath>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>

#define TIMER 0 
#define MAX 10
#define yes "YES"
#define no "NO"

using namespace std;

int inp[MAX][MAX];
int done[MAX][MAX];
int m,n;
int si[MAX],sj[MAX];
bool row=false,col=false;
char * solve(){

		for(int i=0;i<(m);i++)
			if (inp[i][0] == 1)
			{ si[i]=1;
				for(int j=0;j<n;j++)
				 if(inp[i][j] != 1)
					{si[i]=0;break;}		
			}else if (inp[i][0] == 2)
			{	si[i]=1;
				for(int j=0;j<n;j++)
				 if(inp[i][j] != 2)
					{si[i]=0;break;}
			}		
			for(int j=0;j<n;j++)
			if (inp[0][j] == 1)
			{ sj[j]=1;
				for(int i=0;i<m;i++)
				 if(inp[i][j] != 1)
					{sj[j]=0;break;}		
			}else if (inp[0][j] == 2)
			{	sj[j]=1;
				for(int i=0;i<m;i++)
				 if(inp[i][j] != 2)
					{sj[j]=0;break;}
			}
	    for(int i=0;i<m;i++)
		{if(si[i]==1)continue;
		else 
				for (int j=0;j<n;j++)      
				if(sj[j]==1)continue;
				else 
					if(inp[i][j] != 2)
						return no;

        }
		return yes;
}


int main(){
	int T=0;
	scanf("%d",&T);
	 for(int t=1;t<=T;t++){
		 scanf("%d %d" ,&m,&n);
	     for(int i=0;i<m;i++)
			 for(int j=0;j<n;j++)
			 {scanf("%d",&inp[i][j]);  
				done[i][j]=0;
		 }
		
        printf("Case #%d: %s\n",t,solve());
	}	
	return 0;
}
