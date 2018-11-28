#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<iostream>
#include<map>
#define REP(i,n) for(int i=0;i<n;i++)
typedef long long ll;

using namespace std;
int ans1[5][5];
int ans2[5][5];
int main(){
#ifdef LOCALL
    freopen("B-large.in","r",stdin);
//    freopen("in","r",stdin);
    freopen("B-large.out","w",stdout);
#endif
    int t,a,b;
    cin>>t;
    for(int kase = 1;kase <= t;kase ++){
        double ret,c,f,x;
        cin>>c>>f>>x;
        cout<<"Case #"<<kase<<": ";
        if(x <= c){printf("%.7f\n",x/2);continue;}

        double nxt = 0,now = 0,time = 0,v = 2,ansnow,ansnxt;
        int flag = 0;
        while(!flag){
            now = nxt;
            time += c/v;
//            cout<<"time: "<<time << "\t v: "<<v<<"\t"<<"ansnow: "<<ansnow<<"\tansnxt: "<<ansnxt<<endl;
            nxt = time;
            ansnow = now + x/v;
            ansnxt = nxt + x/(v+f);
            if(ansnow < ansnxt) flag = 1;
            v += f;
        }
//        cout<<"\n";
        printf("%.7f\n",ansnow);
    }
    return 0;
}

