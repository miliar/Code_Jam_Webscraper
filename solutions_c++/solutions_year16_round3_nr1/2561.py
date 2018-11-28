#include <bits/stdc++.h>
using namespace std;
struct node
{
    int val;
    char cha;
};
bool myfn(node a,node b)
{
    if(a.val<b.val)
        return true;
    return false;
}
node arr1[27];
bool check(int n)
{
    int sum=0;
    for(int i=0;i<n;i++)
    {
        sum+=arr1[i].val;
    }
    for(int i=0;i<n;i++)
    {
        if(arr1[i].val*2>sum)
            return true;
    }
    return false;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output1.out","w",stdout);
    int t,n,i,j;
    cin>>t;
    int arr[27];
    for(int kalo=0;kalo<t;kalo++)
    {
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
            arr1[i].val=arr[i];
            arr1[i].cha=(char)('A'+(i));
        }
        sort(arr1,arr1+n,myfn);
        cout<<"Case #"<<kalo+1<<": ";
        for(int j=n-1;j>=0;j--)
        {
            for(int i=n-1;i>=0;i--)
            {
                while(arr1[i].val!=0)
                {   arr1[i].val-=1;
                    bool b=check(n);
                    if(b==true)
                    {
                        arr1[i].val+=1;
                        break;
                    }
                    cout<<arr1[i].cha<<" ";
                }
            }
        }
        int pos1=-1,pos2=-1;
        for(int i=0;i<n;i++)
        {
            if(arr1[i].val!=0 && pos1!=-1)
            {
                pos2=i;
                while((arr1[pos1].val--)!=0 && (arr1[pos2].val--)!=0)
                {
                    cout<<arr1[pos1].cha<<arr1[pos2].cha<<" ";
                }
                if(arr1[pos1].val<=0)
                {
                    pos1=-1;
                }
                if(arr1[pos2].val<=0)
                {
                    pos2=-1;
                }
            }
            else if(arr1[i].val!=0 && pos1==-1 && pos2==-1)
            {
                pos1=i;
            }
            else if(arr1[i].val!=0 && pos1==-1 && pos2!=-1)
            {
                pos1=i;
                while((arr1[pos1].val--)!=0 && (arr1[pos2].val--)!=0)
                {
                    cout<<arr1[pos1].cha<<arr1[pos2].cha<<" ";
                }
                if(arr1[pos1].val<=0)
                {
                    pos1=-1;
                }
                if(arr1[pos2].val<=0)
                {
                    pos2=-1;
                }
            }

        }
        cout<<endl;
    }
    return 0;
}

