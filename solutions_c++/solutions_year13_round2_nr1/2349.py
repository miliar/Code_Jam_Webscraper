#include <iostream>
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
#include<fstream>

typedef long long ll;
using namespace std;
vector<ll> arr(101);
int calc(ll & init, ll final)
{
    int n=0;
    while(init<=final)
    {
        init+=(init-1);
        n++;
    }
    return(n);
}
int main()
{
    ifstream fin("A-small-attempt1.in");
    //ifstream fin("input.in");
    ofstream fout("output.out");
    int t,a,n,i;
    fin>>t;
    //cout<<t;
    for(int cno=1;cno<=t;cno++)
    {
        fin>>a>>n;

        for(i=0;i<n;i++)
        {
            fin>>arr[i];
        }
        if(a==1)
        {
             fout<<"Case #"<<cno<<": "<<n<<"\n";
             continue;

        }
        sort(arr.begin(),arr.begin()+n);
        ll sum=a;
        int count=0;
        for(i=0;i<n;)
        {
            if(arr[i]<sum)
            {
                //cout<<"A sum= i "<<sum<<"\n";
                sum+=arr[i];
                i++;
                //cout<<"A sum= f "<<sum<<"\n";
            }
            else
            {
//                if(arr[i]<(2*sum-1))
//                {
//                    //cout<<"b sum= i "<<sum<<"\n";
//
//                    count++;
//                    sum+=(sum-1);
//                    sum+=arr[i];
//                    i++;
//                    //cout<<"b sum= f "<<sum<<"\n";
//                }
//                else
//                {
//                    //cout<<"ff\n";
//                    count+=(n-i);
//                    break;
//                }
                    int ans= calc(sum,arr[i]);
                    if(ans<(n-i))
                    {

                        sum+=arr[i];
                        i++;
                        count+=ans;

                    }
                    else
                    {
                        count+=(n-i);
                        break;
                    }
            }

        }
        fout<<"Case #"<<cno<<": "<<count<<"\n";
    }
    return 0;
}
