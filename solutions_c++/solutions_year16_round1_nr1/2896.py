#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    int count;
    in >> count;
    for(int i = 0; i < count; i++) {
        string sValue;
        string winningString;
        in >> sValue;
        for(int j = 0; j < sValue.length(); j++) {
            if(winningString.length() == 0) {
                winningString = sValue[j];
            } else {
                if(sValue[j] < winningString[0]) {
                    winningString+= sValue[j];
                } else {
                    winningString = sValue[j] + winningString;
                }
            }
        }
        out << "Case #" << i+1 << ": " << winningString << endl;
    }

    in.close();
    out.close();
}
