#include<iostream>

using namespace std;

int main() {

    int t,ctr,len;
    char last,present;
    cin >> t;

    ctr = cin.get();

    for (int i = 1;i<=t;i++) {

        ctr = 0;
        present = cin.get();
        last = present;
        while (present != '\n' ) {
            if (last != present)
                ctr++;
            last = present;
            present = cin.get();
        }
        cout << "Case #"<<i<<": ";
        if (last == '-')    // Happiness not found
            cout <<ctr+1<<'\n';
        else
            cout << ctr << '\n';
    }
    return 0;
}
