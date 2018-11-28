#include <iostream>
#include <algorithm>
#include <fstream>
#include <set>

using namespace std;


int main()
{
    int N;
    ifstream myfile ("A-large.in");
    ofstream outfile;
    outfile.open ("A-large.out", ios::out | ios::trunc);
    if (myfile.is_open())
    {
        int a,b,c;
        myfile >> N;
        std::vector<int> output(N);
        for (int i = 0; i < N; i++) {
            int M;
            myfile >> M;
            output[i] = 0;
            int sum = 0;
            std::string str;
            myfile >> str;
            for (int j = 0; j < M+1; j++) {
                int c = str[j] - '0';
                if (sum < j) {
                    output[i] += j - sum;
                    sum += j - sum;
                }
                sum += c;
            }
            outfile << "Case #" << i+1 << ": " << output[i] << endl;
        }
        myfile.close();
    } else {
        return 1;
    }


    return 0;
}
