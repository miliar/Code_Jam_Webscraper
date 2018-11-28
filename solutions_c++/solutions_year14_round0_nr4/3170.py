#include<iostream>
#include<cstdio>
using namespace std;
void merge(double arr[],int left,int right)
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
}
int main()
{
    double naomi[1005],ken[1005];
    int t,k;
    int  n,j,i,start_index,end_index;
    int z,ans1,ans2;
    #ifndef ONLINE_JUDGE
        freopen("input.c","r",stdin);
        freopen("output.c","w",stdout);
    #endif // ONLINE_JUDGE
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        cin>>n;
        for(i=0;i<n;i++)
            cin>>naomi[i];
        for(i=0;i<n;i++)
            cin>>ken[i];
        merge(naomi,0,n-1);
        merge(ken,0,n-1);
        start_index=0;
        end_index=n;
        printf("Case #%d: ",k);
        while(start_index<n)
        {
            for(i=0;i<end_index;i++){
                if(naomi[i+start_index]<ken[i]){
                    break;
                }
            }
            if(i==end_index)break;
            else
            {
                start_index++;
                end_index--;
            }
        }
        ans1=n-start_index;
        z=0;
        for(i=0;i<n;i++)
        {
            for(j=z;j<n;j++)
            {
                if(ken[j]>naomi[i])
                {
                    z=j+1;
                    break;
                }
            }
            if(j==n)
                break;
        }
        ans2=n-i;
        cout<<ans1<<" "<<ans2<<endl;
    }
    return 0;
}
