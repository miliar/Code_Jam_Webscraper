#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;
bool lawnsmall(int low,int high);
bool compare();
int m,n;
int arr[100][100],result[100][100];

int main()
{
    int T;
    freopen("oplawnlarge.txt","wt",stdout);

    cin>>T;
    int low,high,x=0;
    while(T--)
    {
        x++;
        cin>>m>>n;
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
        {
            cin>>arr[i][j];

        }

        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
        {
            result[i][j] = 100;

        }

        for(int i=100;i>=1;i=i-1)
        {
            high=i;
            low = i-1;
            lawnsmall(low,high);
         }
        if( compare()==1)
               cout<<"Case #"<<x<<": YES"<<endl;
           else
               cout<<"Case #"<<x<<": NO"<<endl;
    }
    return 0;
}

bool lawnsmall(int low,int high){
    bool flag;


        for(int i=0;i<m;i++)
           {
               flag = 1;

                for(int j=0;j<n;j++)
                {
                    if(arr[i][j]<high)
                     {

                     }  // flag = 1;
                    else
                       flag=0;


                }
                if (flag == 1)
                {
                    for(int k=0;k<n;k++)
                        result[i][k]=low;
                }
           }

           for(int j=0;j<n;j++)
           {
               flag = 1;

                for(int i=0;i<m;i++)
                {
                    if(arr[i][j]<high)
                    {

                    }    //flag = 1;
                    else
                        flag =0;


                }
                if (flag == 1)
                {
                    for(int k=0;k<m;k++)
                        result[k][j]=low;
                }
           }
    return 0;
}

bool compare()
{
    bool flag=1;
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
        {
            if(arr[i][j]!=result[i][j]){
                flag=0;
                break;
            }
        }
    return flag;
}
