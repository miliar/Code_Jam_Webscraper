#include <set>
#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int x, p, q, T, ns, ps, temp;
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        set<int> Q;
        cin >> q;
        for(int i = 1; i <= 4; i++)
        for(int j = 1; j <= 4; j++)
        {
            cin >> x;
            if(i == q) {
                ps = Q.size();
                Q.insert(x);
                ns = Q.size();
                if(ps == ns) temp = x;
            }
        }
        cin >> p;
        for(int i = 1; i <= 4; i++)
        for(int j = 1; j <= 4; j++)
        {
            cin >> x;
            if(i == p){
                ps = Q.size();
                Q.insert(x);
                ns = Q.size();
                if(ps == ns) temp = x;
            }
        }
        cout << "Case #" << t << ": ";
        if(Q.size() == 8) cout << "Volunteer cheated!" << endl;
        else if(Q.size() == 7) cout << temp << endl;
        else cout << "Bad magician!" << endl;
    }
    return 0;
}
