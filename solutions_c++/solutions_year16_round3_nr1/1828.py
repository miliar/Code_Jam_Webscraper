

//#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <cmath>
#include <iomanip>
#include <queue>

using namespace std;


int main(){
    //freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int k = 0; k < t; ++k){
        int n;
        cin >> n;
        vector <pair <int, char> > v;
        for (int i = 0; i < n; ++i){
            int f;
            cin >> f;
            char c = 'A'+i;
            v.push_back(make_pair(f, c));
        }
        sort(v.begin(), v.end());
        cout << "Case #" << k+1 << ": ";
        int h = v[0].first;
        bool pr = 0;
        while (!pr){
            pr = 1;
            for (int i = n-1; i > 0;){
                if (v[i].first == h)
                    break;
                if (i > 1 && v[i-1].first > h){
                    v[i].first--;
                    v[i-1].first--;
                    cout << v[i].second << v[i-1].second << ' ';
                    if (v[i].first>h)
                        pr = 0;
                    i = i-2;
                }
                else if (v[i].first - 2 >= h){
                    v[i].first--;
                    v[i].first--;
                    cout << v[i].second << v[i].second << ' ';
                    if (v[i].first>h)
                        pr = 0;
                    i = i-2;
                }
                else {
                    v[i].first--;
                    cout << v[i].second << ' ';
                    if (v[i].first>h)
                        pr = 0;
                    i = i-1;
                }
            }
        }
        
        if (n%2 == 1){
            n = n-1;
            int g = h;
            while (g > 0){
                if (g > 1){
                    g-=2;
                    cout << v[n].second << v[n].second << ' ';
                }
                else {
                    g--;
                    cout << v[n].second << ' ';
                }
            }
        }
        while (h>0){
              h--;
              for (int i = 0; i < n; i = i+2){
                  cout << v[i].second << v[i+1].second << ' ';
              }
        }
        cout << endl;
    }



    return 0;
    
}