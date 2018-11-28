#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>
#include <fstream>
#include <cstring>

using namespace std;
typedef long long LL;

int a[5][5];
int k[20];
int main()
{
    freopen("magic_trick.in","r",stdin);
    freopen("magic_trick.out","w",stdout);
    int tc, nt=1;
    cin>>tc;
    while (tc--)
    {
        int n;
        memset(k,0,sizeof(k));
        for (int cnt=0;cnt<2;cnt++)
        {
            cin>>n;
            for (int i=0;i<4;i++)
                for (int j=0;j<4;j++)
                {
                    cin>>a[i][j];
                    if (i==n-1) k[a[i][j]]++;
                }
        }
        int ret=0, cnt=0;
        for (int i=1;i<=16;i++)
            if (k[i]==2)
            {
                ret=i;
                cnt++;
            }
        cout<<"Case #"<<nt++<<": ";
        if (cnt==0) cout<<"Volunteer cheated!"<<endl;
        else if (cnt>=2) cout<<"Bad magician!"<<endl;
        else cout<<ret<<endl;
    }
}
