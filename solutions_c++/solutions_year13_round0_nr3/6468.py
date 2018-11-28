#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
using namespace std;

int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int a[1005];
    memset(a,0,sizeof(a));
    a[0] = 0;
    a[1] = 1;
    a[4] = 2;
    a[9] = 3;
    a[121] = 4;
    a[484] = 5;

    int ans = 1;
    for(int i = 1 ; i < 1005; i++){
        if(a[i] == 0) a[i] = ans;
        else{
            ans = a[i];
        }
    }
    int t;
    cin >> t;
    int M = 1;
    while(t--){
        int m ,n;
        cin >> m>> n;
        //cout << m <<' '<< n;
        cout << "Case #"<<M++<<": "<<a[n] - a[m-1] <<endl;
    }

	return 0;
}
