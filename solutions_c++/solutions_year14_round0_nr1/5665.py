#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int t,r1,r2,b1[4][4],b2[4][4];
    int c=1;
    cin>>t;
    while(t--)
    {
        cin>>r1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>b1[i][j];
        cin>>r2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>b2[i][j];
        int ans =0;
        int val = 0;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(b1[r1-1][i] == b2[r2-1][j])
                    ans++,val=b1[r1-1][i];
        if(ans==1)
            cout<<"Case #"<<c<<": "<<val<<endl;
        else if(ans>1)
            cout<<"Case #"<<c<<": Bad magician!"<<endl;
        else
            cout<<"Case #"<<c<<": Volunteer cheated!"<<endl;
        c++;
    }
    return 0;
}
