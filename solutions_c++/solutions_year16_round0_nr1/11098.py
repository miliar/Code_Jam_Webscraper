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
#include <bits/stdc++.h>
using namespace std;
string convertInt(long long number)
{
    stringstream ss;
    ss << number;
    return ss.str();
}
int arr[10];
int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("oo.txt","w",stdout);
    long long n;
    long long cases;
    cin>>cases;
    long long t=1;
    while (cases--)
    {
        cin>>n;
        if (n==0)
            cout<<"Case #"<<t++<<": INSOMNIA"<<endl;
        else
        {
            cout<<"Case #"<<t++<<": ";
            long long f=1;
            long long temp=1;
            while (1)
            {
               // cout<<temp<<endl;
                temp=n*f;
                string s=convertInt(temp);
                for (long long i=0; i<s.size(); i++)
                {
                    arr[s[i]-'0']=1;
                }
                if (count(arr,arr+10,1)==10)
                {
                    cout<<temp<<endl;
                    memset(arr,0,sizeof arr);
                    break;
                }
                f++;
            }
        }
    }
}
// END KAWIGIEDIT TESTING
