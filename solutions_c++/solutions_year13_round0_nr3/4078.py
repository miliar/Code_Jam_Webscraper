#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#define max_n 9999999
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
#define pi acos(-1)

using namespace std;


typedef long long ll;
typedef vector <int > vi;
typedef pair<int,int> pii;
typedef vector <pii> vii;

int find(ll x,vector <ll> dumb){
        for(int i=0;i<dumb.size();i++)if(x<=dumb[i])return i;
        return 39;
}
int main(){
    ll dumb[] = { 1 ,2 ,3 ,11 ,22 ,101 ,111 ,121 ,202 ,212 ,1001 ,1111 ,2002 ,10001 ,10101 ,10201 ,11011 ,11111 ,11211 ,20002 ,20102 ,100001 ,101101 ,110011 ,111111 ,200002 ,1000001 ,1001001 ,1002001 ,1010101 ,1011101 ,1012101 ,1100011 ,1101011 ,1102011 ,1110111 ,1111111 ,2000002 ,2001002 };
    vector<ll> data(dumb,dumb+39);
    int T,up,low;
    ll x,y; 
    for(int i=0;i<data.size();i++)data[i]=data[i]*data[i];
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%lld%lld",&x,&y);
        low=find(x,data);
        up=find(y,data);
        if(data[up]==y)up++;
        printf("Case #%d: ",t);
        printf("%d\n",up-low); 
    }
    return 0;
}
