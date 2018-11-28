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

using namespace std;

int main() {
  freopen("lin", "r", stdin);
  freopen("lout", "w", stdout);
  int tt;
  int smax, j, sum, invite;
  string av;
  int i, a[1200];

  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++)
        {
            printf("Case #%d: ", qq);
            cin>>smax;
            cin>>av;

            for (i=0; i<=smax; i++)
            {
                a[i]=av[i];
                a[i]-=48;

            }
            invite=0;
            sum=a[0];
            for (i=1; i<=smax; i++)
            {


                for (j=0; j<i; j++)
                {
                    sum+=a[j];
                }
                if (sum<i)
                {
                    invite+=(i-sum);

                }
                sum=invite;
            }
            cout<<invite<<endl;


        }



  return 0;
}
