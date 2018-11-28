#include<iostream>
using namespace std;
int main()
{
    int  n,m,h,tc,arr[102][102],row[102],col[102],max1,max2;
    bool check;
    cin>>tc;
    for(int i=1;i<=tc;++i)
    {
            cin>>n>>m;
            for(int j=0;j<n;++j)
            {
                    for(int z=0;z<m;++z)
                    {
                            cin>>arr[j][z];
                    }
            }
            for(int j=0;j<n;++j)
            {
                    max1=arr[j][0];
                    for(int z=1;z<m;++z)
                    {
                            if(arr[j][z]>max1)
                            max1=arr[j][z];
                    }
                    row[j]=max1;
            }
            for(int z=0;z<m;++z)
            {
                    max1=arr[0][z];
                    for(int j=1;j<n;++j)
                    {
                            if(arr[j][z]>max1)
                            max1=arr[j][z];
                    }
                    col[z]=max1;
            }
            
            check=true;
            for(int j=0;j<n;++j)
            {
                    for(int z=0;z<m;++z)
                    {
                           if(arr[j][z]!=row[j] && arr[j][z]!=col[z])
                            {
                                                check=false;
                                                j=n;
                            }
                    }
            } 
            if(check)
           cout<<"Case #"<<i<<": YES"<<endl;
           else
           cout<<"Case #"<<i<<": NO"<<endl;
    }
    return 0;
}
