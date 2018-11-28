#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t;
    ifstream inp("A-small-attempt1.in");
    ofstream out("out.txt");
    inp >> t;
    int k,h;
    int a[5][5];
    int b[5][5];
    for (int i=1; i<=t; i++)
    {
        inp >> k;
        for (int j=1; j<=4; j++)
            for (int z=1; z<=4; z++)
                {
                    inp >> a[j][z];
                }
        inp >> h;
        for (int j=1; j<=4; j++)
            for (int z=1; z<=4; z++)
                {
                    inp >> b[j][z];
                }
        int sum;
        int rez;
        sum=0;
        rez=0;
        for (int j=1; j<=4; j++)
            for (int z=1; z<=4; z++)
            {
                if (a[k][j]==b[h][z])
                {
                    sum++;
                    rez=a[k][j];
                }
            }
        if (sum==0) out << "Case #" << i << ": " << "Volunteer cheated!" << endl;
            else if (sum>1) out << "Case #" << i << ": " << "Bad magician!" << endl;
            else out << "Case #" << i << ": " << rez << endl;
    }
    return 0;
}
