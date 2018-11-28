#include <cstdio>
#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.in");
ofstream fout("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.out");

int main()
{
    int t;
    int rownum[17];
    int ans1, ans2;
    int chosen, satisfied_num;
    
    fin>>t;
    for (int i=1;i<=t;i++)
    {
        fin>>ans1;
        for (int r=1; r<=16; r++) rownum[r] = 0;
        for (int r=1; r<=4; r++)
            for (int c=1; c<=4; c++)
            {
                int temp;
                fin>>temp;
                rownum[temp]=r;
            }
        fin>>ans2;
        satisfied_num = 0;
        for (int r=1; r<=4; r++)
            for (int c=1; c<=4; c++)
            {
                int temp;
                fin>>temp;
                if (r == ans2)
                {
                    if (rownum[temp] == ans1)
                    {
                        satisfied_num++;
                        chosen = temp;
                    }
                }
            }
        fout<<"Case #"<<i<<": ";
        if (satisfied_num == 1)
        {
            fout<<chosen<<endl;
        } else if (satisfied_num == 0) {
            fout<<"Volunteer cheated!"<<endl;
        } else
        {
            fout<<"Bad magician!"<<endl;
        }
    }
    return 0;
}
