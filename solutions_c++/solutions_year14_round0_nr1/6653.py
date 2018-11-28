#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    int T;
        cin >> T;
    int i;
        for(i=1;i<=T;i++)
        {
            int A[17]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
            int first;
            cin >> first;
            int j;
                for(j=1;j<=4;j++)
                {
                    int no1,no2,no3,no4;
                    cin >> no1 >> no2 >> no3 >> no4;
                    if(j==first)
                    {
                        A[no1]=1;
                        A[no2]=1;
                        A[no3]=1;
                        A[no4]=1;
                    }
                }
            int second;
            int value=0;
            int value2=0;
            cin >> second;
                for(j=1;j<=4;j++)
                {
                    int no1,no2,no3,no4;
                    cin >> no1 >> no2 >> no3 >> no4;
                    if(j==second)
                    {
                      value = A[no1]+A[no2]+A[no3]+A[no4];
                        if(A[no1]!=0)
                            value2=no1;
                        if(A[no2]!=0)
                            value2=no2;
                        if(A[no3]!=0)
                            value2=no3;
                        if(A[no4]!=0)
                            value2=no4;
                    }
                }
            if(value==1)
            {
                cout<<"Case #"<<i<<": "<<value2<<endl;
            }
            else if(value == 0)
            {
                cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
            }
            else
            {
                cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
            }
        }
}
