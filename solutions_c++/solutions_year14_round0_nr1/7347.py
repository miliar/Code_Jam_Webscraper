#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
    int T;
    cin>>T;
    int a,b;
    int ar[5][5],br[5][5];
    int match=0;
    int num=0;
    for(int i=0;i<T;i++)
    {
        cin>>a;//1st ans
        for(int j=1;j<5;j++)//row
        {
            for(int k=1;k<5;k++)//column
                cin>>ar[j][k];
        }
        cin>>b;//2nd ans
        for(int j=1;j<5;j++)//row
        {
            for(int k=1;k<5;k++)//column
                cin>>br[j][k];
        }
        for(int ai=1;ai<5;ai++)//column for a
        {
            for(int bi=1;bi<5;bi++)//column for b
            {
                if(ar[a][ai]==br[b][bi])
                {
                    num=ar[a][ai];
                    match++;
                }
            }
        }
        cout<<"Case #"<<i+1<<": ";
        if(match==0)cout<<"Volunteer cheated!";
        else if(match==1)cout<<num;
        else cout<<"Bad magician!";
        cout<<endl;
        match=0;
    }
}
