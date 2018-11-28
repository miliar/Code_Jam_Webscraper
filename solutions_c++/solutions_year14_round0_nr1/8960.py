#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    fstream input("input.txt"), out("output.txt");
    int T, answer_1, answer_2, N = 4;
    int *temp = new int[N];
    int **a = new int*[N];
    int count = 0;
    int result = 0;
    int C;
    string st;
    for(int i = 0; i < N; i++)
        a[i] = new int[N];
    input >> T;
int Z=0;
    while (Z<T) {
    input >> answer_1;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            input >> a[i][j];
            }
        }
    for(int i = 0; i < N; i++)
        temp[i]=a[answer_1-1][i];

    input >> answer_2;


    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            input >> a[i][j];
            }
        }

    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++) {
            if(temp[i]==a[answer_2-1][j]) {
                count++;
                result=a[answer_2-1][j];

                }
            if(count > 1)
                st="Bad magician!";
            if(count == 0)
                st="Volunteer cheated!";
            }
    if(count == 1)
        out << "Case #" << Z+1 << ": " << result << endl;
    else
        out << "Case #" << Z+1 << ": " << st << endl;
    count = 0;




Z++;
    }


    return 0;
}
