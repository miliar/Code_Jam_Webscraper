#include <bits/stdc++.h>

using namespace std;

#define all(n) (n).begin(),(n).end()
#define rall(n) (n).rbegin(),(n).rend()

#define mp make_pair
#define pb push_back
#define sz size()
#define FO(i,x) for(ll i=0;i<x;i++)
#define F first
#define S second
#define ll long long
#define ld long double


#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
//  ll dx[]={-2,-2,-1,-1,1,1,2,2}; ll dy[]={-1,1,-2,2,-2,2,-1,1}; // Knight Dir
//  ll dx[]={-1,-1,-1,0,1,1,1,0}; ll dy[]={-1,0,1,1,1,0,-1,-1};  // 8 Dir
//  ll dx[]={0,1,-1,0};  ll dy[]={1,0,0,-1};

int arr[1009];
int main(){   
      READ("A-large.in");
      WRITE("A-large.out");
   int t,n;
   cin>>t;
   int k=1;
   while(t--){
   	  cin>>n;
   	  FO(i,n) cin>>arr[i];
   	  int a=0,b=0,rate=0;
   	  for(int i=1;i<n;i++)
   	     if(arr[i]<arr[i-1]){
   	     	   a=a+arr[i-1]-arr[i];
   	     	   if(arr[i]<arr[i-1]) rate=max(rate , arr[i-1]-arr[i]);
   	     }
   	  for(int i=0;i<n-1;i++) b=b+min(rate,arr[i]);
   	  cout<<"Case #"<<k++<<": "<<a<<" "<<b<<endl;
   }
   return 0;
}
