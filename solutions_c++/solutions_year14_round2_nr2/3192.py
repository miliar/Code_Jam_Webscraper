#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <list>
#include <ctime>
#include <vector>
#include <fstream>
#include <algorithm>
#include <iomanip>
#define  epsilon 1e-5
#include <list>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <set>
#include <bitset>
#include <cassert>
using namespace std;


int main()
{
    ofstream out("out.txt");
    int tt;
    cin >> tt;
    for(int j = 0; j < tt; j++)
    {
        int a, b, k;
        cin >> a >> b >> k;
        int cnt = 0;
        for(int i = 0; i < a; i++)
        {
            for(int m = 0; m < b; m++)
            {
                int minn = (i & m);

                if(minn < k){  cnt++;}
            }
        }

        out << "Case #" << j + 1 << ": " << cnt << endl;
    }
}
