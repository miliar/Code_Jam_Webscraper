#include<iostream>
#include<cstdio>
#include<queue>
using namespace std;

int arr[1003],d;
int moves(int const_moves)
{
    int ans=0;
    int temp;
    for(int i=1;i<=d;i++)
    {
        if(arr[i]> const_moves){
        ans+=arr[i]/const_moves;
        temp=arr[i]/const_moves;
        if(temp*const_moves==arr[i])
            ans--;
        }
    }
    return ans+const_moves;
}


int main()
{
    //freopen("input2.txt","r",stdin);
    //freopen("output2.txt","w",stdout);
    int t,temp,max,min,temp_min;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        scanf("%d",&d);
        max=0;
        min=3000;
        for(int i=1;i<=d;i++)
        {
            scanf("%d",&temp);
            if(max < temp)
                max=temp;
            arr[i]=temp;
        }
        for(int i=1;i<=max;i++)
        {
            temp_min=moves(i);
           // printf("temp for %d=%d\n4e39",i,temp);
            if(min>temp_min)
                min=temp_min;
        }
        printf("Case #%d: %d\n",i,min);
    }

    return 0;
}

