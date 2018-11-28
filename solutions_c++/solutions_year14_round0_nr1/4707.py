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
#define outd(x) printf("%lf",x);
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

int ar[5];

int main(){
    int t,m,count,cas,i,j,k,a;
    inpi(t);
    forup(cas,0,t){
        count=0;
        inpi(m);
        forup(i,0,4){
            if (i+1==m){
                forup(j,0,4){
                    inpi(ar[j]);
//                    outi(ar[j]);nl;
                }
            }else{
                forup(j,0,4){
                    inpi(a);
                }
            }

        }
//        outi(m);nl;
        inpi(m);
        int ans;
        forup(i,0,4){
            if (i+1==m){
//                outi(i);nl;
                forup(j,0,4){
                    inpi(a);
                    forup(k,0,4){
                        if (a==ar[k]){
                            count++;
                            ans=a;
                        }
                    }

                }
            }else{
                forup(j,0,4){
                    inpi(a);
                }
            }

        }
        switch(count){
            case 1:
                cout<<"Case #"<<cas+1<<": "<<ans;
                break;
            case 0:
                cout<<"Case #"<<cas+1<<": Volunteer cheated!";
                break;
            default:
                cout<<"Case #"<<cas+1<<": Bad magician!";
                break;
        }
        nl;
    }
}
