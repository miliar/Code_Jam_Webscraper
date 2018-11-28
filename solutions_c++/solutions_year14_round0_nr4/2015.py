//ShivamRana...
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <iterator>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <functional>
#include <numeric>
#include <algorithm>
using namespace std;
int main()
{
    //freopen("4b.in","r",stdin);
    //freopen("4b.out","w",stdout);
    int t;
    cin>>t;
    for(int cs=1;cs<=t;cs++)
    {
        printf("Case #%d: ",cs);
        int n;
        cin>>n;
        double arr[n+1],brr[n+1];
        for(int i=0;i<n;i++)
        cin>>arr[i];
        for(int i=0;i<n;i++)
        cin>>brr[i];
        sort(arr,arr+n);
        sort(brr,brr+n);
        int WAR=0,DWAR=0;
        for(int i=0,j=0;i<n&&j<n;)
        {
            if(arr[i]>brr[j]){
            WAR++;
            j++;
            }
            else{
                i++;
                j++;
            }
        }
        for(int i=0,j=0;i<n&&j<n;)
        {
            if(arr[i]>brr[j]){
            DWAR++;
            i++;
            j++;
            }
            else{
                i++;
            }
        }
        printf("%d %d\n",DWAR,WAR);

    }
    return 0;
}



