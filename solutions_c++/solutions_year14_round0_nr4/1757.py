#include <bits/stdc++.h>

using namespace std;


int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, caseno = 0;
    scanf("%d", &t);
    while(t--)
    {
        deque<double> naomi, ken, n2, k2;
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
        {
            double x;
            scanf("%lf", &x);
            naomi.push_back(x);
        }
        for(int i = 0; i < n; i++)
        {
            double x;
            scanf("%lf", &x);
            ken.push_back(x);
        }
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        n2 = naomi;
        k2 = ken;
        int counter = 0;
        while(!naomi.empty())
        {
            if(naomi.back() > ken.back())
            {
                counter++;
                naomi.pop_back();
                ken.pop_front();
            }
            else
            {
                naomi.pop_back();
                ken.pop_back();
            }
        }
        int c2 = 0;
        while(!n2.empty())
        {
            if(n2.back() > k2.back())
            {
                c2++;
                for(int i = 0; i < (int)n2.size(); i++)
                {
                    if(n2[i] > k2.front())
                    {
                        n2.erase(n2.begin() + i);
                        k2.pop_front();
                        break;
                    }
                }
            }
            else if(n2.back() < k2.back())
            {
                n2.pop_front();
                k2.pop_back();
            }
        }
        printf("Case #%d: %d %d\n", ++caseno, c2, counter);

    }
    return 0;

}
