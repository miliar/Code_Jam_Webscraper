#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream input("input2.txt");
    ofstream output;
    output.open("output2.txt");
    int t;
    input>>t;
    for(int i = 0; i < t; ++i)
    {
        int r1,r2;
        int A[17] = {0};
        int B[17] = {0};
        input>>r1;
        int a;
        for(int j = 0; j < 4; ++j)
        {
            for(int k = 0; k < 4; ++k)
            {
                input>>a;
                if(j+1 == r1)
                    A[a] = 1;
            }
        }
        input>>r2;
        for(int j = 0; j < 4; ++j)
        {
            for(int k = 0; k < 4; ++k)
            {
                input>>a;
                if(j+1 == r2)
                    B[a] = 1;
            }
        }
        int c = 0;
        for(int j = 1; j < 17; ++j)
        {
            if(A[j] == 1 && A[j] == B[j])
            {
                ++c;
                a = j;
            }
        }
        output<<"Case #"<<(i+1)<<": ";
        if(c == 0)
        {
             output<<"Volunteer cheated!";
        }
        else if(c == 1)
        {
            output<<a;
        }
        else
        {
            output<<"Bad magician!";
        }
        output<<endl;
    }
    output.close();
    return 0;
}
