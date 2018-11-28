#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <sstream>

using namespace std;

inline void print_set(set<int> si)
{
    cout << "{ ";
    for (set<int>::iterator i = si.begin(); i != si.end(); ++i)
    {
        cout << (*i) << " ";
    }
    cout << "}" << endl;
}

template <typename T>
string ntos ( T Number )
{
    stringstream ss;
    ss << Number;
    return ss.str();
}

set<int> digits(unsigned long long int n, set<int> &d)
{
    // set<int> d;
    string n_string = ntos(n);
    for ( string::iterator it = n_string.begin() ; it != n_string.end(); ++it)
    {
        d.insert((int)(*it) - (int)'0');
    }
    return d;
}

int main()
{

    int t;
    cin >> t;
    int myints[]= {0,1,2,3,4,5,6,7,8,9};
    set<int> all (myints,myints+10);        // digits
    for (int c=1; c<=t; ++c)
    {
        string answer = "INSOMNIA";
        unsigned long long int n;
        cin >> n;
        if (n > 0)
        {
            int curr_n = 0;
            set<int> digits_so_far;
            while( digits_so_far != all )
            {
                curr_n += n;
                digits(curr_n,digits_so_far);
            }

            answer = ntos(curr_n);
        }
        cout << "Case #" << c << ": " << answer << endl;
    }

    return 0;
}
