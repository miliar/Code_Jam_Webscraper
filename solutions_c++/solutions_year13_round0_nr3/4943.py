#include <iostream>
#include <cstdio>
using namespace std;
int main() 
{
int a[]={1,4,9,121,484};
    int ans[1001];
    for(int i=0,k=0;i<1001;i++)
        {
            if(i>=a[k]&&k<5)
                k++;
            ans[i]=k;         
        }
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int a,b;
        scanf("%d %d",&a,&b);
        printf("Case #%d: %d\n",i+1,(ans[b]-ans[a-1]));
    }
	return 0;
}