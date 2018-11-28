#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<sstream>
#include<algorithm>
#include<map>
#define f(i,n) for (int i=0;i<n;i++)
#define ff(i,a,n) for (int i=a;i<n;i++)
#define ll long long

using namespace std;

ll a,b;
ll dp[50]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,
111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};
int palindrome(ll num){
    string cad1,cad2;
    stringstream ss;
    ss<<num;
    ss>>cad1;
    cad2=cad1;
    reverse(cad2.begin(),cad2.end());
    if (cad1==cad2)return 1;
    else return 0;

}

ll solve(){

    ll cont=0;
    f(i,39){
        if (dp[i]*dp[i]>=a && dp[i]*dp[i]<=b) {
            cont++;
            
            //cout<<i<<endl;
        }
    }
    return cont;
}


int main(){
int t;
cin>>t;

f(ncase,t){
    cin>>a>>b;
    
    //cout<<"hola q hace"<<endl;
    printf("Case #%d: ",ncase+1);
    cout<<solve()<<endl;
    
    
    
    

}




return 0;}
