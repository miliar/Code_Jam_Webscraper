#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include<fstream>
#define ll long long
using namespace std;


int main () {
    freopen("B-small-attempt0.in", "r", stdin);
freopen("output.txt", "w", stdout);
    int t,h,n,m,flag=0;
    cin >> t;
    for(int k=0;k<t;k++){

        cin >> n>>m;
        vector<vector <int> > a;
        for(int i=0;i<n;i++){
            vector<int> aa(m,100);
            a.push_back(aa);

        }
        vector<vector <int> > vv;
        for(int i=0;i < n; i++){
            vector<int>v(m);
            for(int j=0;j < m;j++){
                cin >> v[j];
            }
            vv.push_back(v);
        }
        cout<<"Case #"<<k+1<<": ";
        for(int i = 0;i < n;i++){

            h = *max_element(vv[i].begin(),vv[i].end());
            for(int l = 0;l<m;l++){
                a[i][l] = h;
            }
        }
        flag = 0;
        for(int i=0;i < n; i++){
                for(int j = 0; j < m;j++){
                    if(a[i][j] != vv[i][j])
                    {
                        for(int l = 0;l < n;l++){
                            a[l][j] = vv[i][j];
                            if(a[l][j] < vv[l][j]){

                                flag=1;
                                break;
                            }
                        }

                    }

                }
                if(flag == 1){
                    cout<<"NO"<<endl;
                    break;
                }
        }
        if(flag == 0)
            cout<<"YES"<<endl;

    }
  return 0;
}
