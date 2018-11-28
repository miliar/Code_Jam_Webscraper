#include <iostream>
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string.h>
#include <queue>
#define st first
#define sz second
using namespace std;
typedef unsigned long long ll;
typedef pair<int,int>ii;
const int N=100005;
const ll INF=1e14;

int main(){
 freopen("test.in","r",stdin);
 freopen("test.out","w",stdout);
 //ios::sync_with_stdio(false);
  int t,a[100005];
  scanf("%d",&t);
  for(int i=1;i<=t;i++){
    int d,mn=100005,cur=0,mx=0;
    scanf("%d",&d);
    for(int j=0;j<d;j++)
        scanf("%d",&a[j]);
    for(int j=1;j<1001;j++){
        int sum=j;
        for(int k=0;k<d;k++){
            if(a[k]<=j)continue;
            sum+=(a[k]+j-1)/j;
            sum--;
        }
        mn=min(mn,sum);
    }
    cout<<"Case #"<<i<<": "<<mn<<endl;
  }
 return 0;
}
