#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int casos, maxV, people, peopleNeeded, ans, tmp;
    string str;

    scanf("%d", &casos);

    for(int i=1; i<=casos; i++)
    {
        cin>>maxV>>str;
        people = peopleNeeded = ans = 0;

        for(int x=0; x<str.size(); x++)
        {
            peopleNeeded = x;

            if(peopleNeeded > people)
            {
                tmp = peopleNeeded - people;
                ans += tmp;
                people+= tmp;
                people+=(str[x] - '0');
            }
            else
            {
                people = people + (str[x] - '0');
            }
        }

        printf("Case #%d: %d\n", i, ans);
    }
return 0;
}
