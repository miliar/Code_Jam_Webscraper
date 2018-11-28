#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
int aaa[100005],b[100005];
vector<int >g;
int cmp(int a,int b){
    return a>b;
}
int main()
{
    int i,j,n,m,t,N=0;
    cin>>t;
    while(t--){
        cin>>n;
        for(i=1;i<=n;i++){
            scanf("%d",&aaa[i]);
        }
        sort(aaa+1,aaa+1+n);
        m=1000000000;
        for(i=1;i<=1000;i++){
            int s=i;
            for(j=1;j<=n;j++){
                if(aaa[j]>i){
                    if(aaa[j]%i!=0)
                        s+=aaa[j]/i;
                    else s+=aaa[j]/i-1;
                }
            }
            m=min(m,s);
        }
        printf("Case #%d: %d\n",++N,m );
    }
}