#include <bits/stdc++.h>
using namespace std;
char str[100005];
int main()
{
	freopen("C:\\Users\\DARPAN\\Desktop\\input.in","r",stdin);
	freopen("C:\\Users\\DARPAN\\Desktop\\output.txt","w",stdout);
	int t;
	cin>>t;
	int j=1;
	while(j<=t)
	{
	    int ct=0,n,sum=0;
	    scanf("%d%s",&n,str);
	    for(int i=0;i<n+1;i++)
	    {
	       if(sum<i)
	       {
	       ct++;
	       sum++;
	       }
	       sum=sum+(str[i]-'0');
	    }
	    printf("Case #%d: %d\n",j,ct);
	    j++;
    }
}

