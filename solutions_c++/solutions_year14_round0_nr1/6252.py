#include <iostream>
#include <cstring>
#include <queue>
#include <stdio.h>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <cstdio>
#include <set>
#include <cstdlib>
#include <vector>
#include <cctype>
#include <utility>
#include <map>
#include <string>
using namespace std;

int conversion(string p){ int o; o=atoi(p.c_str()); return o; }
string toString(int h){ stringstream ss; ss<<h; return ss.str(); }
long long gcd(long long a,long long b) {return (b==0 ? a : gcd(b,a%b));}
int lcm(int a,int b) {return (a*(b/gcd(a,b))); }

int main()
{
    ios::sync_with_stdio(1);

    #ifndef ONLINE_JUDGE
    freopen("D:/input.txt","r",stdin);
    freopen("D:/output.txt","w",stdout);
    #endif

    int T,cas=1;
    cin>>T;
    while(T--)
    {
        int num[17];
        memset(num,0,sizeof num);
        int lab[4][4],lab1[4][4];
        int n,m,res=0,acu=0;
        cin>>n;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>lab[i][j];
            }
        }
        cin>>m;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>lab1[i][j];
            }
        }
        for(int i=0;i<4;i++) num[lab[n-1][i]]++;
        for(int i=0;i<4;i++) num[lab1[m-1][i]]++;
        for(int i=0;i<17;i++)
        {
            if(num[i]==2)
            {
                res=i;
                acu++;
                if(acu==2)
                {
                    cout<<"Case #"<<cas<<": Bad magician!"<<endl;
                    cas++;
                    break;
                }
            }
        }
        if(acu==2) continue;
        if(acu==1) cout<<"Case #"<<cas<<": "<<res<<endl;
        else cout<<"Case #"<<cas<<": "<<"Volunteer cheated!"<<endl;
        cas++;
    }
}
