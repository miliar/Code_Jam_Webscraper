#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <math.h>
#include <algorithm>

using namespace std;

int n,m;
int a[100][100];

bool lawn()
{
//    for(int i=0;i<n;++i)
//    {
//        for(int j=0;j<m;++j)
//            cout << a[i][j] << " ";
//        cout << endl;
//    }
    if(n==1||m==1) return true;

    int allr = 0;
    vector<int> diffrow;
    vector<int> samerow;
    for(int i=0;i<n;++i)
    {
        int v=a[i][0];
        int flag = 0;
        for(int j=0;j<m;++j)
        {
            if(v != a[i][j]) flag = 1;
        }
        if(flag == 1) diffrow.push_back(i);
        if(flag == 0) samerow.push_back(i);
        allr+=flag;
    }
    if (allr == 0) return true;

    int allc = 0;
    vector<int> diffcol;
    for(int j=0;j<m;++j)
    {
        int v=a[0][j];
        int same = 0;
        for(int i=0;i<n;++i)
        {
            if(v != a[i][j]) same = 1;
        }
        if(same == 1) diffcol.push_back(j);
        allc+=same;
    }
    if (allc == 0) return true;

    vector<int>::iterator it;
    for(it=diffrow.begin();it!=diffrow.end();++it)
    {
        for(int j=0;j<m;++j)
        {
            if(a[*it][j]==1) {
                for(int i1=0;i1<n;++i1)
                {
                    if(a[i1][j] != 1) return false;
                }
            }
        }
    }

    return true;
/*
    for(int j=0;j<m;++j)
    {
        int v=a[0][j];
        vector<int> low;
        for(int i=0;i<n;++i)
        {
            if(a[i][j]==1) low.push_back(j);
            if(a[i][j]==2 && low.size() != 0) {
                if (low.find(j) != low.end()) {
                    return false;
                }
            }
        }
    }
*/
}

int main(int argc, char * argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int TT;
    scanf("%d", &TT);
    for(int T=1;T<=TT;++T)
    {
        scanf("%d%d",&n,&m);
        memset(a,0,sizeof(a));
        for(int i=0;i<n;++i)
        {
            for(int j=0;j<m;++j)
            {
                scanf("%d",&a[i][j]);
            }
        }
        bool p = lawn();
        if (p) {
            printf("Case #%d: YES\n",T);
        } else {
            printf("Case #%d: NO\n",T);
        }
    }
    return 0;
}
