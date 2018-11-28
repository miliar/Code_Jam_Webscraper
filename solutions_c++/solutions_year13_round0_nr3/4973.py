#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

fstream fin,fout;
int T;
int a,b;
int num;

bool check(int x)
{
    int a[10];
    int j = 0;
    for (int i = 0; i < 10; i++) a[i] = 0;
    while (x > 0)
    {
        a[j] = x % 10;
        x = x / 10;
        j++;
    }
    for (int i = 0; i < j; i++)
        if (a[i] != a[j-1-i]) return false;
    return true;
}

int main()
{
    fin.open("C-small-attempt0 (2).in",ios::in);
    fout.open("c.txt",ios::out);
    fin >> T;
    for (int k = 0; k < T; k++)
    {
        fin >> a >> b;
        num = 0;
        for (int i = int(sqrt(a)); i <= int(sqrt(b))+1; i++)
        {
            if (i*i >= a && i*i <= b && check(i*i) && check(i)) num++;
        }
        fout << "Case #" << k+1 << ": " << num << endl;
    }
    fout.close();
    return 0;
}
