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
        long long int A,N;
        cin>>A>>N;
        vector<int> tailles(N);
        for(int c2=0;c2<N;c2++)
        {
            cin>>tailles[c2];
        }
        sort(tailles.begin(),tailles.end());
        int mini=tailles.size();
        int to_add=0;
        if(A==1)
        {
            out<<tailles.size()<<endl;
            continue;
        }
        for(int c2=0;c2<tailles.size();c2++)
        {
            mini=min(mini,(int)tailles.size()-c2+to_add);
            while(A<=tailles[c2])
                A+=(A-1),to_add++;
            A+=tailles[c2];
        }
        mini=min(mini,to_add);
        out<<mini<<endl;
    }
}
