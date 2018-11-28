#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctype.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <deque>
#include <sstream>
using namespace std;
#define ot(x) cout<<x<<endl
#define cen cout<<endl
#define EPS 1e-10
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
vector<vii> AdjList;
priority_queue< pair<int, ii> > Edgelist;
int n,m,i,t,j,k,l;
double a[6000],b[6000];
double dn,dm,dk,time,dc;

int main(){
    cin>>t;
    for(i=0;i<t;i++){
        cin>>n;
        memset(a,0,sizeof a);
        memset(b,0,sizeof b);

        for(int ii=0;ii<n;ii++){
            scanf("%lf",&a[ii]);
        }
        for(int ii=0;ii<n;ii++){
            scanf("%lf",&b[ii]);
        }
        sort(a,a+n);
        sort(b,b+n);
//        ot("<<<< "<<j);
        l=0;k=0;
        while(l!=n){
            if(a[k]<b[l]){
                k++;
                l++;
            }else{
                l++;
            }
        }
        j=k;
        l=n-1;k=n-1;
        while(l!=-1){
            if(a[k]>b[l]){
                k--;
                l--;
            }else{
                l--;
            }
        }
//        ot(j<<" "<<k);
//        for(int ii=0;ii<n;ii++){
//            printf("%lf ",a[ii]);
//        }
//        cen;
//        for(int ii=0;ii<n;ii++){
//            printf("%lf ",b[ii]);
//        }
//        cen;
        printf("Case #%d: %d %d\n",i+1,n-k-1,n-j);
    }
    return 0;
}

/*
5
1 0 -1 0 0
0 1 0 -1 -2
*/
