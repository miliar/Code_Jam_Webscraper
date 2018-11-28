#include <iostream>
#include<bits/stdc++.h>
using namespace std;
typedef vector <int> vi;
typedef vector <long long> vill;

#define sc(a) scanf("%d",&a)
#define scll(a) scanf("%I64d",&a)
#define pf(a) printf("%d\n",a)
#define pfll(a) printf("%I64d\n",a)
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define pb(a) push_back(a)
#define fore(i,a,b) for(i=a;i<=b;i++)

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long n,k,i,t,j,m,m1,cnt,indx;
    vi a(10);
    scll(t);

    fore(k,1,t){

        scll(n);
        if(n==0){
            printf("Case #%I64d: INSOMNIA\n",k);
            continue;
        }
        fore(i,0,9){
            a[i]=0;
        }
        cnt=0;
        j=1;
        while(true){
            m=n*j;
            m1=m;
            while(m1!=0){
                indx=m1%10;
                if(a[indx]==0){
                    a[indx]=1;
                    cnt++;
                }
                m1=m1/10;
            }
            if(cnt==10){
                printf("Case #%I64d: ",k);
                pfll(m);
                break;
            }
            j++;
        }
    }


    return 0;
}
