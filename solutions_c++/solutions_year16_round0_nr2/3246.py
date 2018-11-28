/* ***********************************************
Author        :yzkAccepted
Created Time  :2016/4/9 18:26:27
TASK		  :ggfly.cpp
LANG          :C++
************************************************ */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <stack>
using namespace std;
typedef __int64 ll;
char a[110];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas=1,i,m,n;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s",a);
		int flag=0,tot=0,ans;
		printf("Case #%d: ",cas);
		cas++;
		n=strlen(a);
		if(a[0]=='-')
			flag=1;
		for(i=0;i<n;i++)
		{
			if(a[i]=='-' && a[i-1]!='-')
			{
				tot++;
			}
		}
		ans=2*tot;
		if(flag==1) ans--; 
		printf("%d\n",ans);
	}
    return 0;
}
