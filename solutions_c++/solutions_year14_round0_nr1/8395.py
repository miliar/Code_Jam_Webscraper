#include <iostream>
#include <fstream>
using namespace std;




int main()
{
    int testCases;

    ifstream file("in.txt",ios::in);
    ofstream out("out.txt",ios::out);
    file>>testCases;
    int flag[17];
    int temp = 0;
    int answ1, answ2;

    for (int nCase=0; nCase<testCases; nCase++)
    {

        for (int i=0; i<=16; i++)
            flag[i]=0;
        file>>answ1;
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                file >> temp;
                if (i==answ1-1) flag[temp]++;
            }
        }

        file>>answ2;
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                file >> temp;
                if (i==answ2-1) flag[temp]++;
            }
        }

        int result = 0;
        int matchCount = 0;
        for (int i=1; i<=16; i++ )
        {
            if (flag[i]==2)
            {
                result = i;
                matchCount++;
            }
        }
        out << "Case #" << nCase+1 <<": ";
        if (matchCount==1)
            out << result << "\n";
        else if (matchCount>1)
            out << "Bad magician!\n";
        else
            out << "Volunteer cheated!\n";

    }
    file.close();
    out.close();
    cout << "Done!" << endl;
    return 0;
}
