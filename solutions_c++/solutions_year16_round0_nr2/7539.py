#include <vector>
#include <stdio.h>
#include <string.h>
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
typedef long long ll;
//typedef long double d;
using namespace std;

int main()
{
    //std::cin.tie(0);
    //std::ios::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ll t;
    cin >> t;
    for(int q=1; q<=t; q++)
    {
        string s;
        cin >> s;
        bool ok=1;
        ll counter=0;
        while(ok)
        {
            ok=0;
            for(int i=s.size()-1; i>=0; i--)
            {
                if(s[i]=='-')
                {
                    ok=1;
                    counter++;
                    if(s[0]=='-')
                    {
                        for(int h=0; h<=i/2; h++)
                        {
                            swap(s[i-h],s[h]);
                            if(s[h]=='-')
                                s[h]='+';
                            else
                                s[h]='-';
                            if(i-h!=h)
                            {
                                if(s[i-h]=='-')
                                    s[i-h]='+';
                                else
                                    s[i-h]='-';
                            }
                        }
                    }
                    else
                    {
                        counter++;
                        for(int h=0; h<i&&s[h]=='+'; h++)
                        {
                            s[h]='-';
                        }
                        for(int h=0; h<=i/2; h++)
                        {
                            swap(s[i-h],s[h]);
                            if(s[h]=='-')
                                s[h]='+';
                            else
                                s[h]='-';
                            if(i-h!=h)
                            {
                                if(s[i-h]=='-')
                                    s[i-h]='+';
                                else
                                    s[i-h]='-';
                            }
                        }
                    }
                }
            }
        }
        cout << "Case #"<< q<<": "<< counter << endl;
    }
    return 0;
}
