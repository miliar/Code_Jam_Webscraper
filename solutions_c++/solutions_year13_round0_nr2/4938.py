#include <iostream>
#include <list>
#include <string>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
using namespace std;

int rows, cols;
int m[500][500];

bool check_col(int cols, int value)
{
    for(int r = 0; r < rows; ++r)
        if(m[r][cols] > value)
            return false;

    return true;
}

bool check_row(int rows, int value)
{
    for(int c = 0; c < cols; ++c)
        if(m[rows][c] > value)
            return false;

    return true;
}

bool calc()
{
    
    for(int r = 0; r < rows; ++r)
        for(int c = 0; c < cols; ++c)
            if(!check_row(r, m[r][c]) && !check_col(c, m[r][c]))
                return false;

    return true;
}

int main()
{
    int test_case;
    cin>>test_case;

    for(int i = 0; i  < test_case ; ++i)
    {
        
        cin>>rows>>cols;
        for(int r = 0; r < rows; ++r)
            for(int c= 0; c< cols; ++c)
                cin>>m[r][c];
    
        bool result = calc();
        if(result)
            cout<<"Case #"<<i+1<<": YES"<<endl;
        else
            cout<<"Case #"<<i+1<<": NO"<<endl;
    }

    return 0;
}



