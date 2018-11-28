#include<iostream>
#include<algorithm>
using namespace std;

#define MAX 1000000
long long int min(long long int a, long long int b)
{
    if(a<b)
    {
        return a;
    }
    return b;
}

long long int  compute(long long int arr[], int currsize, int  left_ind, int right_ind, long long int counter)
{
    if(left_ind>right_ind)
    {
        return counter; 
    }

    if(currsize > arr[left_ind])
    {
        return compute(arr,currsize+arr[left_ind], left_ind+1, right_ind, counter);
    }
    if(left_ind == right_ind)
    {
        return counter+1;
    }
    if(currsize==1)
    {
        return compute(arr,currsize,left_ind,right_ind-1,counter+1);
    }
    return min(compute(arr,2*currsize-1,left_ind, right_ind, counter+1), compute(arr,currsize, left_ind, right_ind-1,counter+1));
    
}


int main()
{
    long long int arr[MAX+1];
    int t;
    cin>>t;
    for(int i=1;i<t+1;i++)
    {
        long long int size,num;
        cin>>size>>num;
        for ( int j=0;j<num;j++)
        {
            cin>>arr[j];
        }
        std::sort(arr,arr+num);

        long long int ans = compute(arr,size, 0, num-1, 0);
        cout<<"Case #"<<i<<": "<<ans<<endl; 
    }
    return 0;
}
