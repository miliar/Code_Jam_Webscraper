#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <cstring>

using namespace std;

typedef pair<int,int> PII;
int t,n,m,k;
int f[11],hash[1025];
int  a[10010];
string ans[110000];
map<PII,string> g;
int bo;
vector<int> e[10];
int stack[110000];
int mask[1100000];


int main(){
    freopen("A-large (2).in","r",stdin);
    freopen("1.out","w",stdout);
    cin >> t;
    for (int ti=1;ti<=t;ti++){
        scanf("%d%d",&n,&m);
        cout << "Case #"<<ti<<": ";
        for (int i=0;i<n;i++) scanf("%d",&a[i]);
        sort(a,a+n);
        int qh=0,qt=n-1;
        int tot=0;
        while (qh<=qt){
              if (qt==qh){
                 tot++;
                 break;
              }
              if (a[qt]+a[qh]<=m){
                 tot++;
                 qh++;
                 qt--;
              }else{
                    tot++;
                    qt--;
              }
        }
        cout<<tot<<endl;
    }
    //system("pause");
    return 0;
}
