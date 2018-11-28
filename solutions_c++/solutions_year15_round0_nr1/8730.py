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
#include <fstream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n;
    cin>>n;
    for(int k=1;k<=n;k++)
    {
        int a;
        string b;
        cin>>a>>b;
        int sum=0,no=0;
        for(int i=0;i<b.size();i++)
        {
            if(sum>=i)
            {
                sum+=(b[i]-'0');
            }
            else
            {
                while(sum<i)
                {
                    sum++;
                    no++;
                }
                sum+=(b[i]-'0');
            }
        }
        cout<<"Case #"<<k<<": "<<no<<endl;
    }

}
