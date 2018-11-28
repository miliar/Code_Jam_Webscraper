#include <iostream>
#include <sstream>
#include <string.h>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <map>
#define pb push_back
#define MAXN 1
#define MAXM 1
#define INF (1<<30)
#define PI 3.1415926535898
#define esp 10e-6
#define Si size()
const int dx[4]={1,0,-1,0};
const int dy[4]={0,-1,0,1};
using namespace std;
long long ans1,ans2;
int N,M;

struct Point{
    int x;
    int y;
    int note;
    //Point (int _x,int _y,int _note):x(_x),y(_y),note(_note){}
}a[2100];

bool cmp(Point a,Point b){
    if (a.x==b.x)
        return a.note<b.note;
    else
        return a.x<b.x;
}

void init(){
    int p,q,c;
    ans1=ans2=0;
    scanf("%d%d",&N,&M);
    for (int i=0;i<M;++i){
        scanf("%d%d%d",&p,&q,&c);
        a[i].x=p;
        a[i].y=c;
        a[i].note=0;
        a[i+M].x=q;
        a[i+M].y=c;
        a[i+M].note=1;
        long long tmp=(N-(q-p-1));
        long long tmq=(q-p);
        //cout<<tmp<<" "<<tmq<<endl;
        ans1=ans1+((N+tmp)*tmq)/2*c;
    }
    //cout<<"!"<<endl;
    sort(a,a+2*M,cmp);
}

vector <Point> list;

void work(){
    ans2=0;
    list.clear();
    for (int i=0;i<2*M;++i){
        if (a[i].note==0){
            list.pb(a[i]);
        }
        else{
            //int p=a[i].y;
            while (a[i].y>0){
                int s=list.Si-1;
                int q=min(list[s].y,a[i].y);
                long long tmp=(N-(a[i].x-list[s].x-1));
                long long tmq=(a[i].x-list[s].x);
                ans2=ans2+((N+tmp)*tmq)/2*q;
                a[i].y-=q;
                list[s].y-=q;
                if (list[s].y==0)
                    list.pop_back();
            }
        }
    }
}

void output(){
    //cout<<ans1<<endl;
    //cout<<ans2<<endl;
    cout<<ans1-ans2<<endl;
}

int main(){
    int T;
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    for (int tt=1;tt<=T;++tt){
        printf("Case #%d: ",tt);
        init();
        work();
        output();
    }
    return 0;
}
