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

int n;

int arr[1000001];

int main()
{
    LL t,i,a;
    cin>>t;
    ofstream myfile;
    myfile.open ("3.txt");
    int c=1,maxi;
    while(t--)
    {
        cin>>n;
        LL d = (2*n) -1;
        myfile<<"Case #"<<c++<<": ";
        maxi=0;
        memset(arr,0,sizeof(arr));
        while(d--)
        {
            for(i=1;i<=n;i++)
            {
                cin>>a;
                if(a>maxi)
                    maxi=a;
                arr[a]++;
            }
        }
        for(i=1;i<=maxi;i++)
        {
                if(arr[i]% 2 ==1)
                myfile<<i<<" ";
        }
        myfile<<endl;
    }
    return 0;
}
