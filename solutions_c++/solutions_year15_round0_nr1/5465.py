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
typedef pair<ii,int>Query;
const int N=100005;
const ll INF=1e14;


int main(){
 freopen("test.in","r",stdin);
 freopen("test.out","w",stdout);
 //ios::sync_with_stdio(false);
 int t;
 cin>>t;
 for(int j=1;j<=t;j++){
    int n;
    string s;
    cin>>n>>s;
    int sum=0,add=0;
    for(int i=0;i<s.length();i++){
        int z=s[i]-'0';
        if(sum<i){
            add+=i-sum;
            sum=i;
        }
        sum+=z;
    }
    cout<<"Case #"<<j<<": "<<add<<endl;
 }
 return 0;
}
