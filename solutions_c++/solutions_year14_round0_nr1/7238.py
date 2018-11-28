#include <iostream>
#include <fstream>

using namespace std;

ifstream f1 ("A-small-attempt0.in");
ofstream f2 ("a.out");

int T, n, m, a[5][5], b[5][5];

void ci ()
{
    f1>>n;
    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
               f1>>a[i][j];


    f1>>m;
    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
            f1>>b[i][j];

}

void card(int x)
{
    int k=0, ca;

    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
            if (a[n][i]==b[m][j])
            {
                k++;
                ca=a[n][i];
            }

    f2<<"Case #"<<x<<": ";

    if (k==1)
        f2<<ca<<endl;
    else if (k==0)
        f2<<"Volunteer cheated!"<<endl;
    else
        f2<<"Bad magician!"<<endl;

}

int main()
{
    f1>>T;
    for (int i=1; i<=T; i++)
    {
        ci();
        card(i);
    }

    f1.close();
    f2.close();

    return 0;
}
