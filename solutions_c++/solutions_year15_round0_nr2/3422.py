#include<iostream>
#include<climits>
#include<cmath>
using namespace std;

int pre[1001][1001];

int _split(int a, int x)
{
    if(a%x==0)
	return a/x-1;
    else
	return a/x;
}

int main()
{
    int T;cin>>T;
    for(int t=0;t<T;t++)
    {
	int D;cin>>D;
	int arr[1000];
	int maxVal=0;
	for(int i=0;i<D;i++)
	{
	    cin>>arr[i];
	    if(arr[i]>maxVal)
		maxVal=arr[i];
	}

	int ans=INT_MAX;

	for(int x=1;x<=maxVal;x++)
	{
	    int curr=x;
	    for(int i=0;i<D;i++)
		if(arr[i]>x)
		    curr+=_split(arr[i],x);
	    if(curr<ans)
		ans=curr;
	}

	cout<<"Case #"<<t+1<<": "<<ans<<endl;
    }
    return 0;
}
