#include <iostream>
#include <fstream>
using namespace std;

bool isValid(bool arr[])
{
    for(int i = 0; i < 10; i++)
    {
        if(arr[i] == false) return false;
    }
    return true;
}
int checkList(int input, bool arr[], int count)
{
    int copyInput = input*count;
    while(copyInput > 0)
    {
        arr[copyInput%10] = true;
        copyInput = copyInput/10;
    }
    if(isValid(arr)) return input*count;
    else return checkList(input, arr, count+1);
}

int checkNumber(int input)
{
    int count = 1;
    bool arr[10] = {false,false,false,false,false,false,false,false,false,false};
    return checkList(input, arr, count);
}

int main()
{
	ifstream fin;
	fin.open("A-large-in.txt");
	ofstream fout;
	fout.open("output-Large.txt");
	if(!fin.is_open()) return -1;
    int testcases;
    fin >> testcases;

    for(int i = 0; i < testcases; i++)
    {
        int input;
        fin >> input;
        if(input == 0)
            fout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
        else
            fout << "Case #" << i+1 << ": " << checkNumber(input) << endl;
    }
    return 0;
}
