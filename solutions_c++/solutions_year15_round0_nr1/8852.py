#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    int T;
    ifstream fin("C:\\Users\\Caoyu\\Downloads\\A-large.in");
    ofstream fout("C:\\Users\\Caoyu\\Downloads\\output.txt");
    fin>>T;
    int caseN = 1;
    while (T > 0){
        int Smax;
        fin>>Smax;
        string str;
        fin>>str;
        int count = 0;
        int sum = str[0] - '0';
        for (int i = 1; i < str.size(); i++) {
            if (sum >= i){
                sum += (str[i]-'0');
            } else {
                count+= (i-sum);
                sum = i + str[i] - '0';
            }
        }
        fout<<"Case #"<<caseN<<": "<<count<<endl;
        caseN++;
        T--;
    }

    fin.close();
    fout.close();
    return 0;
}