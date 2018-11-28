#include <bits/stdc++.h>
#define mp make_pair
using namespace std;
int n;
set<double> s1,s2,s3;
main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int test=1;test<=t;test++){
        printf("Case #%d:",test);
        s1.clear();
        s2.clear();
        cin>>n;
        double x;
        for(int i=0;i<n;i++){
            cin>>x;
            s1.insert(x);
        }
        for(int i=0;i<n;i++){
            cin>>x;
            s2.insert(x);
        }
        int ans=0,ans1=0;
        s3=s2;
        for(set<double> :: iterator it=s1.begin();it!=s1.end();++it){
            set<double> :: iterator it1=s3.lower_bound(*it);
            if(it1!=s3.end()){
                s3.erase(it1);
            }else{
                ++ans;
                s3.erase(s3.begin());
            }
        }
        for(set<double> :: iterator it=s1.begin();it!=s1.end();++it){
            set<double> :: iterator it2=s2.end();it2--;
            if(*it>*s2.begin()){
                s2.erase(s2.begin());
                ++ans1;
            }else{
                s2.erase(it2);
            }
        }
        printf(" %d %d\n",ans1,ans);
    }
}
