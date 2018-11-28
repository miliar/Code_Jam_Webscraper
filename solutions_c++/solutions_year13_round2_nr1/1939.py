#include<iostream>
#include<stdio.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<stdlib.h>
#include<string.h>
#include<cstring>
#include<cmath>
#include<sstream>

using namespace std;
vector<int> arr;
int n;
int dp[105];

int findmin(int i, int a){
    if(i>=n)
      return dp[i]=0;
    if(dp[i]!=-1)
       return dp[i];
    
    if(arr[i]<a){
          return dp[i]=findmin(i+1,a+arr[i]);       
    }
    
   // cout<<"ingayaavathu"<<endl;
    int minn=n-i;    
    if(a>1){    
     // cout<<"here"<<endl;
       int steps=0,aa=a;
       while(aa<=arr[i]){
              aa=aa+aa-1;
              steps++;         
       }
      // cout<<aa<<" "<<steps<<endl;
       minn=min(minn,steps+findmin(i+1,aa+arr[i]));
    }
    return dp[i]=minn;
}


int main(){
    int t,c=1,a,i,temp;
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    cin>>t;
    while(t--){
       arr.clear();        
       memset(dp,-1,sizeof(dp));        
       cin>>a>>n;      
       for(i=0;i<n;i++){
         cin>>temp; arr.push_back(temp);
       }
       sort(arr.begin(),arr.end());
             

       cout<<"Case #"<<c++<<": "<<findmin(0,a)<<endl;  
    }
    
    return 0;
}
