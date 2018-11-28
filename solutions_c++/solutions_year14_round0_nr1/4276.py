#include<iostream>
#include<cstdio>
#include<cstring>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<cmath>
using namespace std;
int main()
{
    int t,i,j,k,l,m,n,a,b,arr[5][5],arr1[5][5];
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    m=t;
    while(t--)
    {
        cin>>a;
        a=a-1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>arr[i][j];
            }
        }
        cin>>b;
        b=b-1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>arr1[i][j];
            }
        }
        k=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(arr[a][i]==arr1[b][j])
                {
                    l=arr[a][i];
                    k++;
                }
            }
        }		
        cout<<"Case #"<<m-t<<": ";
		if(k==0) 
            cout<<"Volunteer cheated!"<<endl;
		else if(k>1) 
            cout<<"Bad magician!"<<endl;
		else 
            cout<<l<<endl;
    }
    return 0;
}
