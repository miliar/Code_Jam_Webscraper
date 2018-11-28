#include<iostream>
#include<fstream>
using namespace std;

ifstream f("input.txt");
ofstream g("output.txt");

int T;
int N,M,A[17], B[17];

void citire(void)
{
    int a;

    f >> N;

    for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        {
            f >> a;
            A[a] = i;
        }

    f >> M;

    for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        {
            f >> a;
            B[a] = i;
        }
}

int main()
{
    f >> T;
    for(int i=1;i<=T;i++)
    {
        int nr = 0,ans;

        citire();

        for(int j=1;j<=16;j++)
            if(A[j] == N && B[j] == M)
                nr ++,
                ans = j;

        if(!nr)
            g << "Case #" << i << ": Volunteer cheated!\n";
        else if(nr > 1)
            g << "Case #" << i << ": Bad magician!\n";
        else
            g << "Case #" << i << ": " << ans << "\n";
    }
}
