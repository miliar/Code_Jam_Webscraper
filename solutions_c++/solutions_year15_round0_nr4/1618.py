#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <cstdio>
typedef long long ll;
typedef double d;
typedef unsigned long long ull;
using namespace std;

int main()
{
    cin.tie(0);
    std::ios::sync_with_stdio(false);
    freopen("D-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,x,r,c;
    cin >> t;
    for(int i =1;i<=t;i++)
    {
        cin >> x>> r>>c;
        cout << "Case #"<<i<<": ";
        if(x==1)
        {
            cout << "GABRIEL"<<endl;
        }
        else if(x==2&&(r%2==0||c%2==0))
        {
            cout << "GABRIEL"<<endl;
        }
        else if(x==3&&((r==3&&c==3)||(r==3&&c==2)||(r==2&&c==3)||(r==3&&c==4)||(r==4&&c==3)))
        {
            cout << "GABRIEL"<<endl;
        }
        else if (x==4&&((c==4&&r==4)||(r==4&&c==3)||(r==3&&c==4)))
        {
            cout << "GABRIEL"<<endl;
        }
        else
            cout <<"RICHARD"<<endl;
    }
    return 0;
}
