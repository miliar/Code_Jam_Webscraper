#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<string>
#include<algorithm>

#define ll long long

using namespace std;

int n;

char s[1010];

int main() {
    //freopen("A-small-attempt3.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int ca=1;
    while(t--) {
        scanf("%d",&n);
        n++;
        scanf("%s",s);
        int sum=s[0]-48;
        int ans=0;
        for(int i=1; i<n; i++) {
            if(sum>=i) {
                sum+=s[i]-48;
            } else {
                ans+=i-sum;
                sum=i+s[i]-48;
            }
        }
        printf("Case #%d: %d\n",ca++,ans);
    }
    return 0;
}
