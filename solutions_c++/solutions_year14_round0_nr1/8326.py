#include <iostream>
using namespace std;
int main ()
{

    int t, x, num[4][4], flag[17], br;
    cin>>t;
    for (int g=0;g<t;g++)
    {
        br=0;
        for (int i=0;i<17;i++)
            flag[i]=0;
        cin>>x;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                cin>>num[i][j];
        for (int i=0;i<4;i++)
            flag[num[x-1][i]]=1;
/*
        for (int i=1;i<=16;i++)
            cout<<flag[i]<<' ';
        cout<<endl;*/

        cin>>x;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                cin>>num[i][j];
        for (int i=0;i<4;i++)
            flag[num[x-1][i]]++;

/*        for (int i=1;i<=16;i++)
            cout<<flag[i]<<' ';
        cout<<endl;*/

        for (int i=1;i<=16;i++)
            if (flag[i]==2) {br++; x=i;}
        cout<<"Case #"<<g+1<<": ";
        if (br>1) cout<<"Bad magician!"<<endl;
        else if (br==1) cout<<x<<endl;
        else cout<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
