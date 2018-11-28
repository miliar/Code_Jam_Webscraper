//#include <bits/stdc++.h>
//#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <vector>
#include <algorithm>
#include <cctype>
#include <fstream>
#include <map>
#include <list>
#include <set>
#include <string>
#include <stack>
#include <bitset>

#define sz 155
#define pb(a) push_back(a)
#define pp pop_back()
#define ll long long
#define fread freopen("A-small-attempt2.in","r",stdin)
#define fwrite freopen("A-small-attempt2.out","w",stdout)
#define inf (1e9)
#define chng(a,b) a^=b^=a^=b;
#define clr(abc,z) memset(abc,z,sizeof(abc))
#define PI acos(-1)
#define fr(i,a,b) for(i=a;i<=b;i++)
#define print1(a)    cout<<a<<endl
#define print2(a,b) cout<<a<<" "<<b<<endl
#define print3(a,b,c) cout<<a<<" "<<b<<" "<<c<<endl
#define mod 1000000007
using namespace std;

char line[sz][sz];


vector<char>ccc;
vector<int>v[sz];


int main()
{
#ifdef ENAM
    fread;
    fwrite;
#endif // ENAM
    int t, n, m, cas=1, cnt;
    char ch;
    string s;
    scanf("%d", &t);
    bool flag;
    while(t--)
    {
        flag = true;
        ccc.clear();

        cnt = 0;
        scanf("%d", &n);
        for (int i = 0; i<n; i++)
            v[i].clear();

        scanf("%s", &line[0]);
        m = 1;
        ch = line[0][0];
        ccc.pb(ch);
        for (int i = 1; i<strlen(line[0]); i++)
        {
            if(ch==line[0][i]) m++;
            else
            {
                v[0].pb(m);
                m = 1;
                ch = line[0][i];
                ccc.pb(ch);
            }
        }
        v[0].pb(m);


        for (int i = 1; i<n; i++)
        {
            scanf("%s", &line[i]);
            m = 1;
            cnt = 0;
            ch = line[i][0];
            if(ccc[0]!=ch) flag = false;
            for (int j = 1; j<strlen(line[i]); j++)
            {
                if(ch==line[i][j]) m++;
                else
                {
                    cnt++;
                    if(ccc.size()<=cnt){flag=false; break;}
                    v[i].pb(m);
                    m = 1;
                    ch = line[i][j];
                    if(ccc[cnt]!=ch) flag = false;
                }
            }
            v[i].pb(m);
        }
//        cout<<"-----"<<endl;
//        for (int i  =0 ; i<n; i++)
//        {
//            for (int j  =0 ; j<v[i].size(); j++)
//                printf("%2d ",v[i][j]);
//                cout<<endl;
//        }
//        cout<<"-----"<<endl;

        int szzz = v[0].size();

        for (int i = 1; i<n; i++)
            if(szzz!=v[i].size())
            {
                flag = false;
                break;
            }


        if(flag)
        {
            int sum, fll, cll, totaln = 0, totalp = 0, total=0, now, prev;
            for (int i = 0; i<ccc.size(); i++)
            {
                sum = 0;
                for (int j = 0; j<n; j++)
                    sum+= v[j][i];
                fll = (int)floor(sum/(n*1.0));
                cll = (int) ceil(sum/(n*1.0));
                now = prev = 0;
                for (int j = 0; j<n; j++)
                    now+= abs(v[j][i]-fll);
                for (int j = 0; j<n; j++)
                    prev+= abs(v[j][i]-cll);
//                cout<<i<<" : "<<now<<" "<<prev<<endl;
                total+=min(now,prev);
//                totaln+= now;
//                totalp+= prev;
            }
            printf("Case #%d: %d\n",cas++, total);
        }
        else printf("Case #%d: Fegla Won\n",cas++);
    }


    return 0;
}
