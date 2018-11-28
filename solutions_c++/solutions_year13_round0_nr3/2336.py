#	include <algorithm>
#include <cstdlib>
#include <iostream>
#include <iterator>
#include <set>
#include <vector>
#include<map>
#include<cstdio>
#include<stack>
#include<cstring>
#include<climits>
#include<cmath>
#include<queue>
#include<string>

using namespace std;


vector<unsigned long long int> ans;


bool isPallindrom(unsigned long long int num)
{
    unsigned long long int  rev = 0, tmp = num;
    while(tmp)
    {
        rev = rev*10 + tmp%10;
        tmp = tmp/10;
    }
    return rev==num;
}
void preprocess()
{
    for(unsigned long long int i=1;i<=10000005;i++)
    {
        if(isPallindrom(i) && isPallindrom(i*i))
        {
            ans.push_back(i*i);
        }
    }
}

int main()
{
    preprocess();
/*
    for(int i=0; i< ans.size(); i++)
    {
        cout<<ans[i]<<endl;
    }*/
    int t;
    scanf("%d",&t);
    for(int cas=1; cas<=t; cas++)
    {
        int count = 0, l,u;
        unsigned long long x,y;
        //scanf("%ld%ld",&x,&y);
        cin>>x>>y;
        l = lower_bound(ans.begin(), ans.end(), x) - ans.begin();
        u = upper_bound(ans.begin(), ans.end(), y) - ans.begin();
        count = u-l;
        printf("Case #%d: %d\n",cas,count);
    }
    return 0;
}
