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
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    int t, i, j;
    int p1,p2;
    int a1[5][5], a2[5][5];
    int counter, ans;
    freopen("C:\\Users\\ZLi\\CodeBlockCode\\Test\\GCJ2014PreA\\bin\\Debug\\A-small-attempt2.in", "r", stdin);
	freopen("C:\\Users\\ZLi\\CodeBlockCode\\Test\\GCJ2014PreA\\bin\\Debug\\output.txt", "w", stdout);

    cin>>t;
    for(int tn = 1; tn <= t; tn++)
    {
        cin>>p1;
        for(i = 1; i <= 4; i++)
        {
            for(j = 1; j <= 4; j++)
            {
                cin>>a1[i][j];
            }
        }
        cin>>p2;
        for(i = 1; i <= 4; i++)
        {
            for(j = 1; j <= 4; j++)
            {
                cin>>a2[i][j];
            }
        }

        counter = 0;
        for(i = 1; i <= 4; i++)
        {
            for(j = 1; j <= 4; j++)
            {
                if(a1[p1][i] == a2[p2][j])
                {
                    counter++;
                    ans = a1[p1][i];
                }
                if(counter > 1)
                    break;
            }
        }

        if(counter == 0)
            cout<<"Case #"<<tn<<": Volunteer cheated!"<<endl;
        else if(counter == 1)
            cout<<"Case #"<<tn<<": "<<ans<<endl;
        else
            cout<<"Case #"<<tn<<": Bad magician!"<<endl;
    }

    return 0;
}
