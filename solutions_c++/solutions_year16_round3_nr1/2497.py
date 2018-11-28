#include <iostream>
#include <string.h>
#include <set>
#include <stdio.h>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <iterator>
#include <queue>
#include <map>
#include <stack>

using namespace std;
long long int arr[27];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    long int i,ind1,lux=1,num,t;
    scanf("%ld",&t);
    while(t--)
    {
        long long int sum=0,maxi1=-99999999999,maxi2=-999999999999,ind2;
        cin>>num;
        for(i=0;i<num;i++)
        {
            cin>>arr[i];
            sum+=arr[i];
        }
        cout<<"Case #"<<lux<<": ";
        if(num==1)
        {
            while(sum>=2)
            cout<<"AA"<<" ",sum-=2;
            if(sum>0)
            cout<<"A"<<" ",sum-=1;
        }
        else if(num>=2)
        {
            while(sum>0)
            {
                for(i=0;i<num;i++)
                {
                if(maxi1<=arr[i])
                {
                maxi1=arr[i];
                ind1=i;
                }
                }
                for(i=0;i<num;i++)
                {
                    if(i!=ind1)
                    {
                        if(maxi2<=arr[i])
                        {
                            maxi2=arr[i];
                            ind2=i;
                        }
                    }
                }
                if(maxi1==maxi2&&maxi1!=1)
                {
                    arr[ind1]-=1;
                    arr[ind2]-=1;
                    sum-=2;
                    
                    cout<<(char)('A'+ind1)<<(char)('A'+ind2)<<" ";
                }
                if(maxi1==maxi2&&maxi1==1)
                {
                    if(sum%2==0)
                    {
                    arr[ind1]--;
                    arr[ind2]--;
                    sum-=2;
                
                    cout<<(char)('A'+ind1)<<(char)('A'+ind2)<<" ";
                    }
                    else
                    {
                    arr[ind1]--;
                    sum-=1;
                    
                    cout<<(char)('A'+ind1)<<" ";
                    }
                }
                else if(maxi1!=maxi2)
                {
                    arr[ind1]-=2;
                    sum-=2;
                    cout<<(char)('A'+ind1)<<(char)('A'+ind1)<<" ";
                }
                maxi1=-9999999999;
                maxi2=-9999999999;
            }
        }
        cout<<endl; 
        lux++;
        }
    
return 0;
}


