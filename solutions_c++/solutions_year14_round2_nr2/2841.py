#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

ifstream file;
void process(int num);
int main(int argc, char** argv)
{
    file.open(argv[1]);
    string line;
    getline(file, line);
    int cases = atoi(line.c_str());
    for(int i = 0; i < cases; ++i){
        process(i + 1);
    }
}

void process(int num)
{
    string line;
    getline(file, line);
    char* str = new char[line.length() + 1];
    strcpy(str, line.c_str());
    int a = atoi(strtok(str, " "));
    int b = atoi(strtok(0, " "));
    int k = atoi(strtok(0, " "));
    delete[] str;
    if(a < b){
        int temp = a;
        a = b;
        b = temp;
    }
    int count = 0;
   // cout << a << " " << b << " " << k << "\n";
    for(int i = 0; i < a; ++i){
        for(int j = 0; j < b; ++j){
//            cout << i << " " << j << "\n";
            int temp = i & j;
            if(temp <= k - 1)
                count++;
        }
    } 
    cout << "Case #" << num << ": " << count << endl;
}

/*void generateSubsets(bool* used, int start_index, int current_size, int size)
{
    if(current_size == size){
        int* nums = new int[size];
        int index = 0;
        for(int i = 0; i < ints.size(); ++i){
            if(used[i]){
                nums[index] = ints[i];
                cout << ints[i] << endl;
                index++;
            }
        }
        subsets.push_back(nums);
        return;
    }
    if(start_index == ints.size())
        return;
    used[start_index] = true;
    generateSubsets(used, start_index + 1, current_size + 1, size);
    used[start_index] = false;
    generateSubsets(used, start_index + 1, current_size, size);

}*/
