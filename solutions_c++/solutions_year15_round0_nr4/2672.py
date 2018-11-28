#include <iostream>
#include <fstream>

int main(void) {
    std::ifstream in ("d2.in");
    std::ofstream out ("out.txt");
    int tests;
    in >> tests;
    for (int i=0; i < tests; i++) {
        int x,r,c;
        in >> x >> r >> c;
        //std::cout << num << std::endl << ov << std::endl;
        if (r*c % x != 0 ) {
            out << "Case #" << i+1 << ": " << "RICHARD" << std::endl;
        }
        else if (x==3 && (r==1 || c==1))
            out << "Case #" << i+1 << ": " << "RICHARD" << std::endl;
        else if (x==4 && (r<3 || c<3 || (r%x!=0 && c%x!=0))) {
            out << "Case #" << i+1 << ": " << "RICHARD" << std::endl;
        }
        else {
            out << "Case #" << i+1 << ": " << "GABRIEL" << std::endl;
        }
    }
    in.close();
    out.close();
    return 0;
}
