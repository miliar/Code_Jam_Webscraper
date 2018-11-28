//DEEPAK AHIRE
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <cstdio>
#include <string>
#include <cassert>
#include <climits>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <fstream>
using namespace std;
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define abs(x) ((x) > 0 ? (x) : -(x))
#define FOREACH(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
typedef long long int LL;
#define INF 1000001

#define IF 1000000000000000L

int main()
{
    LL t,k,c,s,cnt,i;
    cin>>t;
    ofstream myfile;
    myfile.open ("3.txt");
    cnt=1;
    while(t--)
    {
        cin>>k>>c>>s;

        myfile<<"Case #"<<cnt<<": ";

        for(i=1;i<=k;i++)
        {
            myfile<<i<<" ";
        }
        myfile<<"\n";
        cnt++;
    }
    myfile.close();
    return 0;
}
