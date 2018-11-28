#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <set>
#include <map>

using namespace std;

int GCD(int a, int b)
{
    if (b == 0) return a;
    return GCD(b, a%b);
}

struct F
{
    int p, q, g, b;

    const pair<int, int> key() const { return std::make_pair(p, q); }

    void gcd()
    {
        int t = GCD(p, q);
        this->p /= t;
        this->q /= t;
    }

    bool isOO() const { return this->p == 1 && this->q == 1; }

    const double v() const { return (double)p / q; }

    bool operator < (const F& f) const
    {
        return this->v() < f.v();
    }
};

int main()
{
    int T, ans = 0;
    int p, q;
    cin >> T;


    vector<F> f;
    map<pair<int, int>, int> best;

   

    for (int i = 0; i < 10; i++)
    {

        F f0;
        f0.p = 1;
        f0.q = 1;
        f0.g = i;

        F f1;
        f1.p = 0;
        f1.q = 1;
        f1.g = 41;

        f.push_back(f0);
        f.push_back(f1);

        best[f0.key()] = 0;
        best[f1.key()] = 0;
    }

    for (int i = 0; i < 11; i++)
    {
        vector<F> list;

        for (size_t a = 0; a < f.size(); a++)
        for (size_t b = 0; b < f.size(); b++)
        {
            const auto& fa = f[a];
            const auto& fb = f[b];                     

            F temp;
            temp.q = fa.q * fb.q * 2;
            temp.p = (fa.p * fb.q + fa.q*fb.p);
            temp.g = std::min(fa.g, fb.g) + 1;
            temp.gcd();

            if (best.count(temp.key()) == 0 || best[temp.key()] > temp.g)
            {                
                best[temp.key()] = temp.g;

                if (temp.q < 8)
                    cerr << temp.p << "/" << temp.q << " = " << temp.g << endl;

                list.push_back(temp);
            }
        }

        f.insert(f.end(), list.begin(), list.end());
    }

    char ch;
    for (int c = 1; c <= T; c++)
    {
        cin >> p >> ch >> q;
        cout << "Case #" << c << ": ";
        auto key = make_pair(p, q);
        if (best.count(key)) cout<<best[key] << endl;
        else cout << "impossible" << endl;
    }
    return 0;
}

//int main()
//{
//    int T,ans = 0;
//    cin >> T;
//    for (int c = 1; c <= T; c++)
//    {
//        cout << "Case #" << c << ": " << ans << endl;
//    }
//    return 0;
//}

