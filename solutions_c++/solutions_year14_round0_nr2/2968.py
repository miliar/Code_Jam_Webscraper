#include <iostream>
#include <fstream>
#include <iomanip>

int main(int argc, const char *argv[])
{
    std::ifstream fin( argv[1] );

    int cases;
    fin >> cases;
    
    for (int i = 0; i < cases; i++) {
        std::cout << "Case #" << i + 1 << ": ";
        double c, f, x;
        double cr = 0, ttb = 9999999999999999.9,  ttw = 9999999999999999999.9;
        int nf;
        double ct, cc;
        fin >> c >> f >> x;
        cr = 2.0;
        cc = 0.0;
        ct = 0.0;
        ttw = x / cr;
        ttb = c / cr;
        while( ttw > (ct + ttb) ){
            ct += ttb;
            cr += f;
            double new_ttw = ct + x / cr;
            if( ttw < new_ttw )
                break;
            else
                ttw = new_ttw;
            ttb = c / cr;
        }
        std::cout << std::setprecision(16) << ttw << std::endl;
            
            
    }
    return 0;
}
