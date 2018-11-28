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
  freopen("A-large.in", "r", stdin);
  freopen("output", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
        //cout<<"1st  "<<endl;
        printf("Case #%d: ", qq);
        int shyns, chi;
        char ch;
        int no_rq = 0, sum = 0, diff = 0;
        scanf("%d", &shyns);
        //cout<<"shyns: "<<shyns<<endl;
        scanf("%c", &ch);
        for(int i = 0; i <= shyns; i++)
        {
            scanf("%c", &ch);
            chi = ch - '0';
            if(chi != 0)
            {
                if(i > sum)
                {
                    diff = i - sum;
                    no_rq = no_rq + diff;
                    sum = sum + chi + diff;
                }
                else
                {
                    sum = sum + chi;
                }
            }
        }

        cout<<no_rq<<endl;

  }
  return 0;
}















