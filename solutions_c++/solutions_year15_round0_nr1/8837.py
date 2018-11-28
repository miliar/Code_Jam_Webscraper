#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ofstream file;
    ifstream input;
    input.open("A-large.in");
    file.open("output.txt");
    int n, shy;
    string inp;
    input >> n;
    for(int i = 0; i < n; i++){
        input >> shy >> inp;
        int friends = 0, sum = 0;
        for(int j = 0; j <= shy; j++){
            if(sum < j){
                friends++;
                sum++;
            }
            sum += inp[j]-48;
        }
        file << "Case #" << i+1 << ": " << friends << endl;
    }
    file.close();
    return 0;
}
