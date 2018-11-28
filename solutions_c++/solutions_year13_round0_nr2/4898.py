#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;



int main(int argc, char *argv[])
{
    string input_path, output_path;

    if (argc == 1)
    {
        cout << "WARNING: NO INPUT AND OUTPUT FILE GIVEN" << endl;
    }
    else if (argc == 2)
    {
        cout << "WARNING: ONLY ONE PATH GIVEN. BUT WHICH?!" << endl;
    }
    else if (argc == 3)
    {
        // read FILENAMES
        input_path = argv[1];
        output_path = argv[2];
        cout << "IN: " << input_path << ", OUT: " << output_path << endl;
    }


    // Prepare output file
    fstream f_clear;
    f_clear.open(output_path.c_str(), ios::out);
    f_clear << flush;
    f_clear.close();

    fstream f_out;
    f_out.open(output_path.c_str(), ios::out|ios::app);


    int num_test_cases;

    fstream f;
    f.open(input_path.c_str(), ios::in);

    // Get number of test cases
    string first_line;
    getline(f, first_line);
    num_test_cases = atoi(first_line.c_str());

    cout << "----------------------------------------" << endl;
    cout << "num_test_cases = " << num_test_cases << endl;
    cout << "----------------------------------------" << endl;


    // For each testcase
    for (int i=0; i<num_test_cases; i++)
    {
        int N, M;

        string N_M_line;
        getline(f, N_M_line);
        stringstream linestream(N_M_line);
        linestream >> N;
        linestream >> M;

        int lawn [N][M];

        for (int j=0; j<N; j++)
        {
            string line;
            getline(f, line);
            stringstream linestream(line);

            for (int k=0; k<M; k++)
            {
                int value;
                linestream >> value;
                lawn[j][k] = value;
            }
        }


        bool impossible = false;

        // For each square in lawn
        for (int j=0; j<N; j++)
        {
            if (impossible)
            {
                break;
            }

            for (int k=0; k<M; k++)
            {
                // Flags for each square
                bool horizontal_obstacle = false;
                bool vertical_obstacle = false;

                for (int kk=0; kk<M; kk++)
                {
                    if (lawn[j][kk] > lawn[j][k])
                    {
                        horizontal_obstacle = true;
                    }
                }
                for (int jj=0; jj<N; jj++)
                {
                    if (lawn[jj][k] > lawn[j][k])
                    {
                        vertical_obstacle = true;
                    }
                }

                if (horizontal_obstacle && vertical_obstacle)
                {
                    impossible = true;
                    break;
                }
            }
        }

        if (impossible)
        {
            f_out << "Case #" << (i+1) << ": NO" << endl;
        }
        else
        {
            f_out << "Case #" << (i+1) << ": YES" << endl;
        }
    }

    f_out.close();
}









