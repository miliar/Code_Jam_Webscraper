#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

bool checkArray(bool arr[])
{
    for(int i = 0; i <= 9; i++)
    {
        if(!arr[i])
        {
            return false;
        }
    }
    return true;
}
void changeArray(bool arr[], string stringVal)
{
    for(int i = 0; i < stringVal.size(); i++)
    {
            char c = stringVal[i];
            int res = c-'0';
            if(res >= 0 && res <= 9)
            {
                if(!arr[res])
                {
                    arr[res] = true;
                }
            }
    }
}
void flushArray(bool arr[])
{
    for(int i = 0; i <= 9; i++)
    {
        arr[i] = false;
    }
}
int main()
{
    int T;
    int N;
    int val, prevVal;
    bool arr[] = {false,false,false,false,false,false,false,false,false,false};
    ifstream infile;
    ofstream ofile;
    infile.open("google_input.txt");
    ofile.open("google_output.txt");

    infile >> T;
    //cin >> T;

    for(int i = 0; i < T; i++)
    {
        infile >> N;
        //cin >> N;
        val = N;
        prevVal = N;

        ofile << "Case #" << i+1 << ": ";
        //cout << "Case #" << i+1 << ": ";
        if(N == 0)
        {
            ofile << "INSOMNIA" << endl;
            //cout << "INSOMNIA" << endl;
        }
        else
        {
            while(!checkArray(arr))
            {
                ostringstream ss;
                ss << val;
                string stringVal = ss.str();
                changeArray(arr, stringVal);
                prevVal = val;
                val = val+N;
            }
            ofile << prevVal << endl;
            //cout << prevVal << endl;
            flushArray(arr);
        }
    }
    infile.close();
    ofile.close();
    return 0;
}
