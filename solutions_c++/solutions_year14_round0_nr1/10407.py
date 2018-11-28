#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <sstream>
#include <vector>
#include <iomanip>
#include <cmath> 

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define MAX 100010
#define MOD 1000000007    
int main()
{
    ios::sync_with_stdio(false);
    int t,n,m,cnt=0;
    cin>>t;
    int arr[5][5];
    int arr1[5][5];
    for(int k=1;k<=t;k++)
    {
        cout<<"Case #"<<k<<": ";
    	cnt++;
    	int pos=0,pos1=0;
    cin>>n;
    for(int i=1;i<=4;i++)
      	for(int j=1;j<=4;j++)
  		    cin>>arr[i][j];
    cin>>m;
    for(int i=1;i<=4;i++)
       	for(int j=1;j<=4;j++)
  		    cin>>arr1[i][j];
    
    int num=0,indx=0,ans=0;
    for(int i=1;i<=4;i++)
    {
        num=arr[n][i];
        for(int j=1;j<=4;j++)
        {
            if(num==arr1[m][j])
                ans++;
            if(ans==1 and num==arr1[m][j])
                indx=j;
        }
    }
    if(ans==1)
        cout<<arr1[m][indx]<<endl;
    else if(ans==0)
        cout<<"Volunteer cheated!"<<endl;
        else
            cout<<"Bad magician!"<<endl;
    }
    return 0;
}


