#include<iostream>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
    ifstream ifile ("A-large.in");
    ofstream ofile ("output.out");
    string s;
    int t, flag1 = 1, flag2 = 1, flag11 = 0, flag22 = 0, flag = 0, flag3 = 1, flag33 = 0, flag4 = 1, flag44 = 0, fflag = 0;
    char val1, val2, val3, val4;
    char arr[4][4];
    ifile >> t;
    getline(ifile, s);
    for(int k = 0 ; k < t ; k++)
    {
        flag = 0, flag3 = 1, flag33 = 0, flag4 = 1, flag44 = 0, fflag = 0;
        for(int i = 0 ; i < 4 ; i++)
        {
            flag1 = 1, flag11 = 0;
            for(int j = 0 ; j < 4 ; j++)
            {
                ifile >> arr[i][j];
                if(arr[i][j] == '.')
                {
                     flag1 = 0;
                     fflag = 1;
                }
                if(arr[i][j] != 'T' && flag11 == 0)
                {
                     val1 = arr[i][j];
                     flag11 = 1;
                }
                else if(arr[i][j] != 'T' && flag11 == 1)
                {
                     if(arr[i][j] != val1)
                          flag1 = 0;
                }
            }
            getline(ifile, s);
            if(flag1 == 1 && flag == 0)
            {
                 ofile << "Case #" << k+1 << ": " << val1 << " won";
                 flag = 1;
            }           
            if(arr[i][i] == '.')
                 flag3 = 0;
            if(arr[i][i] != 'T' && flag33 == 0)
            {
                 val3 = arr[i][i];
                 flag33 = 1;
            }
            else if(arr[i][i] != 'T' && flag33 == 1)
            {
                 if(arr[i][i] != val3)
                      flag3 = 0;
            }
            
            if(arr[i][4-(i+1)] == '.')
                 flag4 = 0;
            if(arr[i][4-(i+1)] != 'T' && flag44 == 0)
            {
                 val4 = arr[i][4-(i+1)];
                 flag44 = 1;
            }
            else if(arr[i][4-(i+1)] != 'T' && flag44 == 1)
            {
                 if(arr[i][4-(i+1)] != val4)
                      flag4 = 0;
            }       
        }
        for(int i = 0 ; i < 4 ; i++)
        {
            flag2 = 1, flag22 = 0;
            for(int j = 0 ; j < 4 ; j++)
            {
                if(arr[j][i] == '.')
                     flag2 = 0;
                if(arr[j][i] != 'T' && flag22 == 0)
                {
                     val2 = arr[j][i];
                     flag22 = 1;
                }
                else if(arr[j][i] != 'T' && flag22 == 1)
                {
                     if(arr[j][i] != val2)
                          flag2 = 0;
                }  
            }
            if(flag2 == 1 && flag == 0)
            {
                 ofile << "Case #" << k+1 << ": " << val2 << " won";
                 flag = 1;
            }
        }
        getline(ifile, s);
        if(flag3 == 1 && flag == 0)
        {
             ofile << "Case #" << k+1 << ": " << val3 << " won";
             flag = 1;
        }
        else if(flag4 == 1 && flag == 0)
        {
             ofile << "Case #" << k+1 << ": " << val4 << " won";
             flag = 1;
        }
        if(flag == 0)
        {
            if(fflag == 1)
            {
                 ofile << "Case #" << k+1 << ": Game has not completed";
            }
            else
            {
                ofile << "Case #" << k+1 << ": Draw";
            }
        }
        if (k != t-1)
           ofile << endl;
    }
    ifile.close();
    ofile.close();
    return 0;
}
