#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <climits>

#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <iterator>

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
#define INF 1e9
#define ll long long
#define ull unsigned long long


int main()
{
    //freopen("C:\\Users\\Sonia\\Documents\\CodeJam\\2015\\a.txt", "r", stdin);
    //freopen("C:\\Users\\Sonia\\Documents\\CodeJam\\2015\\b.txt", "w", stdout);
    int tc, res, sMax, sum;
    string str;
    scanf("%d", &tc);
    for(int t = 1; t <= tc; t++)
    {
        scanf("%d", &sMax);
        int arr[sMax+1];
        cin >> str;
        for(int i = 0; i <= sMax; i++)
        {
            arr[i] = str[i]-'0';
        }
        res = 0;
        sum = 0;
        if(arr[0] == 0)
        {
            res++;
            sum++;
        }
        else
        {
            sum += arr[0];
        }
        for(int i = 1; i <= sMax; i++)
        {
            if(arr[i] > 0 && sum < i)
            {
                int p = i - sum;
                sum += p;
                res += p;
            }
            sum += arr[i];
        }


        /*for(int i = 0; i <= sMax; i++)
        {
            cout << arr[i]<< endl;
        }*/

        printf("Case #%d: %d\n", t, res);
    }


    return 0;
}
