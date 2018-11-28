#include <iostream>
#include <iomanip>
using namespace std;

/*int main()
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
}*/

int nFarm(double C, double F, double X)
{
    double val = X/C - 2/F - 1;
    double aux = val - ((int)val);
    if (val<0)
        return 0;

    if (aux==0)
        return val;

    int a=1;

    return (val+1)/1;
}

int main()
{
    int cases;
    cin>>cases;
    for(int i = 0; i < cases; i++)
    {
        cout<<"Case #"<<i+1<<": ";

        double C, F, X;

        cin>>C>>F>>X;

        int farms = nFarm(C,F,X);

        double val=0.0;
        for (int j = 1; j <= farms; j++)
            val+=C/((j-1)*F + 2);
        val+=X/((farms)*F+2);
        cout<<fixed<<setprecision(7)<<val<<endl;
    }
}
