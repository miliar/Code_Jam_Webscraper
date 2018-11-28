
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i,n) for(int i=0; i<(int)(n); ++i)


class Problem
{
private:
    static const int MAX_MN=101;
    int T;
    int CASE;
    int N,M;
    int MAP[MAX_MN][MAX_MN];

public:
	Problem()
	{
	}

    bool check()
    {
        REP(i,N)REP(j,M)
        {
            int check_num=MAP[i][j];
            bool retx=true;
            bool rety=true;
            REP(a,N)
            {
                if(check_num<MAP[a][j])
                {
                    retx=false;
                    break;
                }
            }
            REP(a,M)
            {
                if(check_num<MAP[i][a])
                {
                    rety=false;
                    break;
                }
            }
            if(!retx && !rety)  return false;
        }
        return true;
    }

	void solve()
	{
        cin>>T;
        while(CASE++<T)
        {
            cin>>N>>M;
            REP(i,N)REP(j,M)
            {
                cin>>MAP[i][j];
            }
            if(check())
                printf("Case #%d: YES\n",CASE);
            else 
                printf("Case #%d: NO\n",CASE);
        }
	}
};

int main()
{
	Problem problem=Problem();
	problem.solve();
	//system("pause");
	return 0;
}


