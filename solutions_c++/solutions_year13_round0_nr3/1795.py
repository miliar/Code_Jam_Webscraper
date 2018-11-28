#include<iostream>
using namespace std;
long long int pal[1000000];
int k=1;
int check(long long int n)
{
    int i,j,temp[200];
    for(i=0;n>0;i++)
    {
        temp[i]=n%10;
        n/=10;
    }
    for(j=0;j<=(i-1)/2;j++)
    {
        if(temp[j]!=temp[i-1-j])
        break;
    }
    if(j==(i-1)/2+1)
    return 1;
    else
    return 0;
}
long long int atoi(int temp[],int lb,int ub)
{
    long long int ans=0;
    for(int i=ub;i>=lb;i--)
    {
        ans=ans*10+temp[i];
    }
    return ans;
}
long long int highpal(long long int n)
{
    int temp[101],j=0,k,i;
    for(i=0;n>0;i++)
    {
        temp[i]=n%10;
        n/=10;
        if(temp[i]==9)
        j++;
    }
    if(j==i)
    {
        temp[0]=temp[i]=1;
        for(int p=1;p<j;p++)
        temp[p]=0;
        return (atoi(temp,0,i));
    }
    else
    {
        j=(i-1)/2;
        k=i-1-j;
        while(temp[j]==9)
        {
            j--;
        }
        temp[j]=temp[i-1-j]=temp[j]+1;
        for(int p=j+1;p<=(i-1)/2;p++)
        {
            temp[p]=temp[i-1-p]=0;
        }
        return (atoi(temp,0,i-1));
    }
}
int main()
{
    pal[0]=1;
    while(1)
    {
        pal[k]=highpal(pal[k-1]);
        //cout<<pal[k]<<"  ";
        if(pal[k]>10000000)
        break;
        k++;
    }
    //cout<<k;
    int t;
    cin>>t;int i=1;
    while(t--)
    {
        long long int A,B,ans1=0,ans2=0;
        cin>>A>>B;
        for(int i=0;pal[i]*pal[i]<=A-1;i++)
        {
            if(check(pal[i]*pal[i]))
            ans1++;
        }
        for(int i=0;pal[i]*pal[i]<=B;i++)
        {
            if(check(pal[i]*pal[i]))
            ans2++;
        }
        //cout<<k;
        //cout<<"\n"<<pal[1098];
        cout<<"Case #"<<i<<": "<<ans2-ans1<<endl;
        i++;
    }
    return 0;
}
