#include<iostream>
#include<cstdio>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>

using namespace std;

int main()
{

    int T;

    cin>>T;
    for(int caseno=1;caseno<=T;caseno++)
    {
        int arr[100+10][100+10],fail=0,pass=1;
        int n,m;

        cin>>n>>m;

        int a,b;
        a=5;
        b=100;

        a=(a+b);
        b=a-b;


        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cin>>arr[i][j];
            }
        }

        int c=a+b;

        int i,j,k;

        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                fail=0;
                for( k=0;k<m;k++)
                {
                    if(arr[i][k]>arr[i][j])
                    {
                        fail=1;

                        c+=5;

                        break;
                    }
                }
                if(fail==1)
                for( k=0;k<n;k++)
                {
                    if(arr[k][j]>arr[i][j])
                    {
                        fail=1;
                        a++;
                        break;
                    }
                }
                if(k==n)
                    fail=0;
                if(fail==1)
                {
                    pass=0;
                    b++;
                    i=n+1;
                    break;
                }
            }
        }

        if(pass)
            cout<<"Case #"<<caseno<<": YES"<<endl;
        else cout<<"Case #"<<caseno<<": NO"<<endl;



    }
}
