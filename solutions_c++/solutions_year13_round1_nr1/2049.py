#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<iostream>
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
using namespace std;
int main()
{
    //freopen("in.txt","r",stdin);
       // freopen("out.txt","w",stdout);
      int  v,r,t,l,cnt,cmp=0;

        cin>>v;
        while(v--)
        {
                cnt=0;cmp++;
                cin>>r>>t;
                for(int i=1;;i+=2)
                {
                        l=(r+i)*(r+i)-(r+i-1)*(r+i-1);
                        if(l<=t)
                        {
                                cnt++;
                                t-=l;
                        }
                        else
                        break;

                }
                printf("Case #%d: %d\n",cmp,cnt);

        }
}
