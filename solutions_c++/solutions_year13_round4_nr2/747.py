#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int n,T,lose,win;
long long p,power[101]; 
bool a[101];

/*int checklose(long long now)
{
    //cout<<"now = "<<now<<endl;
    if (now==0) return 0;
    long long rest=now;
    int cnt=0;
    for (int i=1;i<=n;i++){
        rest=(rest-1)/2;
        if (rest==0) break;
    }   
   // cout<<"lostcnt = "<<cnt<<endl;
    if (cnt>lose) return 1;
    return 0;
}*/

int checklose(long long now)
{
    //cout<<"now = "<<now<<endl;
    if (now==0) return 1;
    long long rest=now;
    int cnt=0;
    for (int i=1;i<=n;i++){
        rest=(rest-1)/2;cnt++;
        if (rest==0) break;
    }   
    long long ans=0;
    for (int i=1;i<=cnt;i++) ans=ans*2+1;
    for (int i=1;i<=n-cnt;i++) ans*=2;
    //cout<<"lostcnt = "<<ans<<endl;
    if (ans<p) return 1;
    return 0;
}

int checkwin(long long now)
{
    //cout<<"now = "<<now<<endl;
    if (now==power[n]-1) return 0;
    long long rest=power[n]-now-1;
    int cnt=0;
    for (int i=1;i<=n;i++){
        rest=(rest-1)/2;cnt++;
        if (rest==0) break;
    }   
    long long ans=0;
    for (int i=1;i<=cnt;i++) ans=ans*2;
    for (int i=1;i<=n-cnt;i++) ans=ans*2+1;
    //cout<<"lostcnt = "<<ans<<endl;
    if (ans<p) return 1;
    return 0;
}

void operation()
{
    long long st=0,ed=power[n]-1,ans1,ans2;
    while (st<ed){
          long long mid=(st+ed)/2;
          if (checklose(mid)) st=mid+1;else ed=mid; 
    }
    if (checklose(st)) ans1=st;else ans1=st-1;
    st=0,ed=power[n]-1;
    while (st<ed){
          long long mid=(st+ed)/2;
          if (checkwin(mid)) st=mid+1;else ed=mid; 
    }
    if (checkwin(st)) ans2=st;else ans2=st-1;
    cout<<ans1<<" "<<ans2<<endl;
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout); 
    cin>>T;
    power[0]=1;
    for (int i=1;i<=50;i++){power[i]=power[i-1]*2;} 
    for (int Case=1;Case<=T;Case++){
        cin>>n>>p; 
        cout<<"Case #"<<Case<<": ";
        if (p==power[n]) cout<<p-1<<" "<<p-1<<endl;else
        operation(); 
    }
}

/* 
0 
1 1

2
7 7 7

3 4 6
4

5 6
6


5 5
6

4 
7
*/
