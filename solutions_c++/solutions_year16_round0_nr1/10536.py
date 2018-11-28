#include <math.h>
#include <time.h>
#include <ctype.h>
#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;
#define sp system("pause")
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) FOR(i,0,(int)n-1)
#define DB(format,...) fprintf(stderr,format, ##__VA_ARGS__)
#define pb(x) push_back(x)
#define mp(a,b) make_pair(a,b)
#define MS0(x) memset(x,0,sizeof(x))
#define MS1(x) memset(x,1,sizeof(x))
#define SORT(a,n) sort(begin(a),begin(a)+n)
#define REV(a,n) reverse(begin(a),begin(a)+n)
#define ll long long
#define pii pair<int,int>
#define vec vector<int>

int main(){
long long int i,j,k=1,n,flag,flag1,t,temp,temp2;
cin>>t;
j=1;
while(j<=t){
    cin>>n;

    if(n==0)
    {
        cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
        j++;
        continue;}

    long long int h[20]={0};
    flag1=1;
    temp=n;
    temp2=n;
    k=1;
    while(flag1==1){
        flag=0;

        while(n>0){
            h[n%10]=1;
            n=n/10;
            //cout<<"KK";
        }
        //cout<<temp;
        for(i=0;i<10;i++){
            if(h[i]==1)
                flag++;
        }
        if(flag==10){
            cout<<"Case #"<<j<<": "<<temp<<endl;
            flag1=0;

        }
        k++;
        temp=temp2*k;
        n=temp;

    }
    j++;
}
return 0;
}
