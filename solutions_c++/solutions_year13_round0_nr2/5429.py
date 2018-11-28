#include<iostream>
using namespace std;
int main()
{
    int t,count=0;
    cin>>t;
    while(t--)
    {
        count++;
    	int n,m,flag=1;
    	cin>>n>>m;
        int a[n][m];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cin>>a[i][j];
            }
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(a[i][j]==1)
                {
                    int check=1;
                    for(int k=0;k<m;k++)
                    {
                    	if(a[i][k]!=a[i][j])
                        {
                            check=0;
                            break;
                        }
                    }
                    if(check==0)
                    {
                        check=1;
                        for(int k=0;k<n;k++)
                        {
                            if(a[k][j]!=a[i][j])
                            {
                                check=0;
                            	break;
                            }
                    	}
                    }
                    if(check==0)
                    {
                    	flag=0;
                        break;
                    }
                }
            }
            if(flag==0)
            break;
        }
        cout<<"Case #"<<count<<": ";
        if(flag==0)
        cout<<"NO"<<endl;
        else
        cout<<"YES"<<endl;
    }
    return 0;
}
