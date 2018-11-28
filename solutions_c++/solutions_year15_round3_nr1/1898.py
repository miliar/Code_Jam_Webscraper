#include <bits/stdc++.h>

using namespace std;

template<typename T>
ostream& operator << (ostream& o, vector<T>& v)
{
    o << "[";
    for(size_t i = 0; i < v.size(); i++)
    {
        o << v[i];
        if(i != v.size() - 1)
            o << ", ";
    }
    o << "]";
    return o;
}

int main(int argc, char* argv[])
{
    (void)argc; (void)argv;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int n_casi;
    cin >> n_casi;
    for(int caso = 1; caso <= n_casi; caso++)
    {
        int r, c, w;
        cin >> r;
        cin >> c;
        cin >> w;
        int sol = 0;
        int search_part = 0;
        search_part = (c/w) + ((c%w != 0) ? (1) : (0));
        int aff_part = w-1;
        cout << "Case #" << caso << ": " << search_part * r + aff_part << endl;
    }
    return EXIT_SUCCESS;
}
