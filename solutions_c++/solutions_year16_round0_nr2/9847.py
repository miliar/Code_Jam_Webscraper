#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    int T;
    cin >> T;
    ofstream fout ("output.txt");
    vector<string> store (T);
    for (int i = 0; i < T; i++) cin >> store[i];

    for (int i = 0; i < T; i++)
    {
        string pancake = store[i];
        int counter = 0;
        for (int j = pancake.size() -1; j >= 0; j--) {
            if (pancake[j] == '-') {
                int k = 0;
                while (pancake[k] == '+') pancake[k++] = '-';
                if (k != 0) counter++;
                string news;
                for (int i = 0; i < pancake.size(); i++) {
                    if (i <= j) news += (pancake[j-i] == '-' ? '+' : '-');
                    else news += pancake[i];
                }

                pancake = news;
                counter++;
            }
        }

        fout << "Case #" << i+1 << ": " << counter << endl;
    }

    return 0;
}
