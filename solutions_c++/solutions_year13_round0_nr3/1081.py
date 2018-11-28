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

long long res[40]={0,1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,
				121242121LL,123454321LL,125686521LL,400080004LL,404090404LL,10000200001LL,10221412201LL,12102420121LL,12345654321LL,40000800004LL,
				1000002000001LL,1002003002001LL,1004006004001LL,1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,
				1214428244121LL,1232346432321LL,1234567654321LL,4000008000004LL,4004009004004LL};

int main(int argc,char **argv)
{
#ifdef LOCAL
    ifstream in("input.txt");
    ofstream out("output.txt");
#endif
    int nb_cas;
    cin>>nb_cas;
    for(int c=0;c<nb_cas;c++)
    {
        cout<<"Case #"<<c+1<<": ";
        long long int a,b;
        cin>>a>>b;
        int sum=0;
        for(int c2=0;c2<40;c2++)
            if(res[c2]>=a&&res[c2]<=b)
                sum++;
        cout<<sum<<endl;
    }
}
