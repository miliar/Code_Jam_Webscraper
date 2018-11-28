#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<list>
#include<utility>
#include<string.h>
using namespace std;
bool pal(int n){
    bool cap = false;
    if(n>=0 && n<=9) cap=true;
    if(n>=11&& n<=99) cap = ( (n-n%10)/10 == n%10 );
    else if(n>=101 && n<1000){
         cap = ( (n-n%100)/100 == n%10 );
    }
    return cap;
}
int solve(int A,int B){
    int ans = 0, iq;
    for(int i=0;i*i<= B;i++)
        if(i*i>=A && pal(i) && pal(i*i))
            ans++;
    return ans;
}
int main(){

    freopen("c-small.in","r",stdin);
    freopen("c-small.out","w",stdout);

    int T, A, B, ans;
    scanf("%d", &T);
    for(int c=0;c<T;c++){
        scanf("%d %d",&A,&B);
        ans = solve(A,B);
        printf("Case #%d: %d\n",c+1,ans);
    }
    return 0;

}
