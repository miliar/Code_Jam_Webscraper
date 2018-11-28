#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <climits>
#include <vector>
#include <queue>
#include <cstring>
#include <iterator>
#include <list>
#include <set>
#include <map>
#include <bitset>

using namespace std;

typedef long long int LL;

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        char S[1005];
        scanf("%s", S);

        int n = strlen(S);
        list<char> mylist;
        mylist.push_back(S[0]);
        for(int i = 1; i < n; i++)
        {
            if(S[i] >= mylist.front())
                mylist.push_front(S[i]);
            else
                mylist.push_back(S[i]);
        }

        int j = 0;
        for(list<char>::iterator it = mylist.begin(); it != mylist.end(); ++it, ++j)
        {
            S[j] = *it;
        }
        printf("Case #%d: %s\n", t, S);
    }
}
