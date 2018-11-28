//         /\_/\
//   _____/ o o \
//  /~____  =ø= /
// (______)__m_m)

#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <deque>
#include <set>
#include <map>
#include <utility>
#include <sstream>
#include <stack>
#include <queue>
#include <climits>
#include <limits>
#include <cstring>

#define pb push_back
#define pf push_front
#define all(c) c.begin(), c.end()
#define tr(c, it) \
for(typeof(c.begin()) it = c.begin(); it!=c.end(); ++it)
#define present(container, element) (find(all(container),element) != container.end())
#define present2(c,x) ((c).find(x) != (c).end()) // For maps and set

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const long double PI = 3.141592653589793238462643383;
const ll MOD = 1000000007;
const double EPS = 1e-9; // a==b is abs(a-b)<EPS, a>=b is a>b-EPS, a>b is a>=b+EPS
const int MAX_INT = 2147483647;

using namespace std;

int main()
{
    int T; cin>>T;
    for(int t=1; t<=T; ++t)
    {
        int ans1,ans2;
        vector<int> dummy(4);
        vector<int> vec1(4);
        vector<int> vec2(4);
        cin>>ans1;
        for(int i=1; i<5; ++i){
            if(i==ans1){
                for(int j=0; j<4; ++j){
                    cin>>vec1[j];
                }
            }
            else{
                for(int j=0; j<4; ++j){
                    cin>>dummy[j];
                }
            }
        }
        cin>>ans2;
        for(int i=1; i<5; ++i){
            if(i==ans2){
                for(int j=0; j<4; ++j){
                    cin>>vec2[j];
                }
            }
            else{
                for(int j=0; j<4; ++j){
                    cin>>dummy[j];
                }
            }
        }
        int matches = 0;
        int match;
        for(int i=0; i<4; ++i){
            for(int j=0; j<4; ++j){
                if(vec1[i]==vec2[j]){
                    matches++;
                    match = vec1[i];
                }
            }
        }
        if(matches==0){
            cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
        }
        else if(matches==1){
            cout<<"Case #"<<t<<": "<<match<<endl;
        }
        else{
            cout<<"Case #"<<t<<": Bad magician!"<<endl;
        }
    }
}