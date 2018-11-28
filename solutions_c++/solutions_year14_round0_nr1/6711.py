#include<iostream>
#include<cstdio>
#include<stdlib.h>
#include<iomanip>
#include<math.h>
#include<limits.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int a[4][4]={0};
    for(int k=0;k<t;k++)
    {
                int flag[17];
                memset(flag,0,sizeof(flag));
                for(int l=0;l<2;l++)
                {
                        int n1=0;
                        cin>>n1;
                        for(int i=0;i<4;i++)
                        {
                                for(int j=0;j<4;j++)
                                {
                                        cin>>a[i][j];
                                        if(i==(n1-1))
                                        {
                                             flag[a[i][j]]++;
                                        }        
                                }        
                        }
                }
                int count=0;
                int pos=0;
                for(int i=1;i<=16;i++)
                {
                        if(flag[i]==2)
                        {
                        count++;
                        pos=i;
                        }
                }
                if(count==1)
                {
                cout<<"Case #"<<k+1<<": "<<pos<<endl;
                }
                else if(count>1)
                {
                cout<<"Case #"<<k+1<<": Bad magician!"<<endl;
                }
                else if(count==0)
                {
                cout<<"Case #"<<k+1<<": Volunteer cheated!"<<endl;
                }
    }    
    return 0;

}

