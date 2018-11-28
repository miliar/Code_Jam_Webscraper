#include <iostream>

using namespace std;

bool found_all(bool seen[]){

    for (int i = 0; i < 10; i++) {
        if (!seen[i]) {
            return false;
        }
    }
    return true;
}

void mark_digits(unsigned long long num, bool seen[]) {
    unsigned long long temp = num;
    while(temp) {
        seen[temp%10] = true;
        temp = temp/10;
    }
}

int main(int argc, char const* argv[])
{
    int T;
    unsigned long long N;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N;
        if (N==0) {
            cout << "Case #" << t << ": INSOMNIA" << endl;
            continue;
        }
        bool seen[10] = {};
        int i = 0;
        do {
            i++;
            mark_digits(i*N,seen);
        }while (!found_all(seen));
        cout << "Case #" << t << ": " << i*N << endl;
    }
    return 0;
}
