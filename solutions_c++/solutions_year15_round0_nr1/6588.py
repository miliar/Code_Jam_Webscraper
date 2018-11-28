#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
  	freopen("out.txt","w",stdout);
    int t,T,n,sum,ant,num;
    char b[1500];
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        scanf("%s",b);
        sum=0;
		ant=0;
        for(int i=0;i<=n;i++)
        {
            num=b[i]-'0';
            if(sum>=i)
				sum+=num;
			else
            {
                ant+=i-sum;
                sum=i+num;
            }     
        }
        printf("Case #%d: %d\n",t,ant);
    }
    return 0;
}
