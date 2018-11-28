#include<iostream>
using namespace std;
int main()
{
    short t,c=0,ans1,ans2,arr1[4][4],arr2[4][4],i,j;
    cin>>t;
    while(c++<t)
    {
        cin>>ans1;
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        cin>>arr1[i][j];
        
        cin>>ans2;
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        cin>>arr2[i][j];

        
        short flag=0,y;
        
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        if(arr1[ans1-1][i]==arr2[ans2-1][j])
        {
            flag++;
            y=arr1[ans1-1][i];
        }
        
        cout<<"Case #"<<c<<": ";
        if(flag==1)
        cout<<y<<endl;
        else if(flag==0)
        cout<<"Volunteer cheated!"<<endl;
        else
        cout<<"Bad magician!"<<endl;
    }
    return 0;
}
