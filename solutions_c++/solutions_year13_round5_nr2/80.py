#include <stdio.h>
#include <algorithm>

using namespace std;

class PT{
    public:
        long long x,y;
        int i;
        PT(){}
        PT(long long _x,long long _y){
            x=_x; y=_y;
        }
        bool operator<(const PT& p) const{
            if(x==p.x) return y<p.y;
            return x<p.x;
        }
        long long operator^(const PT& p) const{
            return x*p.y-y*p.x;
        }
        long long operator*(const PT& p) const{
            return x*p.x+y*p.y;
        }
        PT operator-(const PT& p) const{
            return PT(x-p.x,y-p.y);
        }
};

inline long long tri(PT p1,PT p2,PT p3){
    return (p2-p1)^(p3-p1);
}

inline int btw(PT p1,PT p2,PT p3){
    return (p2-p3)*(p1-p3)<=0;
}

inline int sect(PT p1,PT p2,PT p3,PT p4){
    long long ta=tri(p1,p2,p3);
    long long tb=tri(p1,p2,p4);
    long long tc=tri(p3,p4,p1);
    long long td=tri(p3,p4,p2);
    if(ta==0 && tb==0){
        return btw(p1,p2,p3) || btw(p1,p2,p4) || btw(p3,p4,p1);
    }else{
        if(ta*tb<=0 && tc*td<=0){
            return 1;
        }
        return 0;
    }
}

PT pt[1010];
PT qt[1010];
int u[1010];
int top,n;
long long sum;
int c[1010];

int dfs(int x){
    if(x==n){
        int j;
        for( j=2; j<x-1; j++ ){
            if(sect(pt[c[j-1]],pt[c[j]],pt[c[x-1]],pt[0])){
                break;
            }
        }
        if(j<x-1) return 0;
        if(x>=2){
            if(tri(pt[c[x-2]],pt[c[x-1]],pt[0])==0 && (pt[0]-pt[c[x-1]])*(pt[c[x-2]]-pt[c[x-1]])>=0) return 0;
        }
        long long s=0;
        for( int i=1; i<n-1; i++ ){
            s+=tri(pt[0],pt[c[i]],pt[c[i+1]]);
        }
        if(s*2>sum){
            return 1;
        }
        return 0;
    }else{
        for( int i=0; i<n; i++ ){
            if(u[i]) continue;
            int j;
            for( j=1; j<x-1; j++ ){
                if(sect(pt[c[j-1]],pt[c[j]],pt[c[x-1]],pt[i])){
                    break;
                }
            }
            if(j<x-1) continue;
            if(x>=2){
                if(tri(pt[c[x-2]],pt[c[x-1]],pt[i])==0 && (pt[i]-pt[c[x-1]])*(pt[c[x-2]]-pt[c[x-1]])>=0) continue;
            }
            u[i]=1;
            c[x]=i;
            if(dfs(x+1)) return 1;
            u[i]=0;
        }
    }
}

int main(){
    int tt,TT,i,j,k,z,tx,ty,m,mi,mj;
    long long md,d;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ){
        scanf("%d",&n);
        for( i=0; i<n; i++ ){
            scanf("%d %d",&tx,&ty);
            pt[i].x=tx;
            pt[i].y=ty;
            pt[i].i=i;
            u[i]=0;
        }
        sort(pt,pt+n);
        top=0;
        qt[0]=pt[0];
        for( i=1; i<n; i++ ){
            while(top>0 && tri(qt[top-1],qt[top],pt[i])<=0){
                top--;
            }
            qt[++top]=pt[i];
        }
        z=top;
        for( i=n-2; i>=0; i-- ){
            while(top>z && tri(qt[top-1],qt[top],pt[i])<=0){
                top--;
            }
            qt[++top]=pt[i];
        }
        sum=0;
        for( i=0; i<top-1; i++ ){
            sum+=tri(qt[0],qt[i],qt[i+1]);
        }
        u[0]=1;
        c[0]=0;
        if(dfs(1)){
            printf("Case #%d:",tt+1);
            for( i=0; i<n; i++ ){
                printf(" %d",pt[c[i]].i);
            }
            puts("");
        }else{
            printf("Case #%d: shit\n",tt+1);
        }
    }
    return 0;
}
