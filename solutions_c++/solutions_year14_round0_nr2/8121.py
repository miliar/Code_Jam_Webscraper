//{ ---------- C headers
# include <cstdio>
# include <cstring>
# include <cmath>
# include <cstdlib>
# include <cctype>
//}

//{ ---------- C++ headers
# include <iostream>
# include <string>
# include <algorithm>
# include <vector>
# include <queue>
# include <stack>
# include <map>
# include <sstream>
//}
using namespace std;

//{ ---------- Movements
/*int dx[]={1,-1,0,0}, dy[]={0,0,1,-1};*/ // 4 way movement
/*int dx[]={1,0,-1,0,1,-1,1,-1}, dy[]={0,1,0,-1,1,1,-1,-1};*/ // 8 way movement
//}

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);

    double c,f,x;
    int t,cse=1;

    cin>>t;
    while(t--)
    {
        cin>>c>>f>>x;
        double total_time=0.0, current_cookie=2.0;

        while(true)
        {
            double current_time = x/current_cookie;
            double next_time = c/current_cookie + x/(current_cookie+f);

            if(current_time < next_time)
            {
                total_time += current_time;
                break;
            }
            else
            {
                total_time += c/current_cookie;
                current_cookie += f;
            }
        }

        printf("Case #%d: %.7lf\n",cse++,total_time);
    }

    return 0;
}
