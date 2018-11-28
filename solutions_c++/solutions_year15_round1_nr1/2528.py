#include<iostream>
#include<string>
#include<cstring>
#include<cstdio>
using namespace std;
const int MAXN=1000+10;
const int INF=99999999;
int a[MAXN];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,n,id=0;
    cin>>T;
    while(T--){
        int y=0,z=0,rate=0;
        cin>>n;
        cin>>a[0];
        for(int i=1;i<n;i++){
            cin>>a[i];
            int d=a[i-1]-a[i];
            if(d>0)y+=d;
            rate=max(d,rate);
        }
        for(int i=0;i<n-1;i++){
            if(a[i]<rate)z+=a[i];
            else z+=rate;
        }
        printf("Case #%d: %d %d\n",++id,y,z);
    }
    return 0;
}
