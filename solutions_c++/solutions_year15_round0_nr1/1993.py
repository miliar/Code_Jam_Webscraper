#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

char s[1010];
int n;
const int inf=0x3f3f3f3f;
bool check(int m){
    int cnt=m;
    for(int i=0;i<=n;i++){
        if(s[i]=='0') continue;
        if(i<=cnt) cnt+=s[i]-'0';
        else return false;
    }
    return true;
}
int main()
{
    //freopen("1.txt","r",stdin);
    //freopen("2.txt","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        scanf("%s",s);
        int l=0,r=n;
        while(l<r){
            int mid=l+r>>1;
            if(check(mid)) r=mid;
            else l=mid+1;
        }
        printf("Case #%d: %d\n",cas++,l);
    }
	return 0;
}
