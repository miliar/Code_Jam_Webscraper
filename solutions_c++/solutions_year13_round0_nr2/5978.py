#include <iostream>
using namespace std;
int main()
{
    int t,n,m,cas=0;
    cin>>t;
    while(t--)
    {
        cas++;
        cin>>n>>m;
        int arr[n][m];
        int arrc[n][m];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cin>>arr[i][j];
                arrc[i][j]=2;
            }
        }
        for(int i=0;i<m;i++)
        {
            bool flag=true;
            if(arr[0][i]==1)
            {
                for(int j=0;j<n;j++)
                {
                    if(arr[j][i]!=1)
                    {
                        flag=false;
                        break;
                    }
                }
                if(flag)
                {
                    for(int j=0;j<n;j++)
                        arrc[j][i]=1;
                }
            }
        }
        for(int i=0;i<n;i++)
        {
            bool flag=true;
            if(arr[i][0]==1)
            {
                for(int j=0;j<m;j++)
                {
                    if(arr[i][j]!=1)
                    {
                        flag=false;
                        break;
                    }
                }
                if(flag)
                {
                    for(int j=0;j<m;j++)
                        arrc[i][j]=1;
                }
            }
        }
        bool is=true;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(arr[i][j]!=arrc[i][j])
                {
                    is=false;
                    break;
                }
            }
            if(!is)
              break;
        }
        if(is)
            cout<<"Case #"<<cas<<": YES"<<endl;
        else
            cout<<"Case #"<<cas<<": NO"<<endl;
    }
        return 0;
}