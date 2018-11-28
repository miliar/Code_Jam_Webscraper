#include<iostream>
#include<cmath>
#include<cstdio>

using namespace std;



int main()
{
    int a[10][10],b[10][10];
    int i,j,k,l,m,n,t,r1,r2,tmp;
    cin>>n;
    for(t=1; t<=n; t++)
    {
        cin>>r1;
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                cin>>a[i][j];
            }
        }
        cin>>r2;
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                cin>>b[i][j];
            }
        }
        tmp=0;
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                if(a[r1-1][i]==b[r2-1][j])
                {
                    tmp+=1;
                    k=a[r1-1][i];
                }
            }

        }
        if(tmp==1)
        {
            cout<<"Case #"<<t<<": "<< k<<endl;
        }
        else if(tmp>1)
        {
            cout<<"Case #"<<t<<": "<< "Bad magician!"<<endl;
        }
        else if(tmp==0)
        {
            cout<<"Case #"<<t<<": "<< "Volunteer cheated!"<<endl;
        }
    }
    return 0;

}


