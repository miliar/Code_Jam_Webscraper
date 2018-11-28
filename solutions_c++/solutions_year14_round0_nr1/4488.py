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

typedef int ttyp;
#define forz(n) for(int i=0;i<n;i++)
#define forzo(j,n) for(int j=0;j<n;j++)
#define MP make_pair
#define sz(v) v.size()



void doit(){
    int a, b, ret;
    bool found = false;
    int va[4][4], vb[4][4];
    cin>>a;
    forz(4)
    forzo(j,4)
        cin>>va[i][j];
    cin>>b;
    forz(4)
    forzo(j,4)
        cin>>vb[i][j];
    a--, b--;
    forz(4)
    forzo(j,4)
    if(va[a][i]==vb[b][j]){
        if(!found){
            found=true;
            ret = va[a][i];
        }
        else{
            cout<<"Bad magician!"<<endl;
            return;
        }
    }
    if(found){
        cout<<ret<<endl;
    }
    else{
        cout<<"Volunteer cheated!"<<endl;
    }
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

