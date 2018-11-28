#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<vector>
#include<utility>
#include<cstring>
#include<fstream>

#define pb push_back
#define po pop_back
#define fs first
#define sc second
#define INF 999999999

using namespace std;
int n,i,j;
long long a;


bool check(int v[]){
    for(int i=0;i<10;i++)
        if(v[i]<1)
            return false;
    return true;
}

long long make(long long x){
    int v[10] = {0};
    long long initialX=x;
    long long cx;
    while(!check(v)){
        cx=x;
        while(cx>0){
            v[cx%10]++;
            cx/=10;
        }
        x+=initialX;
    }
    return x-initialX;
}

int main(){
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);
    cin.sync_with_stdio(false);
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>a;
        if(a==0)
            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        else cout<<"Case #"<<i+1<<": "<<make(a)<<endl;
    }


    return 0;
}
