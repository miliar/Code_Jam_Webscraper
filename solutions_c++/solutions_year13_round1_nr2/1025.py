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

#define cin in

#ifdef LOCAL
#define COUT(s) cout<<"-----"<<s<<"-----"<<endl;
#endif

using namespace std;


int bourrin(int i,vector<int> v,int E,int R,int initial)
{
    if(i>=v.size()) return 0;
    int maxi=0;
    for(int c=E;c>=0;c--)
    {
        int z=v[i]*c+bourrin(i+1,v,min(E-c+R,initial),R,initial);
        if(z>maxi)
            maxi=z;
        else break;
    }
    return maxi;
}

int main(int argc,char **argv)
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int nb_cas;
    cin>>nb_cas;
    for(int c=1;c<=nb_cas;c++)
    {
        out<<"Case #"<<c<<": ";
        int E,R,N;
        cin>>E>>R>>N;
        vector<int> v(N);
        for(int c=0;c<N;c++)
        {
            cin>>v[c];
        }
        out<<bourrin(0,v,E,R,E)<<endl;
    }
}
