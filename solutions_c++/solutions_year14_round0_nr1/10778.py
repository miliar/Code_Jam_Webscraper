#include<iostream>
using namespace std;
int main()
{
    int T,r1,r2,arr1[4][4],arr2[4][4],i,j,cnt=0,k=1,ans;
    cin >> T;
    while(k<=T)
    {
        cnt=0;
        cin >> r1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                cin >> arr1[i][j];
            }
        cin >> r2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                cin >> arr2[i][j];
            }
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                if(arr1[r1-1][i]==arr2[r2-1][j])
                {
                    ans=arr1[r1-1][i];
                    cnt++;
                }
            }
            cout << "case #"<<k<<": ";
            if(cnt==1)
                cout<<ans;
            if(cnt>1)
                cout<<"Bad magician!";
            if(cnt==0)
                cout <<"Volunteer cheated!";
            cout <<endl;
        k++;
    }

    return 0;
}
