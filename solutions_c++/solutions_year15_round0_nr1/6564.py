#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <queue>
using namespace std;
int main()
{
    //freopen("input.txt","r",stdin);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int smax;
        cin>>smax;
        char arr[smax+5];
        cin>>arr;
        long long int cnt=0;
        long long int curr=0;
        for(int j=0;j<=smax;j++)
        {
            int tmp = arr[j]-48;
            if(tmp==0)
                continue;
            if(j<=curr)
            {
                curr+=tmp;
            }
            else
            {
                cnt+=j-curr;
                curr+=j-curr+tmp;
            }
            //cout<<curr<<" "<<cnt<<endl;
        }
        cout<<"Case #"<<i<<": "<<cnt<<endl;
    }
    return 0;
}
