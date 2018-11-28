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





int main(int argc,char **argv)
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int nb_cas;
    cin>>nb_cas;
    for(int c=1;c<=nb_cas;c++)
    {
        out<<"Case #"<<c<<": ";
        double r,t;
        cin>>r>>t;

        int nb_cercles=0;
        double act=0;
        while(act<=t)
        {
            act+=((r+nb_cercles*2+1)*(r+nb_cercles*2+1)-(r+nb_cercles*2)*(r+nb_cercles*2));
            nb_cercles++;
        }
        nb_cercles--;
        out<<nb_cercles<<endl;

    }
}
