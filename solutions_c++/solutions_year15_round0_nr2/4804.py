#include<bits/stdc++.h>
using namespace std;

int Size,arr[1003];
int Fsize,frr[1003];
bool func(int special,int mid)
{
    while(Size<1000)
    {
        Size++;
        arr[Size]=0;
    }
    Fsize=0;
    for(int i=1; i<=Size; i++)
    {
        if(arr[i]<=mid)
        {
          
        }
        else if(arr[i]>mid)
        {
            int diff=arr[i]-mid;
            Fsize++;
            frr[Fsize]=diff;
            
        }
    }
    int idx=1;
    while( idx<=Fsize )
    {
        if(frr[idx]>0 && special==0)
        {
            return false;
        }
        if(mid>=frr[idx])
        {
            idx++;
            special--;
            
        }
        else
        {
            frr[idx]-=mid;
            special--;
        }
    }
    return true;
}
int main()
{
    int t,D,P,c;
    scanf("%d",&t);
    c=0;
    while(t--)
    {
        c++;
        Size=0;
        scanf("%d",&D);
        for(int i=1; i<=D; i++)
        {
            scanf("%d",&P);
            Size++;
            arr[Size]=P;
        }
        int ans=1000006;
        for(int special=0; special<=1000; special++)
        {
            int low,up,mid;
            low=1;
            up=1000;
            while(low<up)
            {
                mid=low+(up-low)/2;
                bool fnd;
                fnd=func(special,mid);
      
                if(fnd==false)
                {
                    low=mid+1;
                }
                else
                {
                    up=mid;
                }
            }
            if(special+low<ans)
            {
                ans=special+low;
            }
        }
        printf("Case #%d: %d\n",c,ans);
    }
    return 0;
}

