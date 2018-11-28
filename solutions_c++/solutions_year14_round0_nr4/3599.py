//Aditya Dixit
#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <functional>
#include <algorithm>
#include <cstdlib>
#include <iomanip>
#include <stack>
#include <queue>
#include <deque>
#include <limits>
#include <cmath>
#include <numeric>
#include <set>

using namespace std;

#define gx getchar_unlocked
#define px putchar_unlocked
#define ps putchar_unlocked(' ')
#define pn putchar_unlocked('\n')
#define LIM
#define MOD 1000000009
#define pb push_back
#define mp make_pair
#define MEM(a, b) memset(a, (b), sizeof(a))
#define CLR(a) memset(a, 0, sizeof(a))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define DBG(vari) cerr<<#vari<<" ==> "<<(vari)<<endl;

const int INF = 2000000000;

typedef long long int i64;
typedef long int i32;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector <PII> VPII;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("aaout.txt","w",stdout);
	
	//std::ios_base::sync_with_stdio(false);
	int t,tt,n,ct,i,j;
	cin >> t;
	tt=0;
	float nmi[1005],ken[1005];
	
	while(t--)
	{
		tt++;
		scanf("%d",&n);
		
		for(i=0;i<n;i++)
		 scanf("%f",&nmi[i]);
		 
		for(i=0;i<n;i++)
		 scanf("%f",&ken[i]);
		 
		sort(nmi,nmi+n);
		sort(ken,ken+n);
		
		/*for(i=0;i<n;i++)
		 printf("%0.3f ",nmi[i]);
		
		px('\n'); 
		 //cout<<"chl\n";
		for(i=0;i<n;i++)
		printf("%0.3f ",ken[i]);
		
		px('\n');*/
		
		ct=0;
		i=0,j=0;
		
		
		
		for(i = 0; i < n ; i++)
		for(; j < n ;)
		{
			if( nmi[j++] < ken[i] )
              ct++; 
             else
              break; 
         }
         
         printf("Case #%d: %d ",tt,n-ct);
         
         
         ct=0;
         
         for(i=0,j=0;j<n ; j++)
		 {	 
				 if(nmi[i] < ken[j] )
				  {
					  ct++;
					  i++;
				  }
				  
				 
		}	
				  
        printf("%d\n",n-ct); 
         
      }
      
      return 0;
}         
              			 
			
		
		 
		  
		 
		 
		
		
	


