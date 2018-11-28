#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("in.txt");
    streambuf *cinbuf = cin.rdbuf(); //save old buf
    cin.rdbuf(in.rdbuf()); //redirect cin to in.txt!
    ofstream out("out.txt");
    streambuf *coutbuf = cout.rdbuf(); //save old buf
    cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
    int caseNumber;
    int k, i;
    char eachCase[10000];
    char toPutIn[10000];
    char temp;
    int charNumber, firstIndex, lastIndex;
    cin >> caseNumber;
    for (k = 0; k < caseNumber; k++){
        charNumber = 0;
        while(1){
            cin >> eachCase[charNumber];
            charNumber++;
            if (cin.peek() == '\n'){
                break;
            }
        }
        toPutIn[5000] = eachCase[0];
        firstIndex = 5000;
        lastIndex = 5000;
        //cout << eachCase[0];
        for (i = 1; i < charNumber; i++){
            temp = eachCase[i];
            //cout << "   " << temp << endl;
            if (temp >= toPutIn[firstIndex]){
                firstIndex--;
                toPutIn[firstIndex] = temp;
            }
            else{
                lastIndex++;
                toPutIn[lastIndex] = temp;
            }
        }
        //cout << firstIndex << " " << lastIndex << endl;
        cout << "Case #" << k + 1 << ": ";
        for (i = firstIndex; i <= lastIndex; i++){
            cout << toPutIn[i];
        }
        cout << endl;
    }
    return 0;
}
