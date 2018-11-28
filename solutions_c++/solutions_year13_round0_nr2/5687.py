#include<iostream>
#include<cstdio>
using namespace std;

int a[100][100];

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("b.txt","w",stdout);
    int t;                                            //number of test cases
    cin>>t;
    int N,M;                                          //N=row, M=col
    for(int i=1;i<=t;i++)
    {
        cin>>N>>M;
        for(int j=0;j<N;j++)
        {
            for(int k=0;k<M;k++)
            {
                cin>>a[j][k];
            }
        }

        int noflag=0;
        for(int j=0;j<N;j++)
        {
            int small=a[j][0];
            for(int k=0;k<M;k++)                        //searching for the smallest number in a row
            {
                if(small > a[j][k])
                    small=a[j][k];
            }
            for(int k=0;k<M;k++)
            {
                if(small==a[j][k])
                {
                    //i ve to check the row or the column all have the same value.
                    //first check all the value of the row
                    int sameRowflag=1;
                    for(int p=0;p<M;p++)
                    {
                        if(small!=a[j][p])
                        {
                            sameRowflag=0;
                            break;
                        }
                    }
                    int sameColFlag = 1;
                    for(int p=0;p<N;p++)
                    {
                        if(small!=a[p][k])
                        {
                            sameColFlag=0;
                            break;
                        }
                    }
                    if(sameColFlag==1 || sameRowflag==1)
                        ;
                    else
                    {
                        cout<<"Case #"<<i<<": NO"<<endl;
                        noflag=1;
                        break;
                    }
                }
            }
            if(noflag==1)
                break;
        }
        if(noflag==0)
            cout<<"Case #"<<i<<": YES"<<endl;
    }
}
