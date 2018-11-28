#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream fil;
    ofstream file2;
    file2.open("out.txt");
    fil.open("A-small-attempt1.in");
    int t;
    fil>>t;
    for(int ct=1;ct<=t;ct++)
    {
        int a;
        fil>>a;
        int arr[4][4];
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            fil>>arr[i][j];
        }
        int b;
        fil>>b;
        int arr2[4][4];
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                fil>>arr2[i][j];
            }
        }
        bool check[17]={0};
        int flag=0;
        int i=a-1;
        for(int j=0;j<4;j++)
        {
           check[arr[i][j]]=1;
        }
        i=b-1;
        int ans;
        for(int j=0;j<4;j++)
        {
            if(check[arr2[i][j]]==1)
            {
                flag++;
                ans=arr2[i][j];
            }
        }
        if(flag==1)
        {
            //cout<<"Case #"<<ct<<": "<<ans<<"\n";
            file2<<"Case #"<<ct<<": "<<ans<<"\n";
        }
        else if(flag>1)
        {
            //cout<<"Case #"<<ct<<": Bad magician!\n";
            file2<<"Case #"<<ct<<": Bad magician!\n";
        }
        else
        {
            //cout<<"Case #"<<ct<<": Volunteer cheated!\n";
            file2<<"Case #"<<ct<<": Volunteer cheated!\n";
        }
    }
    fil.close();
    return 0;
}
