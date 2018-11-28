#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream fin("example.txt");
    if(fin.is_open()) {
        int N;
        int T;
        ofstream fout("output.txt");
        fin >> T;
        int c = 0;
        int last;
        int num, i, ans;
        bool zero, one, two, three, four, five,
             six, seven, eight, nine;
        while(fin >> N) {
            c++;
            if(N == 0) {
                fout << "Case #" << c << ": INSOMNIA" << endl;
            } else {
                zero = false, one = false, two = false, three = false,
                four = false, five = false, six = false, seven = false,
                eight = false, nine = false; 
                i = 0;

                while(!zero || !one || !two || !three || !four || !five ||
                      !six || !seven || !eight || !nine) {
                    ++i;
                    num = i*N;
                    ans = num;
                    while(num > 0) {
                        int digit;
                        digit = num % 10;
                        switch(digit) {
                            case 0:
                                zero = true;
                                break;
                            case 1:
                                one = true;
                                break;
                            case 2:
                                two = true;
                                break;
                            case 3:
                                three = true;
                                break;
                            case 4:
                                four = true;
                                break;
                            case 5:
                                five = true;
                                break;
                            case 6:
                                six = true;
                                break;
                            case 7:
                                seven = true;
                                break;
                            case 8:
                                eight = true;
                                break;
                            case 9:
                                nine = true;
                                break;
                        }
                        num = num / 10;
                    }
                }

                fout << "Case #" << c << ": " << ans << endl;
            }
        }

        fin.close();
        fout.close();
    } else
        cout << "Could not open file." << endl;

}
