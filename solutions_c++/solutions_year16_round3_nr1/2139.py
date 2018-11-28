#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>

using namespace std;

const int N = 30;
struct Node
{
    int num;
    char idx;
};

Node node[N];
int n, sum;

bool cmp(const Node & a, const Node & b)
{
    return a.num > b.num;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outL.txt", "w", stdout);
    int tcase;
    cin >> tcase;
    for(int k = 1; k <= tcase; ++ k) {
        cin >> n;
        sum = 0;
        for(int i = 0; i < n; ++ i) {
            cin >> node[i].num;
            node[i].idx = ('A' + i);
            sum += node[i].num;
        }
        printf("Case #%d:", k);
        while(sum > 2) {
            sort(node, node + n, cmp);
            if(node[0].num == node[1].num) {
                if(n == 2)
                {
                    cout << " " << node[0].idx << node[1].idx;
                    sum -= 2;
                    node[0].num --;
                    node[1].num --;
                }
                else {
                    if(node[0].num + node[1].num - 2 <= node[2].num) {
                        cout << " " << node[0].idx;
                        node[0].num --;
                        sum --;
                    }
                    else {
                        cout << " " << node[0].idx << node[1].idx;
                        sum -= 2;
                        node[0].num --;
                        node[1].num --;
                    }
                }
                continue;
            }
            cout << " " << node[0].idx;
            node[0].num --;
            sum --;
        }
        sort(node, node + n, cmp);
        //cout << " ---- "<< endl;
        cout << " " << node[0].idx << node[1].idx << endl;
    }

    return 0;
}
