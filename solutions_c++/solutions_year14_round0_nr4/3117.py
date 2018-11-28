#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm> 
using namespace std;
#define maxn 1110
double a[maxn],b[maxn];
int n;
int main()
{
    freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
    int t,cas,i,j,k,cnt;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++){
        cin>>n;
        for(i=0;i<n;i++)
            cin>>a[i];
        
        for(i=0;i<n;i++)
            cin>>b[i];
        
        sort(a,a+n);
        sort(b,b+n);
        k=0;
		cnt=0;
        j=n-1;
        for(i=n-1;i>=0 && j>=0;i--)
            while(j>=0){
                if(b[i]>a[j]){
                    j--;
                    k++;
                    break;
                }
                j--;
            }
        
        j=n-1;
        for(i=n-1;i>=0 && j>=0;i--)
            while(j>=0){
                if(a[i]>b[j]){
                    j--;
                    cnt++;
                    break;
                }
                j--;
            }
        
        printf("Case #%d: %d %d\n",cas,cnt,n-k);
    }
    return 0;
}
