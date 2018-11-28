#include <bits/stdc++.h>
using namespace std;

int t;

char wcz[1000007];

vector <char> wek;
int wyn;

int main()
{
    scanf("%d", &t);
    for (int tt=1; tt<=t; tt++)
    {
        printf("Case #%d: ", tt);
        wyn=0;
        wek.clear();
        scanf("%s", wcz+1);
        for (int i=1; wcz[i]; i++)
        {
            wek.push_back(wcz[i]);
            if (wek.size()>1 && wek[wek.size()-1]==wek[wek.size()-2])
            {
                wyn+=10;
                wek.pop_back();
                wek.pop_back();
            }
        }
        wyn+=5*(wek.size()/2);
        printf("%d\n", wyn);
    }
    return 0;
}
