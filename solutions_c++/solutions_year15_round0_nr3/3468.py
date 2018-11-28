#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

void prologue()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    FILE *fp = freopen("/Users/-RooneY-/Desktop/src/input", "r", stdin);
    assert(fp);
    
    FILE *fpw = freopen("/Users/-RooneY-/Desktop/src/output", "w", stdout);
    assert(fpw);
}

const int MAX = 10005;
int is_k[MAX];

int main()
{
    prologue();
    
    int t;
    cin >> t;
    
    int prod_abs[4][4] = { {0, 1, 2, 3}, {1, 0, 3, 2}, {2, 3, 0, 1}, {3, 2, 1, 0}};
    int prod_sign[4][4] = { {1, 1, 1, 1}, {1, -1, 1, -1}, {1, -1, -1, 1}, {1, 1, -1, -1}};
    
    for (int test = 1; test <= t; ++test)
    {
        int _l, x;
        string lstr;
        
        cin >> _l >> x;
        cin >> lstr;
        
        vector<int> L;
        
        for (int i = 0; i < x; ++i)
        {
            for (char c : lstr)
            {
                int d = c - 'i' + 1;
                assert(d >= 1 && d <= 3);
                L.push_back(d);
            }
        }
        
        int l = (int)L.size();
        
        for (int i = 0; i < l; ++i)
        {
            int abs = 0, sign = 1;
            for (int p = i; p < l; ++p)
            {
                sign *= prod_sign[abs][L[p]];
                abs = prod_abs[abs][L[p]];
            }
            
            is_k[i] = (abs == 3 && sign == 1) ? 1 : 0;
        }

        bool found = false;

        int abs1 = 0, sign1 = 1;
        for (int p1 = 0; p1 < l-2; ++p1)
        {
            sign1 *= prod_sign[abs1][L[p1]];
            abs1 = prod_abs[abs1][L[p1]];
            
            if (abs1 == 1 && sign1 == 1) // found i
            {
                int abs2 = 0, sign2 = 1;
                for (int p2 = p1 + 1; p2 < l-1; ++p2)
                {
                    sign2 *= prod_sign[abs2][L[p2]];
                    abs2 = prod_abs[abs2][L[p2]];
                    
                    if (abs2 == 2 && sign2 == 1) // found j
                    {
                        if (p2 + 1 < l && is_k[p2 + 1]) // found k
                        {
                            found = true;
                            break;
                        }
                    }
                }
            }
            
            if (found)
                break;
        }
        
        cout << "Case #" << test << ": " << (found ? "YES":"NO") << endl;
    }
    
    return 0;
}