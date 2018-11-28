#include <iostream>
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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;
int t;
int n;
int anss;
int sum[100];
//int cnt;
string s;
int cnt[100];
int cntt;
int num[100];
pair<int,int>a[100][100];
bool flg;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        flg=true;
        anss=0;
        for(int j=0;j<100;j++)
        {
            num[j]=0;
            sum[j]=0;
            for(int k=0;k<100;k++)
            {
                a[j][k].first=0;
                a[j][k].second=0;
            }
        }
        cin>>n;
        for(int j=0;j<n;j++)
        {
            cnt[j]=0;
            cin>>s;
            a[j][0].first=s[0];
            a[j][0].second=1;
            for(int k=1;k<s.length();k++)
            {
                if(s[k]!=s[k-1])
                {
                    cnt[j]++;
                    a[j][cnt[j]].first=s[k];
                }
                a[j][cnt[j]].second++;
            }
            //cout<<a[j][cnt[j]].first<<" "<<a[j][cnt[j]].second<<endl;
        }
        for(int j=0;j<n;j++)
        {
            //cout<<cnt[j]<<endl;
            if(cnt[j]!=cnt[0]) flg=false;
        }
        if(flg==true)
        {
            cntt=cnt[0]+1;
            //cout<<"c "<<cntt<<endl;
            for(int j=0;j<cntt;j++)
            {
                num[j]=a[0][j].second;
                for(int k=1;k<n;k++)
                {
                    if(a[k][j].first!=a[k-1][j].first)
                    {
                        flg=false;
                    }
                    num[j]=num[j]+a[k][j].second;
                }
                num[j]=num[j]/n;
                //cout<<num[j]<<endl;
                for(int k=0;k<n;k++)
                {
                    sum[j]=sum[j]+abs(a[k][j].second-num[j]);
                }
            }
        }
        if(flg==true)
        {
            for(int j=0;j<=cntt;j++)
            {
                anss=anss+sum[j];
            }
        }
        if(flg==false)
        {
            cout<<"Case #"<<i+1<<": Fegla Won"<<endl;
        }
        else
        {
            cout<<"Case #"<<i+1<<": "<<anss<<endl;
        }
    }


    return 0;
}
