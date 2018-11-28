#include<stdio.h>
#include<stdint.h>
#include<math.h>
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
using namespace std;

int main()
{
    int t,cas=1,ca=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,ans1=0,ans2=0;
        vector<double> veca,vecb,veca1,vecb1;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            double x;
            scanf("%lf",&x);
            veca.push_back(x);
            veca1.push_back(x);
        }
         for(int i=0;i<n;i++)
        {
            double x;
            scanf("%lf",&x);
            vecb.push_back(x);
            vecb1.push_back(x);
        }
        sort(veca.begin(),veca.end());
        sort(vecb.begin(),vecb.end());
        sort(veca1.begin(),veca1.end());
        sort(vecb1.begin(),vecb1.end());
        int i=n-1,j=n-1;

        for(int il=0;il<n;il++)
        {
            for(int jl=n-1;jl>=0;jl--)
            {
                if(veca[il]>vecb[jl])
                {
                    ans1++;
                    vecb[jl]=100;
                    break;
                }
            }
        }
        int xl=n-1;
        for(int il=n-1;il>=0;il--)
        {
            if(xl<0)
                break;
            if(vecb1[xl]==100)
            {
                il++;
                xl--;
                continue;
            }

            if(veca1[il]>vecb1[xl])
            {
                for(int jl=0;jl<n;jl++)
            {
                if(veca1[il]>vecb1[jl])
                {
                    ans2++;
                    vecb1[jl]=100;
                    break;
                }
            }
            }
            if(veca1[il]<vecb1[xl])
            {
                for(int jl=0;jl<n;jl++)
            {
                if(veca1[il]<vecb1[jl]&&vecb1[jl]!=100)
                {
                    vecb1[jl]=100;
                    break;
                }
            }
            }

        }
         printf("Case #%d: ",ca);
         printf("%d %d\n",ans1,ans2);
         ca++;
    }
}
