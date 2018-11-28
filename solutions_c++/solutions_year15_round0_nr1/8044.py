#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;
    for(int i = 0; i < T ; i++)
    {

    int smax;
    cin >> smax;

    string shylist;
    cin >> shylist;

    int standup = 0;
    int needed = 0;

    for(int shyi = 0; shyi < smax + 1 ; shyi++)
    {
        int diff = shyi - standup;
        if(standup < shyi)
        {
            //shylist[shyi - 1] = shylist[shyi - 1] + diff;
            needed += diff;
            standup += diff;
        }
        standup += shylist[shyi] - '0';
        //cout << shyi << " " << standup << " " << needed << endl;
    }

    cout << "Case #" << i+1 << ": " << needed << endl;
    }
}
