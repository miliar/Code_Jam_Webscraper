#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>

using namespace std;

int get_war(set< double > naomi, set< double > ken)
{
    int n_score = 0;
    while (!naomi.empty())
    {
        double n_move = *naomi.rbegin();
        naomi.erase(n_move);
        
        if (*ken.rbegin() < n_move) { // can't beat
            ken.erase(*ken.begin());
            n_score++;
        } else {
            set< double >::iterator it = lower_bound(ken.begin(), ken.end(), n_move);
            ken.erase(*it);
        }
        
    }
    return n_score;
}

int get_cheat_war(set< double > naomi, set< double > ken)
{
    int n_score = 0;
    while (!naomi.empty())
    {
        double n_move = *naomi.begin();
        naomi.erase(n_move);
        if (*ken.begin() < n_move) { // can't beat
            ken.erase(*ken.begin());
            n_score++;
        } else {
            ken.erase(*ken.rbegin());
        }
    }
    return n_score;
}

void solve(int test_num)
{
    int n;
    set< double > naomi, ken;
    cin >> n;
    for (int i = 0; i < n; i++) {
        double x;
        cin >> x;
        naomi.insert(x);
    }
    for (int i = 0; i < n; i++) {
        double x;
        cin >> x;
        ken.insert(x);
    }
    printf("Case #%d: %d %d\n", test_num + 1, get_cheat_war(naomi, ken), get_war(naomi, ken));
    
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
        solve(i);
}