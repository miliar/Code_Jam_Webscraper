#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<cmath>
#include<queue>
#include<cstring>
#include<string>
#include<bitset>
#include<algorithm>
using namespace std;
int solve(int r,int c,int w)
{

       if(w==c)
		return c;
	else
		return (w-1+ceil((c*1.0)/w));
    
}
int cse=1;
main()
{
//freopen("in.txt","r",stdin);
//freopen("out.txt","w",stdout);
int t;
cin>>t;
while(t--){
int r,c,w;
cin>>r>>c>>w;
printf("Case #%d: %d\n",cse++,solve(r,c,w));
}
return 0;
}




