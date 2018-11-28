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
#define ll long long
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    for(int cs=1;cs<=t;cs++)
    {
         printf("Case #%d: ",cs);
       int n;
       cin>>n;
       string a,b;
       cin>>a>>b;
       int i=0,j=0;
       int la=a.length();
       int lb=b.length();
       int flg=0;
       int ans=0;
       while(i<la||j<lb)
       {

        if(i<la&&j<lb&&a[i]==b[j])
        {
            i++;
            j++;
        }
        else if(i==0&&j==0)
        {
            flg=1;
            break;
        }
        else if(i==la)
        {
            if(b[j]==b[j-1])
            {
                j++;
                ans++;
            }
            else {
                flg=1;
                break;
            }
        }
        else if(j==lb)
        {
            if(a[i]==a[i-1])
            {
                i++;
                ans++;
            }
            else{
                flg=1;
                break;
            }
        }
        else if(a[i]==a[i-1]&&b[j]==b[j-1])
        {
            if((la-i)>(lb-j))
            {
                i++;
                ans++;
            }
            else
            {
                j++;
                ans++;
            }
        }
        else if(a[i]==a[i-1])
        {
            i++;
            ans++;
        }
        else if(b[j]==b[j-1])
        {
            j++;
            ans++;
        }
        else
        {
            flg=1;
            break;
        }

       }
    if(flg==1)
        cout<<"Fegla Won\n";
    else 
        cout<<ans<<endl;
    }
    return 0;
}