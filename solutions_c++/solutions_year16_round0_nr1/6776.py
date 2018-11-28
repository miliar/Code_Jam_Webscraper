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
#include <cmath>
#include <cstdlib>
#include <ctime>

#define LL long long
using namespace std;

int main()
{
    freopen("linpu.txt", "r", stdin);
    freopen("out17.txt", "w", stdout);
   int tst ,ctr,cou,dig;
   LL num,xnum=0;
   cin >> tst;
   for(int ii=1;ii<=tst;ii++)
   {
       int *arry = new int[10];
       for (int jj=0;jj<10;jj++)
           {arry[jj]=10;}
        cin >> num;
        xnum=num;ctr=0;cou=1;
        if(num==0)
           cout <<"Case #"<<ii<<": INSOMNIA"<<endl;
        else {while(ctr<10)
        {
            while(num>0)
            {
                 dig=num%10;
                 if(arry[dig]!=dig)
                   ctr++;
                 arry[dig]=dig;
                 num/=10;
            }
            cou++;
            num=cou*xnum;
        }
        cout <<"Case #"<<ii<<": "<<((cou-1)*xnum)<<endl;
   }}
   return 0;
}

