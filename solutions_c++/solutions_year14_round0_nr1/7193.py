#include<iostream>
#include<stdio.h>
#define SIZE 4

using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    //freopen("output.out","w",stdout);
    int t,k,r1,r2,i,j;
    int A[SIZE][SIZE];
    int temp1[SIZE],temp2[SIZE];
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>r1;
        for(i=0;i<SIZE;i++)
        {
            for(j=0;j<SIZE;j++)
            {
                cin>>A[i][j];
                if(i==r1-1)
                {
                    temp1[j]=A[i][j];
                }
            }
        }
        cin>>r2;
        for(i=0;i<SIZE;i++)
        {
            for(j=0;j<SIZE;j++)
            {
                cin>>A[i][j];
                if(i==r2-1)
                {
                    temp2[j]=A[i][j];
                }
            }
        }
        int NUM[17]={0};
      //  cout<<"k";
        for(i=0;i<4;i++)
        {
            NUM[temp1[i]]++;
            NUM[temp2[i]]++;
        }
        bool found=false;
        bool bad=false;
        int common;
        for(i=1;i<=16;i++)
        {
            if(NUM[i]==2)
            {
                if(found==true)
                    {
                        bad=true;
                    }
                found=true;
                common=i;
            }
        }
        if(found==true && bad==true)
        {
            cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
        }
        else if(found==true && bad==false)
        {
            cout<<"Case #"<<k<<": "<<common<<endl;
        }
        else
        {
            cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
        }
    }

return 0;
}
