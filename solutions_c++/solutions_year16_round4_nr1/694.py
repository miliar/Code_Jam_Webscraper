#include<iostream>
#include<cstring>
#include<cstdio>
#include<iomanip>
#include<algorithm>
#include<queue>
using namespace std;
#define ll __int64
const int N=18;
struct Node{
    int num,id;
}t[3];
int cmp(Node a,Node b){
    if(a.num!=b.num) return a.num<b.num;
    return a.id<b.id;
}
void print(int x){
    if(x==0) printf("P");
    if(x==1) printf("R");
    if(x==2) printf("S");
}
void prin(int id,int dep){
    if(dep==0){
        print(id); return;
    }
    if(id==0){
        prin((id+0)%3,dep-2);
        prin((id+1)%3,dep-2);
        prin((id+1)%3,dep-2);
        prin((id+2)%3,dep-2);
    }
    else if(id==1){
        prin((id+2)%3,dep-2);
        prin((id+1)%3,dep-2);
        prin((id+0)%3,dep-2);
        prin((id+1)%3,dep-2);
    }
    else{
        prin((id+1)%3,dep-2);
        prin((id+2)%3,dep-2);
        prin((id+1)%3,dep-2);
        prin((id+0)%3,dep-2);
    }

}
int main(){
    #ifdef DouBi
    freopen("in.cpp","r",stdin);
    freopen("out.cpp","w",stdout);
    #endif // DouBi
    int TAT,cas=1; scanf("%d",&TAT);
    while(TAT--){
        int n; scanf("%d",&n);
        scanf("%d%d%d",&t[1].num,&t[0].num,&t[2].num);
        t[0].id=0; t[1].id=1; t[2].id=2;
        sort(t,t+3,cmp);
        printf("Case #%d: ",cas++);
        if(n==1){
            if(t[2].num==2) printf("IMPOSSIBLE\n");
            else{
                for(int i=1;i<3;i++) print(t[i].id);
                printf("\n");
            }
            continue;
        }
        int dx=t[1].num-t[0].num, dy=t[2].num-t[0].num;
        if(n%2==1){
            int off=(n-1)/2;
            if(dx==1&&dy==1){
                prin((t[1].id+off*2)%3,n-1); prin((t[2].id+off*2)%3,n-1);
                printf("\n");
            }
            else printf("IMPOSSIBLE\n");
        }
        else{
            int off=(n/2);
            if(dy==1&&dx==0){
                prin((t[2].id+off*2)%3,n);
                printf("\n");
            }
            else printf("IMPOSSIBLE\n");
        }

    }
    return 0;
}
