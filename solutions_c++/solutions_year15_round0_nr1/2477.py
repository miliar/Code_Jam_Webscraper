#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream f("C:/Users/Rebecca/Downloads/A-large.in");
    ofstream out;
    out.open("C:/Users/Rebecca/Downloads/result2.txt");

    int numtests;
    f >> numtests;
    for (int i = 0; i < numtests; i++) {
        int n;
        string str;
        f >> n;
        f >> str;
        int arr[n + 1];
        for (int i = 0; i <= n; i++) {
            arr[i] = str[i] - '0';
        }
        int required = 0;
        int curr = arr[0];
        for (int i = 1; i <= n; i++) {
            if (curr < i) {
                required += i - curr;
                curr = i;
            }
            curr += arr[i];
        }
        out << "Case #" << i+1 << ": " << required << endl;
    }
    out.close();
    return 0;
}

