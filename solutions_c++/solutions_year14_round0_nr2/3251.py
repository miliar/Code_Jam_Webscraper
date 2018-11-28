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
int a[26];
double dn,dm,dk,time,dc;

int main(){
    cin>>t;
    for(i=0;i<t;i++){
        cin>>dn>>dm>>dk;
        time=0;dc=2;
        while(dk/dc > dn/dc + dk/(dc+dm)){
            time+=dn/dc;
            dc+=dm;
        }
        time+=dk/dc;
        printf("Case #%d: %.7lf\n",i+1,time);
    }
    return 0;
}

/*
5
1 0 -1 0 0
0 1 0 -1 -2
*/
