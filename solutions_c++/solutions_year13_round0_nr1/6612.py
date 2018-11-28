#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <climits>
#include <cctype>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <deque>
#include <queue>
#include <stack>
#include <iomanip>
#include <complex>
#include <list>
#include <bitset>
#include <fstream>
#include <limits>
#include <memory.h>

using namespace std;

#define REP(i,n) for( (i)=0 ; (i)<(n) ; (i)++ )
#define rep(i,x,n) for( (i)=(x) ; (i)<(n) ; (i)++ )
#define REV(i,n) for( (i)=(n) ; (i)>=0 ; (i)-- )
#define FORIT(it,x) for( (it)=(x).begin() ; (it)!=(x).end() ; (it)++ )
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define SZ(x) (x).size()
#define MMS(x,n) memset(x,n,sizeof(x))
#define pb push_back
#define mp make_pair
#define UN(x) sort(all(x)),x.erase(unique(all(x)),x.end())
#define CV(x,n) count(all(x),(n))
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

int  check(char arr[4][4])
{
int countx=0;
int countdot=0;
int counto=0;
int countt=0;
 for(int i=0;i<4;i++ )   
{
 countx=0;
 counto=0;
 countt=0;

for(int j=0;j<4;j++)	
{
if(arr[i][j]=='X')
countx++;
else if(arr[i][j]=='O')	
counto++;
else if(arr[i][j]=='T')
countt++;
else
countdot++;	
	}	
	
if((countx==3&&countt==1)||(countt==0&&countx==4))		
	return 1;
else if((counto==3&&countt==1)||(countt==0&&counto==4))		
	return 2;
	
}

for(int i=0;i<4;i++ )   
{
 countx=0;
 counto=0;
 countt=0;

for(int j=0;j<4;j++)	
{
if(arr[j][i]=='X')
countx++;
else if(arr[j][i]=='O')	
counto++;
else if(arr[j][i]=='T')
countt++;
else
countdot++;
	
	}	
if((countx==3&&countt==1)||(countt==0&&countx==4))		
	return 1;
else if((counto==3&&countt==1)||(countt==0&&counto==4))		
	return 2;
}
 countx=0;
 counto=0;
 countt=0;


for(int i=0;i<4;i++ )   
{
if(arr[i][i]=='X')
countx++;
else if(arr[i][i]=='O')	
counto++;
else if(arr[i][i]=='T')
countt++;
else
countdot++;

}
if((countx==3&&countt==1)||(countt==0&&countx==4))		
	return 1;
else if((counto==3&&countt==1)||(countt==0&&counto==4))		
	return 2;
	countx=0;
 counto=0;
 countt=0;

for(int i=0;i<4;i++ )   
{
if(arr[i][3-i]=='X')
countx++;
else if(arr[i][3-i]=='O')	
counto++;
else if(arr[i][3-i]=='T')
countt++;
else
countdot++;

}
if((countx==3&&countt==1)||(countt==0&&countx==4))		
	return 1;
else if((counto==3&&countt==1)||(countt==0&&counto==4))		
return 2;


if(countdot>0)
return 3;





return 0;	
}


int main()
{
    READ("A-large.in");    // esm l downloaded file ay 7aga 
    WRITE("A-large.out");  // esm l output file w dah hn3melo upload m3 l source pp
 char arr[4][4];
 double n;
 cin>>n;
 for(int k=1;k<=n;k++ )   
    {
 for(int i=0;i<4;i++ )   
    {
    	for(int j=0;j<4;j++ )   
    { cin>>arr[i][j];
	}
     }

int c;
c=check(arr);
if(c==3)
cout<<"Case #"<<k<<": Game has not completed"<<endl;
else if(c==1)
cout<<"Case #"<<k<<": X won"<<endl;
else if(c==2)
cout<<"Case #"<<k<<": O won"<<endl;
else  if(c==0)
cout<<"Case #"<<k<<": Draw"<<endl;
	
	
		
    	
    	
    	
    }
    
    
    return 0;
}
