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
int revert(int num) {
  int reverted = 0;
  while (num) {
    reverted = reverted*10 + num%10;
    num /= 10;
  }
  return reverted;
}

int main()
{
    freopen("c.in","r",stdin);
    freopen("outputC.in","w",stdout);
        
	
	int t;
	cin>>t;
	int n;
     int c=1;
     int l,u;
     
     while(t--)
	{
     int ans=0;
     cin>>l>>u;
     for(int i=l;i<=u;i++)
     {
          int srt=(int)sqrt(i);   
     if(i==(revert(i)) && (i==srt*srt) && srt==revert(srt))        
     {
     ans++;               
     }
     }
     cout<<"Case #"<<c<<": "<<ans<<endl;          
     ans=0;
    c++;
    }     
    
    //system("pause");
	return 0;
}
