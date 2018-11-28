#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <math.h>
#include <vector>
using namespace std;
typedef long long LL;


int main()
{
    int tries;
    int C,K,S;
    FILE *fin = freopen("D-small.in", "r", stdin);
    assert(fin!=NULL );
    FILE *fout = freopen("D-small.out", "w", stdout);
    cin >> tries;
    for (int i = 1; i <= tries; i++)
    {
        cin >> K;
        cin >> C;
        cin >> S;
        vector<int> data_pts;
        if(C==1){
            if(S>=K){
                cout << "Case #" << i << ": ";
                for(int j=1;j<=K;j++){
                    data_pts.push_back(j);
                }
                if(data_pts.size()==0){
                    cout << "IMPOSSIBLE" << endl;
                }
                else{
                    for (int l = 0; l < data_pts.size(); l++)
                        cout << data_pts[l] << " ";
                    cout << endl;
                }
            }
        }
        else{
            int x = ceil(K/2.0);
            int p = K;
            if (S >= x)
            {
                for (int l = 0; l < x; l++)
                {
                    data_pts.push_back(p);
                    p += (K-1);
                }
            }
            cout << "Case #" << i << ": ";
            if(data_pts.size()==0){
                    cout << "IMPOSSIBLE" << endl;
            }
            else{
                for (int l = 0; l < data_pts.size(); l++)
                    cout << data_pts[l] << " ";
                cout << endl;
            }
        }
    }
    return 0;

}
