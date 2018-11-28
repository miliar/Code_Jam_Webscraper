#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int arr1[5][5], arr2[5][5];
    int count=0, p, ans1,ans2,i,j;
    int a; int n;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>n;

    for(int q=1; q<=n; q++)
    {
        count=0;
        fin>>ans1;
        for(i=1; i<=4; i++)
    {
        for(j=1; j<=4; j++)
        {
            fin>>arr1[i][j];
        }
    }


    fin>>ans2;

    for(i=1; i<=4; i++)
    {
        for(j=1; j<=4; j++)
        {
            fin>>arr2[i][j];

        }
    }

    for(i=1; i<=4; i++)
    {
        a=arr1[ans1][i];
        for(j=1; j<=4; j++)
        {
            if(a==arr2[ans2][j])
            {
                count++;
                p=a;
            }
        }
    }

    if(count==1)
    {
        fout<<"Case #"<<q<<": "<<p;
    }
    if(count>1)
    {
        fout<<"Case #"<<q<<": "<<"Bad magician!";
    }
    if(count==0)
    {
        fout<<"Case #"<<q<<": "<<"Volunteer cheated!";
    }
    fout<<"\n";
    }

    return 0;
}
