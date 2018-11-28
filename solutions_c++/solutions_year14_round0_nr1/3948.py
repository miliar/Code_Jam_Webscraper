# include <iostream>
# include <fstream>
# include <sstream>
# include <algorithm>
# include <numeric>
# include <cstdio>
# include <cmath>
# include <cstdlib>
# include <cstring>
# include <vector>
# include <list>
# include <set>
# include <map>
# include <stack>
# include <queue>
# include <cctype>
# include <climits>
# include <string.h>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;

#define GI ({int t;scanf("%d",&t);t;})
#define REP(i,a,b) for(int i=a;i<b;i++)
#define ALL(v) (v).begin(),(v).end()
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define pb push_back
#define mp make_pair
#define INF (int)1e9
#define EPS (double)(1e-9)
#define PI (double)(3.141592653589793)

int main()
{
    int T;
    cin>>T;
    REP(in,1,T+1)
    {
        int A,B;
        int arrange1[4][4],arrange2[4][4];
        cin>>A;
        REP(i,0,4)
        {
            REP(j,0,4)
            {
                cin>>arrange1[i][j];
            }
        }
        cin>>B;
         REP(i,0,4)
        {
            REP(j,0,4)
            {
                cin>>arrange2[i][j];
            }
        }
        int count=0;
        int value;
        REP(i,0,4)
        {
            int num1=arrange1[A-1][i];
            REP(j,0,4)
            {
                int num2=arrange2[B-1][j];
                if(num1==num2)
                        {
                            count++;
                            value=num1;
                        }
                if(count>1)
                {
                    cout<<"Case #"<<in<<": Bad magician!\n";
                    break;
                }

            }
            if(count>1)
                break;
        }
        if(count==0)
            cout<<"Case #"<<in<<": Volunteer cheated!\n";
        else if(count==1)
            cout<<"Case #"<<in<<": "<<value<<"\n";
    }
    return 0;
}
