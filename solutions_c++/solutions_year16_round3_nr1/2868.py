#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
#include<string>

using namespace std;

bool remain(int *arr,int n)
{
    for(int i=0;i<n;i++)
        if(arr[i])
            return true;

    return false;
}

bool choose1(int *arr,int n, int x)
{
    int sum =0;
    for(int i=0;i<n;i++)
        sum+=arr[i];
    sum--;
    arr[x]--;
    int mx =0;

    for(int i=0;i<n;i++)
        if(arr[i]>mx)
            mx=arr[i];

    if(((float)mx)/sum > 0.5)
    {
        arr[x]++;
        return false;
    }

    return true;

}

bool choose2(int *arr,int n, int x ,int y)
{

    int sum =0;
    for(int i=0;i<n;i++)
        sum+=arr[i];
    sum--;
    sum--;
    arr[x]--;
    arr[y]--;
    int mx =0;
    for(int i=0;i<n;i++)
        if(arr[i]>mx)
            mx=arr[i];

    if(((float)mx)/sum > 0.5)
    {
        arr[x]++;
        arr[y]++;
        return false;
    }
    return true;
}
int main()
{
	int t;
    cin>>t;
    int cnt=1;
    while(t--)
    {
        int n;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++)
            cin>>arr[i];
        string s;

        while(remain(arr,n))
        {
            //cout<<remain(arr,n)<<endl;
            for(int i=0;i<n;i++)
            {
                if(arr[i]>0&&choose1(arr,n,i))
                {
                    s+= 'A'+i;
                    s+= ' ';
                    continue;
                }
            }
            for(int i=0;i<n;i++)
                for(int j=0;j<n;j++)
                    if(arr[i]>0&&arr[j]>0&&choose2(arr,n,i,j))
                    {
                        s+='A'+i;
                        s+='A'+j;
                        s+=' ';
                        continue;
                    }
          //cout<<s<<endl;
        }

    	cout<<"Case #"<< cnt++<<": "<<s<<endl;
    }
}