#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

#define frl(a, b, c) for( a = b; a < c; a++)
#define fru(a, b, c) for( a = b; a <= c; a++)
#define frd(a, b, c) for( a = b; a >= c; a--)
#define mst(a, b) memset(a, b, sizeof(a))



int main()
{
    int n, k, t;
    cin >> t;
    string str;
    long long ans = 0, sz;
    int last_pos = 0, i, j, test = 1;
    while(t--)
    {
        int flag = 0;
        last_pos = 0, ans = 0;
        cin >> str >> k;
        sz = str.size();
        int temp_cnt = 0;
        for(i = 0; i < sz; i++)
        {
            //cout << "For i = " << i ;
            if(str[i] != 'a' && str[i] != 'e' && str[i] != 'i' && str[i] != 'o' && str[i] != 'u')
                temp_cnt++;
            else
                temp_cnt = 0;
            //cout << " temp_cnt = " << temp_cnt << " " << "lsat_pos = " << last_pos;
            if(temp_cnt >= k){
                flag++;
                if(flag > 1)
                    ans += ((i - last_pos - k + 1) * (sz - i));
                else
                    ans += ((i - last_pos - k + 2 ) * (sz - i));
                last_pos = i - k + 1;
            }

            //cout << " ans = " << ans << endl;
        }
        cout << "Case #" << test++ << ": " << ans << endl;
    }

}












