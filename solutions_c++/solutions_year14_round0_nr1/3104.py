#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define foreach(u, o) \
    for (typeof((o).begin()) u = (o).begin(); u != (o).end(); ++u)
const int INF = 2147483647;
const double EPS = 1e-9;
const double pi = acos(-1);
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T mod(T a, T b) { return (a % b + b) % b; }
template <class T> int size(const T &x) { return x.size(); }

void intersect(set<int>& first, set<int>& second, set<int>& output)
{
    for(set<int>::iterator i = first.begin(); i != first.end(); ++i){
        if(second.count(*i)){ 
            output.insert(*i);
        }
    }
}

int main()
{
    int T;
    cin >> T;
    set<int> first, second, inter;
    int choice, card;

    for(int t = 0; t < T; ++t){
        printf("Case #%d: ", t+1);
        cin >> choice;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                cin >> card;
                if(i+1 == choice){
                    first.insert(card);
                }
            }
        }
        cin >> choice;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                cin >> card;
                if(i+1 == choice){
                    second.insert(card);
                }
            }
        }
        intersect(first, second, inter);
        if(inter.size() > 1){
            printf("Bad magician!\n");
        } else if(!inter.size()){
            printf("Volunteer cheated!\n");
        } else {
            printf("%d\n", *(inter.begin()));
        }
        first.clear(); second.clear(); inter.clear();
    }
}
