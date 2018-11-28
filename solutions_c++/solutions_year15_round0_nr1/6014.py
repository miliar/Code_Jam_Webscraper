#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        int smax, person_count;
        cin >> smax;
        string shy_level;
        cin >> shy_level;
        int COUNT= 0;
        int final_result = 0;
        for(int i = 0; shy_level[i] !='\0'; i++)
        {
            person_count = shy_level[i] - '0';

            if(COUNT < i)
            {
                final_result = final_result + (i - COUNT);
                COUNT = COUNT + (i - COUNT) ;
            }
            COUNT += person_count;
        }
        cout << "Case #" <<t<<": "<<final_result<<"\n";
    }
}
