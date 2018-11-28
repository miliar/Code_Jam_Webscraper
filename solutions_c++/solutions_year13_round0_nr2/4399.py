#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>

using namespace std;

bool doSomething(int matrix[100][100], int n, int m);

int main(int argc, char* argv[])
{
    int test_cases;
    ifstream fin;
    ofstream fout;
    string input_file = "input.txt";
    if (argc >=2)
        input_file = *(argv+1);
    fin.open(input_file.c_str());
    fin>>test_cases;
    
    fout.open("output.txt");

    int n, m;
    int matrix[100][100];

    for (size_t i= 0; i<test_cases; ++i)
    {
        fin>>n>>m; //get matrix size
        for(size_t j = 0; j< n; ++j) //load matrix
        {

            for(size_t k=0; k<m; ++k)
            {
                fin>>matrix[j][k];
            }
        }
        fout<<"Case #"<<i+1<<": "<<(doSomething(matrix, n, m)?"YES":"NO")<<endl;
    }
    return 0;
}


bool doSomething(int matrix[100][100], int n, int m)
{
    bool possible;
    for(size_t i =0; i<n; ++i)
    {
        for(size_t j=0; j<m; ++j)
        {
            //looking at matrix[n][m], have to check following row/column if legal or not
            possible = true;
            for(size_t a=0; a<n; ++a) //check row
                if (matrix[a][j] > matrix[i][j])
                    possible = false;
            if (possible)
                continue;
            for(size_t b=0; b<m; ++b) //check column
                if (matrix[i][b] > matrix[i][j])
                    return false;
        }
    }

    return true;
}

