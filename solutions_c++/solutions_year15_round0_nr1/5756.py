#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <cassert>
#include <stack>
#include <complex>
#include <utility>
#include <cstdio>

#define NODES 200002


#define MAX 200002

using namespace std;


int max(int a,int b)
{
    return a>b?a:b;
}

int main() {
    int cases; cin >> cases;
    for(int i=1; i<=cases; i++)
    {
        int max_shyness; cin >> max_shyness;
        string shyness_index; cin >> shyness_index;
        
        int answer = 0;
        int persons = 0;
        for(int i=0; i<=max_shyness; i++)
        {
            answer = max(i-persons,answer);
            persons += (shyness_index[i]-'0');
        }
        cout << "Case #" << i << ": " << answer << endl;
    }
}