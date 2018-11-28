#include <iostream>
#include <fstream>

int main(void) {
    std::ifstream in ("input1.in");
    std::ofstream out ("out.txt");
    int tests;
    in >> tests;
    for (int i=0; i < tests; i++) {
        int num;
        std::string ov;
        in >> num >> ov;
        int people=0;
        int friends = 0;
        //std::cout << num << std::endl << ov << std::endl;
        for(int i=0; i < num+1; i++ ) {
            if (i > people) {
                friends += i-people;
                people = i;
            }
            people += ov[i] - '0';
        }
        //std::cout << friends << std::endl;
        out << "Case #" << i+1 << ": " << friends << std::endl;
    }
    in.close();
    out.close();
    return 0;
}
