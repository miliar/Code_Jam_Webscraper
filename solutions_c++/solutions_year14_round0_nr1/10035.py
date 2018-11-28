#include <iostream>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int m = 1; m <= t; m++)
    {
        int data[4][4];
        int n1;
        cin>>n1;
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
                cin>>data[i][j];
        }
        int temp[4];
        for(int i = 0; i < 4; i++)
            temp[i] = data[n1-1][i];
        int n2;
        cin>>n2;
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
                cin>>data[i][j];
        }
        int count = 0;
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                if(temp[i]==data[n2-1][j])
                    count++;
            }
        }
        if(count == 0)
            cout<<"Case #"<<m<<": Volunteer cheated!\n";
        else if(count > 1)
            cout<<"Case #"<<m<<": Bad magician!\n";
        else
        {
            for(int i = 0; i < 4; i++)
            {
                for(int j = 0; j < 4; j++)
                {
                    if(temp[i]==data[n2-1][j])
                    {
                        cout<<"Case #"<<m<<": "<<temp[i]<<"\n";
                        break;
                    }
                }
            }
        }
    }
    return 0;
}
