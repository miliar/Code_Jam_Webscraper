#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

const int modd=10;
int a[100];
int l;
int h[10];

inline void pluss(int n)
{
    a[0]+=n;
    int i=0;
    while(i<100 && a[i]>=modd){
        a[i+1]+=a[i]/modd;
        a[i]%=modd;
        ++i;
    }
    if(i>l) l=i;
    while(l>=0 && a[l]==0) --l;
}
inline int point()
{
    for(int i=0;i<=l;++i) h[a[i]]=1;
    int k=0;
    for(int i=0;i<10;++i) k+=h[i];
    if(k==10) return 1;else return 0;
}

inline void print(){
    for(int i=l;i>=0;--i) cout<<a[i];
    cout<<endl;
}

int main(){
    int T,n;
    scanf("%d",&T);
    for(int i=1;i<=T;++i){
        printf("Case #%d: ",i);
        scanf("%d",&n);
        if(n==0)
        {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        memset(a,0,sizeof(a));
        memset(h,0,sizeof(h));
        l=1;
        int f=0;
        while(!f){
            pluss(n);
            f=point();
        }
        print();
    }
    return 0;
}
