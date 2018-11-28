#include<bits/stdc++.h>
using namespace std;

int Size,arr[1003];
int fr,arr2[1003];
bool soln(int s,int mid);

int main()
{
    int t,D,P,c;
    cin>>t;
    c=0;
    while(t--)
    {
        c++;
        Size=0;
        cin>>D;
        for(int i=1; i<=D; i++)
        {
            scanf("%d",&P);
            Size++;
            arr[Size]=P;
        }
        int ans=1000006;
        for(int s=0; s<=1000; s++)
        {
            int low,up,mid;
            low=1;
            up=1000;
            while(low<up)
            {
		bool rs;
                mid=low+(up-low)/2;
                rs=soln(s,mid);
                
                if(!rs)
                {
                    low=mid+1;
                }
                else
                {
                    up=mid;
                }
           }
            if(s+low<ans)
            {
                ans=s+low;
            }
        }
        printf("Case #%d: %d\n",c,ans);
    }
    return 0;
}

bool soln(int s,int mid)
{
   
    while(Size<1000)
    {
        Size++;
        arr[Size]=0;
    }
    fr=0;
    for(int i=1; i<=Size; i++)
    {
        if(arr[i]<=mid)
        {
         
        }
        else if(arr[i]>mid)
        {
            int diff=arr[i]-mid;
            fr++;
            arr2[fr]=diff;
            
        }
    }
    int idx=1;
    while( idx<=fr )
    {
        if(arr2[idx]>0 && s==0)
        {
            return false;
        }
        if(mid>=arr2[idx])
        {
            idx++;
            s--;
            
        }
        else
        {
            arr2[idx]-=mid;
            s--;
        }
    }
    return true;
}
