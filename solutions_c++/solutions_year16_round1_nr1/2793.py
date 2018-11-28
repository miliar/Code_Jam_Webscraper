#include <vector>
#include <deque>
#include <set>
#include <map>
#include <iostream>
#include <string>
#include <sstream>

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

int main()
{
    LL T; cin>>T;
    for(LL t=0; t<T; t++)
    {
        string N; cin>>N;

        deque<char> ans;
        ans.push_back(N[0]);

        for(int i=1; i<N.size(); i++) {
            if(N[i]>=ans[0]) {
                ans.push_front(N[i]);
            } else {
                ans.push_back(N[i]);
            }
        }

        cout << "Case #" << t+1 << ": ";
        for(int i=0; i<ans.size(); i++)
            cout << ans[i];
        cout << endl;
    }

    return 0;
}

