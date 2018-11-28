#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int cases;
    cin>>cases;

    for(int i = 0; i < cases; i++)
    {
        cout<<"Case #"<<i+1<<": ";
        bool numbers[17];
        int count=0;
        int val;

        for(int j = 0; j < 17; j++)
            numbers[j]=false;

        int row;
        cin>>row;
        int k;
        int thrash;

        for(k = 1; k < row; k++)
            cin>>thrash>>thrash>>thrash>>thrash;

        for(k = 0; k < 4; k++)
        {
            int aux;
            cin>>aux;
            numbers[aux]=true;
        }

        for(k = row + 1;k <= 4; k++)
            cin>>thrash>>thrash>>thrash>>thrash;

        cin>>row;

        for(k = 1; k < row; k++)
            cin>>thrash>>thrash>>thrash>>thrash;

        for(k = 0; k < 4; k++)
        {
            int aux;
            cin>>aux;
            if(numbers[aux])
            {
                count++;
                val=aux;
            }
        }

        for(k = row + 1; k <= 4; k++)
            cin>>thrash>>thrash>>thrash>>thrash;

        if(count == 0)
            cout<<"Volunteer cheated!"<<endl;
        else if(count == 1)
            cout<<val<<endl;
        else
            cout<<"Bad magician!"<<endl;
    }
    return 0;
}
