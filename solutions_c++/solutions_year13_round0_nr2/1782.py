#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>

using namespace std;
int a[105][105];
void doit(){
    int n, m;
    bool rok,cok;
    memset(a,0,sizeof(a));
    cin>>n>>m;
    for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin>>a[i][j];
    for(int i=0;i<n;i++) for(int j=0;j<m;j++){
        rok=true;cok=true;
        for(int k=0;k<n;k++)if(a[k][j]>a[i][j])rok=false;
        for(int k=0;k<m;k++)if(a[i][k]>a[i][j])cok=false;
        if(!rok && !cok){cout<<"NO"<<endl;return;}
    }
    cout<<"YES"<<endl;
    return;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
      cout<<"Case #"<<i<<": ";
      doit();
    }
    return 0;
}

