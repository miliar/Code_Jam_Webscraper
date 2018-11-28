#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int va1,va2;
    int i,j,k,p,q,x;
    int a1[4][4]={'0'},a2[4][4]={'0'};
    int count;
    for(i=0;i<t;i++)
    {
        va1=0;
        va2=0;
        count=0;
        cin>>va1;
        va1=va1-1;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                cin>>a1[j][k];
            }
        }
        cin>>va2;
        va2=va2-1;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                cin>>a2[j][k];
            }
        }

            j=va1;
            x=va2;
            for(p=0;p<4;p++)
            {
                for(q=0;q<4;q++)
                {
                    if(a1[j][p]==a2[x][q])
                        count++;
                }
            }
            cout<<'\n';
            if(count==1)
            {
                for(p=0;p<4;p++)
            {
                for(q=0;q<4;q++)
                {
                    if(a1[j][p]==a2[x][q])
                        cout<<"case #"<<i+1<<": "<<a1[j][p];
                }
            }   
            }
            else if(count==0)
            {
                cout<<"case #"<<i+1<<": "<<"Volunteer cheated!";
            }
            else if(count>1)
                cout<<"case #"<<i+1<<": "<<"Bad magician!";
    }
    cout<<'\n'; 
return 0;
}
