#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iterator>
#include <numeric>

using namespace std;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("output1.txt","w",stdout);
    int t;cin>>t;
    int testcaseno=1;
    while(t--)
    {
    int n;
    cin>>n;
    double naomi[n],ken[n];
    for(int i=0;i<n;++i){cin>>naomi[i];}
    for(int i=0;i<n;++i){cin>>ken[i];}
    sort(naomi,naomi+n);
    sort(ken,ken+n);
    //for(int i=0;i<n;++i){cout<<naomi[i]<<" ";}cout<<endl;
    //for(int i=0;i<n;++i){cout<<ken[i]<<" ";}cout<<endl;
    ///lightest first; war
    int z=0;int i=0;int j=0;
    while(i<n && j<n)
    {
        if(ken[j]>naomi[i])//ken scores a point
        {
            i++;j++;
        }
        else //find the lightest block with ken which is heavier than naomi's
        {
            j++;
        }
    }
    if(j==n)//ken has no block to counter naomi's
    {
        //naomi scores a point for each block she has
        z+=(n-i);//ith block is the first unmatched; no points if i is already n, means all blocks matched
    }
    /**at each step, naomi can make ken destroy his lightest block, gaining 1 point or destroy his heaviest block, ken gaining 1 point this time **/
    int y=0;i=0;int low=0;int high=n-1;
    while(i<n)
    {
        if(naomi[i]>ken[low]){i++;low++;y++;} //weigh ith block(by overstating) against lightest ken block, and naomi gains 1 point
        else if(naomi[i]<ken[high])//ith block with naomi is heavier than lightest with ken; ken wouls realize the lie; so use it to destroy the heaviest block with ken
        {
            i++;high--;
        }
        //else //when naomi[i]<ken[low] and naomi[i]>ken[high]; not possible
        //and low can never be larger than high; bcoz low++ and high-- can be atmost done n times, till i reaches n
    }


    cout<<"Case #"<<testcaseno<<": "<<y<<" "<<z<<endl;
    testcaseno++;
    }
    return 0;
}
