#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )

using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }


int main()
{
    int i, j, k;
    int nbTestCases = 0;
    freopen ("A-small-attempt0.in","r",stdin);
    freopen ("A-small-attempt0.out","w",stdout);
    cin >> nbTestCases;

    fi(nbTestCases) {
        int N = 0;
        cin >> N;
        vector<string> words;
        fj(N)
            words.push_back(ns());

        bool done = false, failed = false;
        int totalSwaps =0;
        while (!done) {
            if (words[0].size() == 0) {
                done = true;
                break;
            }
            char c = words[0][0];
            int wc = 0;
            fj(N) {
                int l = 0;
                if (words[j].size() == 0 || words[j][0] != c) {
                    done = true; failed = true; break;
                }
                while (words[j][l] == c)
                    l++;
                wc += l;
            }
            if (done)
                break;
            int target = round(wc/N);
            int swaps = 0;
            fj(N) {
                int l = 0;
                while (words[j][l] == c)
                    l++;
                swaps += abs(l-target);
                words[j].erase(0,l);
            }
            totalSwaps += swaps;
        }
        fj(N)
            if (words[j].size() != 0)
                failed = true;
        cout << "Case #"<<i+1<<": ";
        if (failed)
            cout << "Fegla Won" << endl;
        else
            cout << totalSwaps << endl;
    }
    return 0;
}
