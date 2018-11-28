#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int tc,n1,n2,k;
    int arr1[4],arr2[4];
    bool yes=0,no=0,ch=0;
    cin>>tc;
    for(int tc_c=1;tc_c<=tc;tc_c++)
    {
           yes=0,no=0,ch=0;
           cin>>n1;
           n1--;
           for(int i=0;i<4;i++)
           {
                   for(int j=0;j<4;j++)
                   {
                           if(i==n1) cin>>arr1[j];
                           else cin>>k;
                   }
           }
            cin>>n2;
           n2--;
           for(int i=0;i<4;i++)
           {
                   for(int j=0;j<4;j++)
                   {
                           if(i==n2) cin>>arr2[j];
                           else cin>>k;
                   }
           }
                
           int ans =0;
           for(int i=0;i<4;i++)
           {
                   for(int j=0;j<4;j++)
                   {
                          
                           //if(i==j) continue;
                          // cout<<"arr[i] " <<arr1[i]<<"  "<<arr2[j]<<endl;
                           if(arr1[i]==arr2[j])
                           {
                                              // cout<<"yes"<<endl;
                                               
                                               if(yes==0)
                                               {
                                                         yes=1;
                                                         ans = arr1[i];
                                               }else
                                               {
                                                    ch = 1;
                                                    break;
                                               }
                           }
                   }
           }
           
           if(ch==1) cout<<"Case #"<<tc_c<<": Bad magician!"<<endl;
           else if(yes) cout<<"Case #"<<tc_c<<": "<<ans<<endl;
           else  cout<<"Case #"<<tc_c<<": Volunteer cheated!"<<endl;
    }
    
    return 0;   
}
