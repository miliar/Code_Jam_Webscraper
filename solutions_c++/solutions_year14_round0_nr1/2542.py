#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("data.txt");
ofstream fout("data.out");

int a[5][5], b[5][5];
void display(int a1[], int b1[]);
bool exist(int num, int b1[]);
int main()
{
    int T,i,ans1,ans2,j,k;
    fin >> T;
    for (i = 1; i <= T; ++i)
    {
        fin >> ans1;
        for (j = 1; j <= 4; ++j)
            for (k = 1; k <= 4; ++k)
            {
                fin >> a[j][k];
            }
        fin >> ans2;
        for (j = 1; j <= 4; ++j)
            for (k = 1; k <= 4; ++k)
            {
                fin >> b[j][k];
            }
        fout << "Case #" << i <<": ";
        display(a[ans1], b[ans2]);
    }
    return 0;
}

void display(int a1[], int b1[])
{
    int i,cnt = 0,r;
    for (i = 1; i <= 4; ++i)
    {
        if (exist(a1[i],b1)) {++cnt;r = a1[i];}
    }
    if (cnt == 0) fout<<"Volunteer cheated!"<< endl;
    if (cnt > 1) fout << "Bad magician!" << endl;
    if (cnt == 1) fout << r << endl;
}

bool exist(int num, int b1[])
{
    int i;
    for (i = 1; i <= 4; ++i)
    {
        if (b1[i]==num) return true;
    }
    return false;
}
