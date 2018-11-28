#include<iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int o = 0;
    while(o < t)
    {
        o++;
        cout<<"Case #"<<o<<": ";
        int f = 0, row;
        int s = 0;
        int a[4][4];
        cin>>row;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                cin>>a[i][j];
        for (int i=0;i<4;i++)
            f = f | (1 << a[row - 1][i]);
        cin>>row;        
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
                cin>>a[i][j];
        for (int i=0;i<4;i++)
            s = s | (1 << a[row - 1][i]);
        
        int add = (f & s);

        if (__builtin_popcount(add) == 1)
        {
            for (int i=1;i<=16;i++)
                if (add & (1<<i))
                    cout<<i<<endl;
        }
        else if (__builtin_popcount(add) == 0)
            cout<<"Volunteer cheated!"<<endl;
        else
            cout<<"Bad magician!"<<endl;
            
    }   
    return 0;
}
