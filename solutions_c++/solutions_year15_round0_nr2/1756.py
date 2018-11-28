#include <bits/stdc++.h>
using namespace std;
int a[2000];
int n,t;
int main(){
#define RUN
#ifdef RUN
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif // RUN
    cin>>t;
    for(int cs=1;cs<=t;cs++){
        memset(a,0,sizeof a);
        cin>>n;
        for(int i = 0;i<n;i++){
            cin>>a[i];
        }
        sort(a,a+n,greater<int>());
        int ans = a[0];
        for(int i=1;i<a[0];i++){
            int sum = 0;
            for(int j=0;j<n;j++){
                if(a[j]<=i)
                    break;
                sum+=a[j]/i;
                if(a[j]%i==0)
                    --sum;
            }
            sum+=i;
            if(sum<ans)
                ans = sum;
        }
        cout<<"Case #"<<cs<<": "<<ans<<endl;
    }
}
