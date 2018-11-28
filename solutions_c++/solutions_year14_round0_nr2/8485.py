#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;

double V,v,x,c,f,ans;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin>>T;
    for (int _=1;_<=T;_++){
        scanf("%lf%lf%lf",&c,&f,&x);
        ans=0;
        v=2;
        V=f*(x/c-1);
        while (v<V){
            ans+=c/v;
            v+=f;
        }
        ans+=x/v;
        printf("Case #%d: %.7f\n",_,ans);
    }
//    system("pause");
}
/*
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

*/
