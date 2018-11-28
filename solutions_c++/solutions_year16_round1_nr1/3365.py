#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <iterator>
#include <map>
#include <cstring>
#include <climits>
#include <time.h>

using namespace std;

#define READ() 	freopen("in.txt","r",stdin)
#define WRITE() freopen("out.txt","w",stdout)
#define sf(n) 	scanf("%d",&n)
#define lsf(n) 	scanf("%lld", &n)
#define pb(n) 	push_back(n)
#define EPS 	1e-10
#define NL 		printf("\n")
#define INF     INT_MAX
#define MAX     INT_MAX
#define MOD     1000000007
#define LL      long long


int main()
{
    READ();
    WRITE();


    int t;
    cin >> t;

    int TC = 0;

    while(t--)
    {
        string s;
        cin >> s;

        deque <char> dq;

        dq.push_back(s[0]);

        for(int i=1;i<s.size();i++)
        {
            char c = s[i];

            if(c >= dq.front())dq.push_front(c);
            else dq.push_back(c);
        }

        cout << "Case #" << ++TC << ": ";

        while(!dq.empty())
        {
            cout << dq.front() ;
            dq.pop_front();
        }

        cout << endl;


    }



//    cin >> s;





    return 0;
}

