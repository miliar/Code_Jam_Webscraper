#include <stdio.h>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

#define sf scanf
#define pf printf
#define maxm 10000000+10
#define Long unsigned long long int

void save();
Long palindrome(Long n);
void ultimatepal();

Long sqnum[maxm];
Long pal[maxm],pal6[maxm];

struct joma{
    Long sq,n;
}T[maxm];

Long limit=10000000;


int main(){

    #ifdef localhost
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);
    #endif

     save();
     ultimatepal();

    Long cases,i,j,k,a,b,paldom,ans,lena,lenb,temp,id,vut;
    sf("%lld",&cases);
    for(i=1;i<=cases;i++){
        ans=0;

        sf("%lld %lld",&a,&b);
        lenb=sqrt(b);
        for(k=a;k<=b;k++){
            vut=sqrt(k);
            if(vut*vut==k){lena=vut; break;}
        }
        for(j=lena;j<=lenb;j++){
            paldom = T[j].sq;
            if(paldom==sqnum[j]){
                paldom= T[j].n;
                if(j==paldom) ans++;
            }
        }


        pf("Case #%lld: %lld\n",i,ans);
    }


    return 0;
}


void save(){
    Long i,k,j,m=0;
    k=limit*limit;
    for(i=1;i<=limit;i++){
        j=i*i;
        if(j<=k) sqnum[i]=j;
        else break;
    }


}


Long palindrome(Long n){

    Long i,j,k,number=0;
    while(n>0){
        i=n%10;
        number=(number*10)+i;
        n/=10;
    }

    return number;
}

void ultimatepal(){
    Long i;
    for(i=1;i<=limit;i++){
        T[i].sq=palindrome(sqnum[i]);
        T[i].n=palindrome(i);
    }
}



