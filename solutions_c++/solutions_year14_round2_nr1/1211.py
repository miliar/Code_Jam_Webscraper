#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int merge(int arr[],int left,int right);

char a[105][105],b[105],ch;
int len[105],pos[105],temp[105];

int main()
{
    int res,test,t,i,j,flag,tem,x,n,mid,y;
    #ifndef ONLINE_JUDGE
        freopen("input.cpp","r",stdin);
        freopen("output.cpp","w",stdout);
    #endif // ONLINE_JUDGE
    scanf("%d",&test);
    t=1;
    while(t<=test)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",a[i]);
            len[i]=strlen(a[i]);
            pos[i]=0;
        }
        x=0;
        res=0;
        flag=0;
        while(1)
        {
            for(i=0;i<n;i++)
            {
                b[i]=a[i][pos[i]];
            }
            ch=b[0];
            for(i=1;i<n;i++)
            {
                if(b[i]!=ch)
                {
                    flag=1;
                    break;
                }
            }
            for(i=0;i<n;i++)
            {
                tem=pos[i];
                while(a[i][pos[i]]==b[i])
                {
                    pos[i]++;
                    if(pos[i]==len[i])
                    {
                        x=1;
                        break;
                    }
                }
                temp[i]=pos[i]-tem;
            }
            merge(temp,0,n-1);
            mid=temp[n/2];
            for(i=0;i<n;i++)
            {
                y=mid-temp[i];
                if(y<0)
                    y=-y;
                res=res+y;
            }
            if(x==1)
            {
                for(i=0;i<n;i++)
                {
                    if(pos[i]!=len[i])
                        break;
                }
                if(i<n)
                    flag=1;
                else
                    break;
            }
            if(flag==1)
                break;
        }
        if(flag==1)
            cout << "Case #" << t << ": Fegla Won" << endl;
        else
            cout << "Case #" << t << ": " << res << endl;
        t++;
    }
}

int merge(int arr[],int left,int right)
{
    int i,j,k=0,mid,temp[right-left+1];
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
                               if(arr[i]<=arr[j])
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
