#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;


int main()
{
    freopen("input.txt" , "r" , stdin);
    int t,cs = 1;
    cin>>t;
    while(t--)
    {
        long long int n;
        string s;
        cin>>n;
        cin>>s;
        vector<long long int> v;
        for(int i = 0 ; i <= n; i++)
        {
            long long int add = s[i] - '0';
            while(add--)
            {
                v.push_back(i);
            } 
        } 
        long long int stood = 0 , ans = 0;
        for(int i = 0; i < v.size(); i++)
        {
            if(stood >= v[i])
            {    
                stood++;
            }
            else
            {
                ans += abs(stood - v[i]);
                stood+= abs(stood - v[i])+1;
            }
            
        }
        cout<<"Case #"<<cs<<": "<<ans<<endl;
        cs++;
    }
    return 0;
}