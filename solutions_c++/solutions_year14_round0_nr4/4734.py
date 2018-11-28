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
#include <string.h>
#include <climits>

#define repx(i,x,n) for(int i=x;i<n;i++)
#define rep(i,n) repx(i,0,n)
#define pb push_back
#define full(v)	v.begin(),v.end()
#define VI vector<int>
#define VS vector<string>
#define LL long long
using namespace std;

int main()
{
    int test,cas=0;
    ifstream cin ("gcjin4big.in");
    ofstream cout ("gcjout4big.txt");
    cin>>test;
    while(test-- && ++ cas)
    {
        int n;
        cin>>n;
        vector <double> kim,naomi;
        double temp;
        int vis1[1002],vis2[1002];
        memset(vis1,0,sizeof(vis1));
        memset(vis2,0,sizeof(vis2));
        rep(i,n)
        {
            cin>>temp;naomi.pb(temp);
        }
        rep(i,n)
        {
            cin>>temp;kim.pb(temp);
        }
        sort(kim.begin(),kim.end());
        sort(naomi.begin(),naomi.end());

        int r1=0,r2=0;
        //play war
        rep(i,n)
        {
            double tochoose = 2.0;
            int pos = -1;
            rep(j,n)
            {
                if(kim[j]>naomi[i]&&!vis1[j])
                {
                    if(kim[j] < tochoose)
                        pos=j;
                    tochoose = min(tochoose , kim[j]);
                }
            }
            if(tochoose == 2.0)
                r1++;
            else
            {
                vis1[pos]=1;
            }
        }
        rep(i,n)
        {
            double tochoose = 2.0;
            int pos=-1;
            rep(j,n)
            {
                if(kim[j] < naomi[i] && !vis2[j])
                {
                    if(tochoose > kim[j])
                        pos=j;
                    tochoose = min(tochoose,kim[j]);
                }
            }
            if(tochoose != 2.0)
            {
          //      cout<<naomi[i]<<" "<<kim[pos]<<"\n";
                    r2++;
                    vis2[pos]=1;
            }
            else
            {
                tochoose = -1.0;
                rep(j,n)
                {
                    if(!vis2[j])
                    {
                        if(tochoose < kim[j])
                        {
                            pos=j;
                            tochoose = kim[j];
                        }
                    }
                }
                vis2[pos]=1;
            //    cout<<naomi[i]<<" "<<kim[pos]<<"\n";

            }
        }
        cout<<"Case #"<<cas<<": ";
        cout<<r2<<" "<<r1<<"\n";

    }
    return 0;
}
