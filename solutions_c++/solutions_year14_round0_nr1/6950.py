#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    //freopen("A-small-attempt1.txt","r",stdin);
    //freopen("A_output.txt","w",stdout);
    int T;
    cin>>T;
    int ans1,ans2,temp,count,result;
    int arr1[4],arr2[4];
    for(int t=1;t<=T;t++)
    {
        cin>>ans1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if((i+1)==ans1)
                    cin>>arr1[j];
                else
                    cin>>temp;
            }
        }

        cin>>ans2;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if((i+1)==ans2)
                    cin>>arr2[j];
                else
                    cin>>temp;
            }
        }

        count=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(arr1[i]==arr2[j]){
                    count++;
                    result = arr1[i];
                }
            }
        }
        if(count==0)
            cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
        else if(count==1)
            cout<<"Case #"<<t<<": "<<result<<endl;
        else
            cout<<"Case #"<<t<<": Bad magician!"<<endl;
    }
}
