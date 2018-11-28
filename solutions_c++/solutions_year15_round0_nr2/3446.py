
//  main.cpp
//  Practice
//  Copyright (c) 2014 Tapan. All rights reserved.
#include<stdio.h>
#include<iostream>
#include<vector>
#include<string.h>
#include<algorithm>
#include<deque>
#include<map>
#include<set>
#include<stdlib.h>
#include<math.h>
#include<queue>
#include<stack>
#include<functional>
using namespace std;
#define ll long long
#define si(x) scanf("%d",&x)
#define sc(x) scanf("%c",&x)
#define sl(x) scanf("%I64d",&x)
#define prl(x) printf("%I64d",x)
#define pri(x) printf("%d\n",x)
#define prs(x) printf("%s\n",x)
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
#define vl vector<ll>
#define vi vector<int>
#define vii vector<ii>
#define vvl vector< vl >
#define vvi vector< vi >
#define vvii vector< vii >
#define pb push_back
#define maX(a,b) ((a)>(b)?a:b)
#define miN(a,b) ((a)<(b)?a:b)
#define mem(x,y) memset(x,y,sizeof(x))
#define f(i,a,b) for(int i=(a);i<(b);i++)
#define max_int_value 2147483647
#define max_long_value 9223372036854775807
#define mod 1000000007
#define pb push_back
#define MAX 10011


int A[MAX];

int main(int argc, const char * argv[]){
    ios_base::sync_with_stdio(false);
    int t,i,j,Test_Num;
    cin >> t;
    for(Test_Num=1;Test_Num<=t;Test_Num++){
        int d;
        cin >> d;
        for(i=0;i<d;i++){
            A[i]=0;
        }
        for(i=0;i<d;i++)
            cin >> A[i];
        int ans,ans1=0;
        for(i=1;i<=1000;i++){
            ans=i;
            for(j=0;j<d;j++){
                if(A[j]>i){
                    if(A[j]%i==0)
                        ans=ans + (A[j]/i-1);
                    else
                        ans=ans + (A[j]/i);
                }
            }
            if(i==1)
                ans1=ans;
            else{
                ans1=min(ans1,ans);
            }
        }
        cout<<"Case #"<<Test_Num<<": "<<ans1<<endl;
    }
    return 0;
}
