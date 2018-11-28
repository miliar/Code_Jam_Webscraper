#include <assert.h>
#include <cstring>
#include <iostream>
#include <fstream>
#include <climits>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
using namespace std;

const int MAX = 1005;

struct node
{
    int value;
    int position;
    bool operator < (const node &nb)
    {
        return value > nb.value;
    }
};

node p[MAX];
int po[MAX];


int main() {
    
    int cases;
    cin >> cases;

    for (int t = 1; t <= cases; t++)
    {
        int res = 0;
        int n = 1000;
        cin>>n;
        for(int i = 0; i < n; i++)
        {
            cin>>p[i].value;
            p[i].position = i;
            po[i] = 0;
        }
        
        sort(p, p + n);

        for(int i = 0; i < n; i++)
        {
            node temp = p[i];
            int move = po[temp.position];
            temp.position -= move;
            if(temp.position  > (n-1 - i) - temp.position)
            {
                res += ( n - 1  - i) - temp.position;
            }
            else
            {
                res += temp.position;
            }
            for(int j = temp.position + move + 1; j <= n-1; j++)
            {
                po[j]++;
            }
        }
        
        printf("Case #%d: %d\n", t, res);
    }
    
    return 0;
}
