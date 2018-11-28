#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

long long int dp[20000] = {0} ;
int main()
{
    freopen("input.txt" , "r" , stdin);
    dp[1] = 0;
    dp[2] = 0;
    dp[3] = 1;
    dp[4] = 1;
    dp[5] = 2;
    dp[6] = 2;
    dp[7] = 2;
    dp[8] = 2;
    dp[9] = 3;
    int t,cs = 1;
    long long pwr[] = {1,2,4,8,16,32,64,128,256,512,1024,2048};
    cin>>t;
    while(t--)
    {
        long long int ans =100000000 ,n,mx=0 , mx_t = 0;
        cin>>n;
        map<long long , long long > mp;
        vector<long long> arr(n);
        for(int i = 0 ; i < n; i++)
        {
            cin>>arr[i];
            mx = max(mx , arr[i]);
        }
        sort(arr.rbegin() , arr.rend());
        long long int lo = 0 , hi = mx;
         mx_t = 0;
         int th = 0;
        while(lo < hi)
        {
            long long mid = (lo+hi)/2 , allot;
            allot = mid;
            bool ch = false;
            mx_t = 0;
            for(int i = 0; i < n; i++)
            {
                //cout<<arr[i]<<" "<<allot<<endl;
                ch = false;
                if(allot >= arr[i]-th && allot >= mx_t)
                {
                    ch = true;
                    break;
                }   
                else
                {
                    long long nm = arr[i];
                    long long subt = 1 , al2 = allot;
                    while(nm > allot && allot >= 0)
                    {
                        nm = (nm+1)/2;
                        allot-= subt;
                        subt *= 2;
                    }
                    if(nm <= allot && allot >= mx_t)
                    {
                        ch = true;
                        mx_t = max(nm , mx_t);
                    }
                    //cout<<ch<<endl;
                    
                    
                }
            }  
            mx_t = 0;
            bool ch2 = false;
            allot = mid;
            for(int i = 0; i < n; i++)
            {
                //cout<<arr[i]<<" "<<allot<<endl;
                ch2 = false;
                if(allot >= arr[i] && allot >= mx_t)
                {
                    ch2 = true;
                    break;
                }   
                else
                {
                    long long nm = arr[i];
                    long long subt = 1 , al2 = allot;
                    if(nm%9 == 0)
                    {
                    while(nm > allot && allot >= 3 && nm>=3)
                    {
                        nm -=3;// (nm+1)/2;
                        allot-= subt;
                        //subt *= 2;
                    } 
                    //cout<<nm<<" "<<allot<<endl ; 
                    }
                    else
                    {
                    while(nm > allot && allot >= 0)
                    {
                        nm = (nm+1)/2;
                        allot-= subt;
                        subt *= 2;
                    }
                    }
                    if(nm <= allot && allot >= mx_t)
                    {
                        ch2 = true;
                        mx_t = max(nm , mx_t);
                    }
                    //cout<<ch<<endl;
                    
                    
                }
            }
            
            
                    
            //cout<<lo<<" "<<mid<<" "<<hi<<" "<<ch<<endl;
            if(ch == false && ch2 == false)
                lo = mid+1;
            else
            {
                ans = min(ans , mid);
                hi = mid;
            }
        } 
        cout<<"Case #"<<cs<<": "<<min(ans,mx)<<endl;
        cs++;
    }
    return 0;
}