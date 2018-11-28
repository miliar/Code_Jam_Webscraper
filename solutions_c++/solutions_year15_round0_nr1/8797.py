#include<iostream>
#include<cstring>
#include<cstdio>
#define M 1001

using namespace std;

char a[M];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,maxs,c=1;
    cin>>t;
    while(t--) {
        int s=0,ned=0;
        cin>>maxs;
        cin>>a;
        int len=strlen(a);
        s=(int)(a[0]-'0');
        for(int i=1;i<len;i++) {
          int n=(int)(a[i]-'0');
          if(s>maxs) break;
          else if(s<i) {
             int d=i-s;
             ned+=d;
             s=s+n+d;
          }else  s=s+n;
           // cout<<s<<endl;
        }
        cout<<"Case #"<<c<<": "<<ned<<endl;
        c++;
    }
    return 0;
}
