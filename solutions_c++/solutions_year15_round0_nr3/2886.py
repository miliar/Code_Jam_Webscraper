#include <cstdio>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <cstdlib>
#include <utility>
#include <bitset>
#include <deque>
#include <cmath>

using namespace std;

int main()
{
    char in[] = "C-small-attempt2.in";
    char out[] = "C-small-attempt2.out";
    freopen(in, "r", stdin);
    freopen(out, "w", stdout);
    unordered_map<char, int> val;
    val['i'] = 2, val['j']=3, val['k']=4;

    int mult[5][5] = {{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
    int T, X, L, caseNum=1;
    vector<int> orig, is;
    orig.reserve(10000);
    is.reserve(10000);

    scanf("%d", &T);
    while(T--)
    {
        int idx=0;
        orig.clear();
        is.clear();
        char c;
        int prod = 1;
        scanf("%d %d", &L, &X);
        getchar();
        for(int i=0; i<L; i++)
        {
            c = getchar();
            orig.push_back(val[c]);
            prod = (prod < 0) ? -mult[-prod][val[c]] : mult[prod][val[c]];
            if(prod == 2)
                is.push_back(idx);
            idx++;
        }

        if(prod == 1 or ((prod == -1 and X%2 == 0) or (prod != -1 and X%4 != 2)))
            printf("Case #%d: NO\n", caseNum++);
        else
        {
            int copyidx = 0;
            for(int i=L; i<L*X; i++)
            {
                orig.push_back(orig[copyidx]);
                prod = (prod < 0) ? -mult[-prod][orig[copyidx]] : mult[prod][orig[copyidx]];
                if(prod == 2)
                    is.push_back(idx);
                idx++;
                copyidx++;
            }

            bool found = false;
            for(auto i:is)
            {
                prod=1;
                for(int j=i+1; j<L*X; j++)
                {
                    prod = (prod < 0) ? -mult[-prod][orig[j]] : mult[prod][orig[j]];
                    if(prod == 3)
                    {
                        found = true;
                        break;
                    }
                }
            }
            if(found)
                printf("Case #%d: YES\n", caseNum++);
            else
                printf("Case #%d: NO\n", caseNum++);
        }
    }
    return 0;
}

