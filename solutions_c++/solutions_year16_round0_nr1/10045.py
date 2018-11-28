#include<bits/stdc++.h>
using namespace std;
int arr[11];
bool check()
{
    for(int i=0;i<10;i++)
		if(arr[i]==0)
			return false;
	return true;
}
int main()
{
    int t;
    cin>>t;
    int index=1;
    while(t--)
	{
		memset(arr,0,sizeof(arr));
        long int n;
        cin>>n;
        if(n==0)
		{
			cout<<"Case #"<<index<<": INSOMNIA\n";
			index++;
			continue;
		}
		int multiple=1;
        while(1)
		{
			long long int temp=n*multiple;
            while(temp>0)
			{
                arr[temp%10]=1;
                temp/=10;
			}
			if(check())
			{
				cout<<"Case #"<<index<<": "<<n*multiple<<endl;
				break;
			}
			else
				multiple++;
		}
	index++;
	}
	return 0;
}
