#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <utility>
#include <queue>
#include <string>
#include <sstream>

using namespace std;

#define ull unsigned long long int
#define ll long long int
#define print_v(v, l)    for (ull i=0; i<l;i++) cout << v[i]; cout << endl;
#define print_pair(p) cout << "(" << p.first << ", " << p.second << ")" << endl;
#define sort_asc(v, b, e) sort(v+b, v+e);
#define sort_dsc(v, b, e) sort(v+b, v+e, std::greater<int>());
#define ssort_asc(v, b, e) stable_sort(v+b, v+e);
#define ssort_dsc(v, b, e) stable_sort(v+b, v+e, std::greater<int>());
#define DEBUG {cout << "DEBUG" << endl;exit(-1);}


int T;
int A, B;

string convert_int(int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}

int is_square(int n)
{
    if(n==1) return 1;
    for(int i=1; i <= n/2; i++)
        if(i*i==n)
            return i;
    return -1;
}

bool is_palindrome(int n)
{
    string n_str = convert_int(n);
    for(int i=0; i < n_str.length()/2; i++)
        if(n_str[i]!=n_str[n_str.length()-1-i])
            return false;
    return true;
}

void solve()
{
    int c=0;
    /* trivial one :) */
    for(int i=A; i<=B; i++)
    {
        int root=is_square(i);
        //cout << "C: " << i << " R: " << root << endl;
        if(root > 0 && is_palindrome(i) && is_palindrome(root))
        {
            c++;
        }
    }
    cout << c;
}

int main (int argc, char *argv[])
{

    #ifdef DEBUGGING
      freopen("input.in","r",stdin);
      freopen("output.txt","w",stdout);
    #endif

    cin >> T;
    for(int i=0; i < T; i++)
    {
        cin >> A >> B;
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
    }


    return 0;
}

