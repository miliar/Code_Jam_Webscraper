#include<bits/stdc++.h>
using namespace std;
int main()
{
    int m,n,i,j,count1,count2,temp,b;
    freopen("11.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    cin>>n;
    for(i=1;i<=n;i++)
    {
        cin>>m;
        int *a=new int[m];
        for(j=0;j<m;j++)
            cin>>a[j];
        count1=temp=0;
        for(j=0;j<m-1;j++)
        {
            b=a[j]-a[j+1];
            if(b>0)
                count1+=b;
            if(b>temp)
                temp=b;
        }
        count2=0;
        for(j=0;j<m-1;j++){
            if(a[j]<temp)
                count2+=a[j];
            else
                count2+=temp;
        }
        cout<<"Case #"<<i<<": "<<count1<<" "<<count2<<endl;
    }
    return 0;
}
