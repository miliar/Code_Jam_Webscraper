#include<iostream>
#include<stdio.h>
#include<fstream>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        int a[4];
        int b[4];
        int temp;
        int ans1,ans2;
        cin>>ans1;
        for(int i=0;i<4;i++)
        {
            if(i+1==ans1)
            {
                for(int j=0;j<4;j++)
                {
                    cin>>a[j];
                }
            }
            else
            {
                for(int j=0;j<4;j++)
                {
                    cin>>temp;
                }
            }
        }
        cin>>ans2;
        for(int i=0;i<4;i++)
        {
            if(i+1==ans2)
            {
                for(int j=0;j<4;j++)
                {
                    cin>>b[j];
                }
            }
            else
            {
                for(int j=0;j<4;j++)
                {
                    cin>>temp;
                }
            }
        }
        int count = 0;
        int req = -1;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(a[i]==b[j])
                {
                    count++;
                    req = a[i];
                }
            }
        }
        if(count <= 0)
        {
            cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
        }
        else if(count > 1){
            cout<<"Case #"<<k<<": Bad magician!"<<endl;
        }
        else
        {
            cout<<"Case #"<<k<<": "<<req<<endl;
        }

    }

}
