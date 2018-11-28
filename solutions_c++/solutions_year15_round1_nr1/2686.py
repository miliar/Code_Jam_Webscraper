#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	int t,n,i,arr[1005],pos=1;
    cin>>t;
    while(t--)
    {
   cin>>n;
   for(i=0;i<n;i++)
        cin>>arr[i];

   int fir=0;
    for(i=0;i<n-1;i++)
        if(arr[i+1]<arr[i])
           fir=fir+arr[i]-arr[i+1];

  int maxi=INT_MIN;
    for(i=1;i<n;i++)
         maxi=max(maxi,arr[i-1]-arr[i]);

int sec=0;
for(i=0;i<n-1;i++)
   sec=sec+min(maxi,arr[i]);

 cout<<"Case #"<<pos<<": "<<fir<<" "<<sec<<"\n";
pos++;
    }
	return 0;
}
