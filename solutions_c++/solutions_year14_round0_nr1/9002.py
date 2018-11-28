#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int T;

int first[4][4];
int second[4][4];
int answer1, answer2;
void getInput();

int i,j,k,l;
int fr[4], sr[4];
void getInputRow();

void findDuplicates(int test = 1);


ifstream input("A-small-attempt0.in");
ofstream out("out.txt");

int main()
{
    input >> T;



    for (int k = 0; k < T ; k++)
    {
//        getInput();
        getInputRow();
        findDuplicates(k+1);

    }

//    cout << T << answer1 << endl;
//    cout << fr[0] << fr[1] << fr[2] << fr[3] << endl;
//    cout << sr[0] << sr[1] << sr[2] << sr[3] << endl;

    return 0;
}

//void getInput()
//{
//    input >> answer1;

//    for (int i = 0; i < 4; i++)
//    {
//        for (int j = 0; j < 4; j++)
//        {
//            input >> first[i][j];
//        }
//    }

//    input >> answer2;

//    for (int i = 0; i < 4; i++)
//    {
//        for (int j = 0; j < 4; j++)
//        {
//            input >> second[i][j];
//        }
//    }
//}

void getInputRow()
{
    input >> answer1;
    for (int g=0; g < 4; g++) {
        if ((answer1-1) == g)
            input >> fr[0] >> fr[1] >> fr[2] >> fr[3];
        else
            input >> i >> j >> k >> l;
    }

    input >> answer2;
    for (int g=0; g < 4; g++) {
        if ((answer2-1) == g)
            input >> sr[0] >> sr[1] >> sr[2] >> sr[3];
        else
            input >> i >> j >> k >> l;
    }
}

void findDuplicates(int test)
{
    vector<int> both(8);

    for (int h = 0; h < 4; h++)
        both[h] = fr[h];

    for (int h = 4, m = 0; h < 8; h++, m++)
        both[h] = sr[m];

    sort(both.begin(), both.end());

    int count = 0, output = 0;

    for (int h = 0; h < 7; h++) {
        if (both[h] == both[h+1]) {
            count++;
            output = both[h];
        }
    }

    if (count == 0) {
        cout << "Case #" << test << ": " << "Volunteer cheated!" << endl;
        out << "Case #" << test << ": " << "Volunteer cheated!" << endl;
    }
    else if (count == 1) {
        cout << "Case #" << test << ": " << output << endl;
        out << "Case #" << test << ": " << output << endl;
    }
    else {
        cout << "Case #" << test << ": " << "Bad magician!" << endl;
        out << "Case #" << test << ": " << "Bad magician!" << endl;
    }

//    cout << count << endl;
}
