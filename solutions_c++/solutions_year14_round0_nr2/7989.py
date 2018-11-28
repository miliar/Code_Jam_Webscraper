#include<iostream>
#include<cstdio>
#include<string>
#include<cstdlib>
#include<algorithm>
#include<set>
using namespace std;
int gh[34][34];
int main(){

set <int> jk;set <int> an;
    int y=0;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        double c,f,x;
        cin>>c>>f>>x;
        int n=0;
        for(int k=0;k<=10000000;k++){
            if(c/(2+ k*f) + x/(2+ (k+1)*f)  > x/(2+ k*f) ) { n=k;break;}
        }
        //cout<<n<<endl;
        double ans=0;
        for(int k=0;k<n;k++){
            ans+=c/(2+k*f);
        }
        ans+=x/(2+n*f);
        float pans;
        //pans= ( float ) (ans);
        printf("Case #%d: %.9lf\n",i,ans);
    }


return 0;
}
