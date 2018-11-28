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
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <stdint.h>
#include <fstream>

using namespace std;
#define LL_max 200000000000
#define mod 1000000007

#define LL long long
#define mp make_pair
#define pb push_back

int main()
{
    int t,n,ca=0,y,z,i,j;
    double val;
    ifstream file;
    file.open ("input.txt");
    std::string word;
    file>>word;
    t = atoi(word.c_str());
    while(t--)
    {
        ca++;
        y=z=0;
        vector<double> v1,v2,v3,v4;
        file>>word;
        n=atoi(word.c_str());
        for(int il=0;il<n;il++)
        {
            file>>word;
            val=atof(word.c_str());
            v1.pb(val);
            v3.pb(val);
        }
        for(int il=0;il<n;il++)
        {
            file>>word;
            val=atof(word.c_str());
            v2.pb(val);
            v4.pb(val);
        }
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        sort(v3.begin(),v3.end());
        sort(v4.begin(),v4.end());
        for(i=0;i<n;i++)
        {
            for(j=n-1;j>=0;j--)
            {
                if(v1[i]>v2[j])
                {
                    y++;
                    v2[j]=10;
                    break;
                }
            }
        }
        j=0;
        for(i=0;i<n;i++)
        {
            if(v4[i]>v3[j])
                j++;
        }
        z=n-j;
        printf("Case #%d: %d %d\n",ca,y,z);
    }
    return 0;
}
