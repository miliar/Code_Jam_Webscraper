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
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

typedef long ll;

using namespace std;


ll mul(ll x,ll y)
{
    if(x==1)
    {
        if(y==1)
            return 1;
        if(y==2)
            return 2;
        if(y==3)
            return 3;
        if(y==4)
            return 4;
    }

    if(x==2)
    {
        if(y==1)
            return 2;
        if(y==2)
            return (-1);
        if(y==3)
            return 4;
        if(y==4)
            return -3;

    }

    if(x==3)
    {
        if(y==1)
            return 3;
        if(y==2)
            return -4;
        if(y==3)
            return (-1);
        if(y==4)
            return (2);
    }

    if(x==4)
    {
        if(y==1)
            return 4;
        if(y==2)
            return (3);
        if(y==3)
            return -2;
        if(y==4)
            return (-1);
    }

    if(x==-1)
    {
        if(y==1)
            return (-1);
        if(y==2)
            return (-2);
        if(y==3)
            return(-3);
        if(y==4)
            return (-4);
    }

    if(x==-2)
    {
        if(y==1)
            return (-2);
        if(y==2)
            return 1;
        if(y==3)
            return -4;
        if(y==4)
            return (3);

    }

    if(x==-3)
    {
        if(y==1)
            return (-3);
        if(y==2)
            return (4);
        if(y==3)
            return 1;
        if(y==4)
            return -2;
    }

    if(x==-4)
    {
        if(y==1)
            return (-4);
        if(y==2)
            return -3;
        if(y==3)
            return (2);
        if(y==4)
            return 1;
    }
}

int func(vector<ll>& dijk)
{
    int flag=0;
    ll ans1=0,ans2=0,ans3=0;
    for(ll j=0;j<dijk.size();j++)
    {
        ans1=dijk[0];
        if(ans1==2||ans1==-2)
            flag++;
        else
        {
            while(flag==0&&j<dijk.size())
            {
                j++;
                ans1=mul(ans1,dijk[j]);
                if(ans1==2)
                  flag++;
            }
        }

        if(flag!=1)
            break;
        j++;
        if(j>=dijk.size())
            break;
        ans2=dijk[j];
        if(ans2==3)
            flag++;
        else
        {
           while(flag==1&&j<dijk.size())
            {
                j++;
                ans2=mul(ans2,dijk[j]);
                if(ans2==3)
                  flag++;
            }
        }

        if(flag!=2)
            break;
        j++;
        if(j>=dijk.size())
            break;
        ans3=dijk[j];
      //  cout<<ans3<<j<<dijk.size()<<endl;

        while(j!=dijk.size()-1)
        {
            j++;
            ans3=mul(ans3,dijk[j]);
            //cout<<ans3<<endl;
        }
        if(ans3==4)
            flag++;
    }
  //  cout<<flag<<" "<<ans1<<" "<<ans2<<" "<<ans3<<endl;
    if(flag==3)
        return 1;
    else
        return 0;

}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        vector<int> vec;
        vector<ll> dijk;
        ll l,x;
        cin>>l>>x;
        string s;
        cin>>s;
        for(ll j=0;j<l;j++)
        {
            if(s[j]=='i')
                vec.push_back(2);
            if(s[j]=='j')
                vec.push_back(3);
            if(s[j]=='k')
                vec.push_back(4);
        }
        for(ll k=0;k<x;k++)
        {
            for(ll j=0;j<l;j++)
            {
                dijk.push_back(vec[j]);
            }
        }

       if(func(dijk))
          cout<<"Case #"<<i<<": YES\n";
       else
          cout<<"Case #"<<i<<": NO\n";
    }
    return 0;
}
