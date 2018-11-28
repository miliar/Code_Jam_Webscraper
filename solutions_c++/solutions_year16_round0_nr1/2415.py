#include <cstdio>
#include <algorithm>
#include <iostream>
#include <deque>
#include <cstring>
using namespace std;
typedef deque<int> longint;

void copy(longint&x,int y)
{   x.clear();
    while (y)
    {   x.push_front(y%10);
        y/=10;
    }
}

void add(const longint&a0,const longint&b0,longint&res)
{   longint ans,a=a0,b=b0;
    while (a.size()<b.size()) a.push_front(0);
    while (b.size()<a.size()) b.push_front(0);
    int len=a.size();
    for (int i=len-1;i>=1;i--)
    {   a[i]+=b[i];
        if (a[i]>9) {a[i]-=10;a[i-1]++;}
        ans.push_front(a[i]);
    }
    a[0]+=b[0];
    if (a[0]>9) {a[0]-=10;ans.push_front(a[0]);ans.push_front(1);}
    else ans.push_front(a[0]);
    res=ans;
}



int main () {

    int T;
    scanf("%d",&T);

    for (int casenum=1;casenum<=T;casenum++) {
        int y;longint x,sum;
        //cin>>y;
        scanf("%d",&y);
        if (!y) {
            cout<<"Case #"<<casenum<<": INSOMNIA"<<endl;
            continue;
        }
        copy(x,y);sum=x;
        bool vis[10]={0};memset(vis,0,sizeof vis);
        for(;;) {
            for (int i=0;i<sum.size();i++) vis[sum[i]]=1;
            bool flag=1;
            for (int i=0;i<10;i++) if (!vis[i]) flag=0;
            if (flag) break;
            add(sum,x,sum);
        }
        cout<<"Case #"<<casenum<<": ";
        for (int i=0;i<sum.size();i++) cout<<sum[i];
        cout<<endl;
    }
}
