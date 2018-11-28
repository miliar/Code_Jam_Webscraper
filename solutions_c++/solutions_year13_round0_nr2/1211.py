#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <istream>
#include <algorithm>
#include <queue>
#include <cmath>
#include <map>
#include <list>
#include <cstdio>
#include <set>
#include <iomanip>
#include <stack>
#include <ctime>
#include <climits>
#include <iterator>
#define LOCAL
#ifdef ONLINE_JUDGE
#define COUT(s)
#undef LOCAL
#endif
#ifdef LOCAL
#define cin in
#define cout out
#define COUT(s) cout<<"-----"<<s<<"-----"<<endl;
#endif

using namespace std;



int main(int argc,char **argv)
{
#ifdef LOCAL
    ifstream in("input.txt");
    ofstream out("output.txt");
#endif
    int nb_cas;
    cin>>nb_cas;
    for(int c=1;c<=nb_cas;c++)
    {
        cout<<"Case #"<<c<<": ";
        int nb_lignes;
        int nb_colonnes;
        cin>>nb_lignes>>nb_colonnes;
        vector<vector<int> > v(nb_lignes,vector<int>(nb_colonnes));
        for(int c2=0;c2<nb_lignes;c2++)
            for(int c3=0;c3<nb_colonnes;c3++)
                cin>>v[c2][c3];
        for(int c2=0;c2<nb_lignes;c2++)
            for(int c3=0;c3<nb_colonnes;c3++)
            {
                int c4=0;
                for(;c4<nb_lignes;c4++)
                    if(v[c4][c3]>v[c2][c3])
                        break;
                if(c4==nb_lignes)
                    continue;
                c4=0;
                for(;c4<nb_colonnes;c4++)
                    if(v[c2][c4]>v[c2][c3])
                        break;
                if(c4==nb_colonnes)
                    continue;
                cout<<"NO";
                goto end;
            }

        cout<<"YES";
        end:
            cout<<endl;

    }
}
