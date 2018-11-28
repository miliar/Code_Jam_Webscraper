
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <set>

using namespace std;

int rotate_integer( int target, int biggest_power_of_ten )
{
    int low_digit = target%10;
    return (target/10) + low_digit*biggest_power_of_ten;
    
}

int grid[100][100];
int num_rows, num_cols;

int is_finished()
{
    for (int i=0; i<num_rows; i++)
    {
        for (int j=0; j<num_cols; j++)
        {
            if (grid[i][j])
            {
                return 0;
            }
        }
    }
    return 1;
}

int mow()
{
    // Find the lowest spot (or one of them)
    int lowest_pos_row = -1;
    int lowest_pos_col = -1;
    int lowest_pos = 1000;
    for (int i=0; i<num_rows; i++)
    {
        for (int j=0; j<num_cols; j++)
        {
            if ((grid[i][j] != 0) && (grid[i][j] < lowest_pos))
            {
                lowest_pos_row = i;
                lowest_pos_col = j;
                lowest_pos = grid[i][j];
            }
        }
    }

    // Mow the row if we can
    int can_mow_row = 1;
    for (int j=0; j<num_cols; j++)
    {
        if (grid[lowest_pos_row][j] > lowest_pos)
        {
            can_mow_row = 0;;
        }
    }
    if (can_mow_row)
    {
        for (int j=0; j<num_cols; j++)
        {
            grid[lowest_pos_row][j] = 0;
        }
    }

    // Mow the column if we can
    int can_mow_col = 1;
    for (int i=0; i<num_rows; i++)
    {
        if (grid[i][lowest_pos_col] > lowest_pos)
        {
            can_mow_col = 0;;
        }
    }
    if (can_mow_col)
    {
        for (int i=0; i<num_rows; i++)
        {
            grid[i][lowest_pos_col] = 0;
        }
    }

    return can_mow_row | can_mow_col;
}

int main( int argc, char ** argv )
{
    fstream input_file;
    input_file.open( argv[1] );
    int num_lines;
    input_file >> num_lines;

   
    //string current_string;
    // Eat the line that had the number of lines
    //getline( input_file, current_string );

    for (int i=0; i<num_lines; i++)
    {
        input_file >> num_rows >> num_cols;
        for (int j=0; j<num_rows; j++)
        {
            for (int k=0; k<num_cols; k++)
            {
                input_file >> grid[j][k];
            }
        }
/*
if (i == 26)
{
    for (int j=0; j<num_rows; j++)
    {
        for (int k=0; k<num_cols; k++)
        {
            cerr << grid[j][k];
        }
        cerr << endl;
    }

}
*/
        int mow_failed = 0;
        while (!is_finished() && !mow_failed)
        {
            if (!mow())
            {
                mow_failed = 1;
            }
/*
if (i == 26)
{
    for (int j=0; j<num_rows; j++)
    {
        for (int k=0; k<num_cols; k++)
        {
            cerr << grid[j][k];
        }
        cerr << endl;
    }
    cerr << endl << endl;

}
*/
        }
        cout << "Case #" << i+1 << ": ";
        //cerr << "Just finished Case #" << i+1 << ": " << endl;
        if (mow_failed)
        {
            cout << "NO" << endl;
        }
        else
        {
            cout << "YES" << endl;
        }

    }

    input_file.close();

    return 0;

}
