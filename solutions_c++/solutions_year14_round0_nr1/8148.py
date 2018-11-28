#include<iostream>
using namespace std;

int main()
{

int arr1[4][4]={{0}};
int arr2[4][4]={{0}};
int t;
cin>>t;
int p=1;
while(p<=t)
{
    int arr3[17]={0};
    int r;
    cin>>r;

    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            cin>>arr1[i][j];
        }
    }

 for(int j=0;j<4;j++)
{
    arr3[arr1[r-1][j]]++;
}

int n;
cin>>n;

 for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            cin>>arr2[i][j];
        }
    }

int sum=0;
int ans=-1;
 for(int j=0;j<4;j++)
{
    if(arr3[arr2[n-1][j]]!=0)
    {
        ans=arr2[n-1][j];
    }

    sum=sum+arr3[arr2[n-1][j]];
}


if(ans==-1)
{
    cout<<"Case #"<<p<<": Volunteer cheated!"<<endl;
}

else if(sum>1)
{
    cout<<"Case #"<<p<<": Bad magician!"<<endl;
}

else if(sum==1)
{
    cout<<"Case #"<<p<<": "<<ans<<endl;
}


p++;
}

    return 0;
}
