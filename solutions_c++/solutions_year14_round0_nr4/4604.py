#include<iostream>
#include<cstdio>
using namespace std;

int merge(double arr[],int left,int right)
{
    int i,j,k=0,mid;
    double temp[right-left+1];
    mid=(left+right)/2;
    if(left<right)
    {
                  mid=(left+right)/2;
                  merge(arr,left,mid);
                  merge(arr,mid+1,right);
    }
    i=left;
    j=mid+1;
    while((i<=mid)&&(j<=right))
    {
                               if(arr[i]<arr[j])
                               {
                                                temp[k]=arr[i];
                                                k++;
                                                i++;
                               }
                               else
                               {
                                   temp[k]=arr[j];
                                   k++;
                                   j++;
                               }
    }
    while(i<=mid)
    {
                 temp[k]=arr[i];
                 k++;
                 i++;
    }
    while(j<=right)
    {
                   temp[k]=arr[j];
                   k++;
                   j++;
    }
    for(i=0;i<k;i++)
                    arr[i+left]=temp[i];
    return 0;
}

int main()
{
    double nao[1005],ken[1005];
    int strt,end,j,x,t,n,i,res1,res2,test;
    #ifndef ONLINE_JUDGE
        freopen("input.cpp","r",stdin);
        freopen("output.cpp","w",stdout);
    #endif // ONLINE_JUDGE
    cin >> test;
    t=1;
    while(t<=test)
    {
        cin >> n;
        for(i=0;i<n;i++)
            cin >> nao[i];
        for(i=0;i<n;i++)
            cin >> ken[i];
        merge(nao,0,n-1);
        merge(ken,0,n-1);
        cout << "Case #" << t << ": ";
        strt=0;
        end=n;
        while(strt<n)
        {
            for(i=0;i<end;i++)
            {
                if(nao[i+strt]<ken[i])
                {
                    break;
                }
            }
            if(i==end)
            {
                break;
            }
            else
            {
                strt++;
                end--;
            }
        }
        res1=n-strt;
        x=0;
        for(i=0;i<n;i++)
        {
            for(j=x;j<n;j++)
            {
                if(ken[j]>nao[i])
                {
                    x=j+1;
                    break;
                }
            }
            if(j==n)
                break;
        }
        res2=n-i;
        cout << res1 << " " << res2 << endl;
        t++;
    }
    return 0;
}
