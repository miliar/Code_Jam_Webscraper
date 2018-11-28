#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int vis[20];
int main(){
    int t;
    double now,al,next,c,f,x;
    double res;
    int ca=1;
    cin>>t;
    while(t--){
        cin>>c>>f>>x;
        now=2;
        next=now+f;
        al=0;
        while(al+x/now>c/now+x/next+al){
            al+=c/now;
            now=now+f;
            next=now+f;
        }
        res=al+x/now;
        printf("Case #%d: %.7lf\n",ca++,res);
    }
    return 0;
}
