#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    char *line = new char[10000];
    for (int t = 0; t < T; t++) {
        int max;
        cin >> max;
        int *fds = new int[max+1];
        for (int i = 0; i <= max; i++)
            fds[i] = 0;
        cin.get();
        cin.getline(line, 10000);
        // cout << line << endl;
        for (int i = 0; i < 10000; i++)
            if (line[i] == '\0')
                break;
            else
                fds[i] = line[i] - '0';
        
        int total = 0;
        int inv = 0;
        for (int i = 0; i <= max; i++)
            if (total >= i) {
                total += fds[i];
            } else {
                inv += (i - total);
                total = i + fds[i];
            }
        cout << "Case #" << t+1 << ": " << inv << endl;
        delete[] fds;
    }
    delete[] line;

    return 0;
}
