#include<iostream>
#include<cstdio>
#include<map>
#include<set>

using namespace std;

int first, second;
int num1;
int num2;
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt","w", stdout);
    int T;
    int cases = 0;
    cin >> T;
    while(T--)
    {
        set<int>mp;
        cin >> first;
        int ansCnt = 0;
        int ans = 0;
        for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; ++j)
        {
            cin >> num1;
            if(i == first - 1)
            {
                mp.insert(num1);
            }

        }
        cin >> second;
        for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; ++j)
        {
            cin >> num2;
            if(i == second - 1 && mp.count(num2) > 0) {++ansCnt; ans = num2;}
        }
        if(ansCnt == 1)
        {
            cout << "Case #"<< ++cases << ": " << ans << endl;
        }
        else if(ans == 0)
        {
            cout << "Case #"<< ++cases << ": " << "Volunteer cheated!" << endl;
        }
        else cout << "Case #"<< ++cases << ": " << "Bad magician!" << endl;

    }
    return 0;
}
