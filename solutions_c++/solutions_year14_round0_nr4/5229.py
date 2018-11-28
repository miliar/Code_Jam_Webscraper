#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string.h>
using namespace std;
//Google Code Jam - Qual - 4  (Small)
double arr1[1009],arr2[1009];
int main()
{
    int t,n,x,i;
	cin>>t;
	for(x=1;x<=t;x++)
    {
        cin>>n;
        for(i=0;i<n;i++)
            cin>>arr1[i];
        for(i=0;i<n;i++)
            cin>>arr2[i];
        sort(arr2,arr2+n);
        sort(arr1,arr1+n);
        int ans1=0,ans2=0;
        int fs=0,ss=0;
        while(fs<n && ss<n)
        {
            if(arr1[fs]<arr2[ss])
             ans2++,fs++,ss++;
            else
             ss++;
        }
        fs=0;
        ss=0;
        while(fs<n && ss<n)
        {
            if(arr1[fs]>arr2[ss])
             ans1++,fs++,ss++;
            else
             fs++;
        }
        cout<<"Case #"<<x<<": "<<ans1<<" "<<n-ans2<<endl;
    }

	return 0;
}
