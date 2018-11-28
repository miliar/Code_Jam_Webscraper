using namespace std;
#include<iostream>
#include<cstdio>
int b[101][101],m,n;
void trim(int max1,int i)
{
    int j;
    for(j=0;j<n;j++)
    {
        b[i][j]=max1;
    }
}
void trim1(int max1,int j)
{
    int i;
    for(i=0;i<m;i++)
    {
        b[i][j]=max1;
    }
}
    int main()
    {
        int t,test=0;
        cin>>t;
        while(t--)
        {
            test++;

        int i,j,a[101][101],max1=-90,flag=0,flag1=0;

        cin>>m>>n;


        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                cin>>a[i][j];
            }
        }
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            max1=max(max1,a[i][j]);

        }
            trim(max1,i);
            max1=-90;

    }
    max1=-90;
    for(j=0;j<n;j++)
    {
        for(i=0;i<m;i++)
        {
            if(a[i][j]!=b[i][j])
            {
                flag=1;
            }
            max1=max(max1,a[i][j]);

        }
        if(flag==1){
        trim1(max1,j);
        flag=0;
        }
        max1=-90;
    }


    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            if(a[i][j]!=b[i][j])
            {
                flag1=1;break;
            }

        }
        if(flag1==1)break;
    }
    if(flag1==0)printf("Case #%d: YES\n",test);
    else printf("Case #%d: NO\n",test);
        }
        return 0;
    }
