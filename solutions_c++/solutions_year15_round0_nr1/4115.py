/*Sarbajit Saha*/

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

typedef long long ll;
typedef unsigned long ul;
typedef unsigned int ui;

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        ll shymax;
        cin>>shymax;
        string shy;
        cin>>shy;
        ll cot=0,add=0;
        ll len=shy.length()-1;
        for(ll j=0;j<=len;j++)
        {
            if(add>=j)
            {
                add+=shy[j]-'0';
            }
            else
            {
                add++;
                cot++;
                add+=shy[j]-'0';
            }

        }
        cout<<"Case #"<<i<<": "<<cot<<endl;
    }
    return 0;
}
