#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>

using namespace std;

class magic{

    private:


    public:
    string cards(int r1, int r2, int a[4][4], int b[4][4])
    {
        ostringstream temp;

        int i,j;
        int n=4;
        int count = 0;
        int num = 0;
        for(i=0;i<n;i++ )
        {
            int A1 = a[r1-1][i];
            for(j=0;j<n;j++)
            {
                if(A1 == b[r2-1][j])
                {
                    num = A1;
                    count ++;
                }
            }
        }
        if(count == 1)
        {
            temp<<num;
            return temp.str();
        }else
        {
            if(count > 1)
            {
                return "Bad magician!";
            }
            else{ return "Volunteer cheated!"; }
        }
    }


};

int main(){

    magic object;
    ifstream input("A-small-attempt0.in");
    ofstream output("outputs.txt");

    int n = 4;
    int A[4][4];
    int B[4][4];
    int T;
    int row1;
    int row2;
    int c = 1;
    int i,j;

    input >> T;

    while (c <= T)
    {
        input >> row1;
        for (i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                input >> A[i][j];
            }
        }
        input >> row2;
        for (i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                input >> B[i][j];
            }
        }

        string x = object.cards(row1, row2, A, B);

        output << "case #" << c << ": " << x << endl;
        c++;
    }


    return 0;
}



