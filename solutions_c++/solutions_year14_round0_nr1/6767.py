#include<iostream>

using namespace std;

int main(void)
{
    int T,ans1,ans2,arr1[4][4],arr2[4][4],out,ans;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        cin>>ans1;
        for(int j=0;j<4;j++)
            cin>>arr1[j][0]>>arr1[j][1]>>arr1[j][2]>>arr1[j][3];
        cin>>ans2;
        for(int j=0;j<4;j++)
            cin>>arr2[j][0]>>arr2[j][1]>>arr2[j][2]>>arr2[j][3];
        out=0;
        ans1--;
        ans2--;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                if(arr1[ans1][i]==arr2[ans2][j])
                    {
                        out++;
                        ans=arr2[ans2][j];
                    }
        }
        switch(out)
        {
            case 0: cout<<"Case #"<<t+1<<": Volunteer cheated!"<<endl; break;
            case 1: cout<<"Case #"<<t+1<<": "<<ans<<endl; break;
            default: cout<<"Case #"<<t+1<<": Bad magician!"<<endl; break;
        }

    }
    return 0;
}
