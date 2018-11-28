#include <iostream>
#include <fstream>
using namespace std;
void getNumbers(int);
bool allNumbers[10];
int main()
{
    ifstream in("in.txt");
    streambuf *cinbuf = cin.rdbuf(); //save old buf
    cin.rdbuf(in.rdbuf()); //redirect cin to in.txt!
    ofstream out("out.txt");
    streambuf *coutbuf = cout.rdbuf(); //save old buf
    cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
    int eachCase;
    int caseNumber;
    int k, i;
    int counter;
    int temp;
    bool isOver;
    cin >> caseNumber;
    for (k = 0; k < caseNumber; k++){
        for (i = 0; i < 10; i++){
            allNumbers[i] = false;
        }
        cin >> eachCase;
        if (eachCase == 0){
            cout << "Case #" << k + 1 << ": INSOMNIA" << endl;
            continue;
        }
        temp = eachCase;
        while(1){
            getNumbers(temp);
            isOver = true;
            for(i = 0; i < 10; i++){
                if (!allNumbers[i]){
                    isOver = false;
                    break;
                }
            }
            if (isOver){
                break;
            }
            temp += eachCase;
        }
        cout << "Case #" << k + 1 << ": " << temp << endl;
    }
    return 0;
}
void getNumbers(int x)
{
    if(x >= 10)
       getNumbers(x / 10);

    int digit = x % 10;
    allNumbers[digit] = true;
}
