#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<vector>
#include<memory.h>
#include<cassert>
#define lint long long
#define rep(i,a,b) for(int i=a; i<b; i++)
#define p_b(V,x) V.push_back(x)
#define sc(x) scanf("%d", &x)
#define mod 1000000007
#define maxn 1000005
using namespace std;
int main(){
    int t;
    int k=1;
    sc(t);
    while(t--){
        int n;
        sc(n);
        int sum=0;
        int A[n];
        rep(i,0,n){
            sc(A[i]);
            sum+=A[i];
        }
        int B[1001];
        if(sum==0){
            cout<<"Case #"<<k<<" : "<<0<<endl;
            k++;
            continue;
        }
        memset(B,0,sizeof B);
        rep(i,1,1001){
            rep(j,0,n){
                int temp=A[j]/i;
                if(temp*i!=A[j])temp++;
                temp--;
                B[i]+=temp;
            }
            B[i]+=i;
        }
        int mn=1000000000;
        rep(i,1,1001){
            if(B[i]<mn && B[i]>0)mn=B[i];
        }
        cout<<"Case #"<<k<<" : "<<mn<<endl;
        k++;
    }
}
