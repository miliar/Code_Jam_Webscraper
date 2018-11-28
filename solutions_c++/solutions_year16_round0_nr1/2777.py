#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;
bool digits[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int count = 0;
int main() {
    int t;
    fstream file("A-large.in", ios::in);
    fstream out("sheep.out", ios::out);
    file >> t;
    for(int i = 1; i <= t; i++) {
        int n;
        file >> n;
        int c = 0, te = 0, temp;
        if(n == 0) {
            out << "Case #" << i << ": INSOMNIA" << endl;
        }
        else {
            while(c != 10) {
                te += n;
                temp = te;
                while(temp != 0) {
                    c += digits[temp % 10] == 0 ? 1 : 0;
                    digits[temp % 10] = 1;
                    temp /= 10;
                }
            }
            out << "Case #" << i << ": " << te << endl;
        }

        for(int i = 0; i < 10; i++)
            digits[i] = 0;
	}
}
