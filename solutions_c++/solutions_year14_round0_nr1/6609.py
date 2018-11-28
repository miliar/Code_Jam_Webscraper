#include <fstream>
#include <iostream>
#include <set>
#include <sstream>

using namespace std;

int main()
{
    ifstream infile("A-small-attempt0.in");
    //ifstream infile("ProblemAInput.txt");
    ofstream outfile("ProblemAOutputSmall.txt");

    int T;
    infile >> T;

    for (int i = 0; i < T; i++) {
        int firstAns;
        int secondAns;
        int num;
        set<int> numbers;
        int count = 0;
        int answer = 0;

        infile >> firstAns;
        for (int j = 1; j <= 4; j++) {
            for (int k = 0; k < 4; k++) {
                infile >> num;
                if (j == firstAns)
                    numbers.insert(num);
            }
        }

        infile >> secondAns;
        for (int j = 1; j <= 4; j++) {
            for (int k = 0; k < 4; k++) {
                infile >> num;
                if (j == secondAns && numbers.count(num) > 0) {
                    count++;
                    answer = num;
                }
            }
        }

        if (count == 0)
            outfile << "Case #" << (i+1) << ": " << "Volunteer cheated!" << endl;
        else if (count == 1)
            outfile << "Case #" << (i+1) << ": " << answer << endl;
        else
            outfile << "Case #" << (i+1) << ": " << "Bad magician!" << endl;
    }
    return 0;
}
