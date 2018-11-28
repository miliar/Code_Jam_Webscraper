#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<map>
#include<list>
#include<queue>
#include<stack>
#include<limits.h>
#include<fstream>

#define inpi(x) scanf("%d",&x);
#define inpd(x) scanf("%lf",&x);
#define inpf(x) scanf("%f",&x);
#define inpl(x) scanf("%ld",&x);
#define inpll(x) scanf("%lld",&x);
#define inpull(x) scanf("%llu",&x);
#define inpc(x) scanf("%c",&x);
#define inps(x) scanf("%s",x);//s is base address

#define outi(x) printf("%d",x);
#define outf(x) printf("%f",x);
#define outd(x) printf("%.7lf",x);
#define outl(x) printf("%ld",x);
#define outll(x) printf("%lld",x);
#define outull(x) printf("%llu",x);
#define nl printf("\n")
#define sp printf(" ")

#define forup(i,a,b) for(i=a;i<b;i++)
#define fordn(i,a,b) for(i=a;i>b;i--)

typedef unsigned long long ull;
typedef long long ll;
using namespace std;

double ans,cs;
double c,f,x;


int main(){
    int t,i,j,k,cas;

    inpi(t);
    forup(cas,0,t){
        ans=0;
        inpd(c);inpd(f);inpd(x);
        cs=2;
//        calc(2);
        while(true){
            if (x/cs<=c/cs+x/(cs+f)){
//                cout<<ans;nl;
                ans+=x/cs;
                break;
            }else{
                ans+=c/cs;
                cs+=f;
            }
        }
//        cout<<ans;
        cout<<"Case #"<<cas+1<<": ";outd(ans);nl;
    }
}
