//Przmeysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;
const int N = 10004;

int t;
int n, X;
typedef multiset<int> S_;
S_ S;

int main()
{
    scanf("%d", &t);
    for(int ti = 1;ti <= t;ti++)
    {
       scanf("%d%d", &n, &X);
       for(int i = 1;i <= n;i++)
       {
           int a;
           scanf("%d", &a);
           S.insert(a);
       }
       int wyn = 0;
       while(!S.empty())
       {
           wyn++;

           S_::iterator it = S.end(); it--;
           int ost = *it;
           S.erase(it);

           if(S.empty()) continue;
           it = S.upper_bound(X-ost);
           if(it == S.begin()) continue;
           it--;
           S.erase(it);
       }

       printf("Case #%d: %d\n", ti, wyn);
    }
    return 0;
}
