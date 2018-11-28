#include<bits/stdc++.h>
using namespace std;


int sz;
int arr[1010];
int sz2;
int ans_arr[1010];



bool solve(int val,int mid)
{
    sz2=0;

    int diff;
    int idx;

    for(int i=1;i<=sz;i++)
    {
        if(arr[i]>mid)
        {
            diff=arr[i]-mid;
            sz2++;
            ans_arr[sz2]=diff;
        }
    }
    idx=1;
    while(idx<=sz2)
    {
        if(ans_arr[idx]>0&&val==0) return false;
        if(mid>=ans_arr[idx])
        {
            idx++;
            val--;
        }
        else
        {
            ans_arr[idx]-=mid;
            val--;
        }
    }
    return true;
}
int main()
{
    int t,elem;
    int D,P;
    cin>>t;
    for(int T=1;T<=t;T++)
    {
        bool flag;
        sz=0;
        cin>>D;

        int ans=2147483647;

        for(int i=1; i<=D; i++)
        {
            cin>>elem;
            arr[++sz]=elem;
        }


        for(int k=0; k<=1000; k++)
        {
            int low=1,high=1000,mid;

            while(low<high)
            {
                mid=low+(high-low)/2;
                flag=solve(k,mid);

                if(!flag) low=mid+1;

                else high=mid;
            }


            if(k+low<ans) ans=k+low;
        }
        printf("Case #%d: %d\n",T,ans);
    }
    return 0;
}
