#include <iostream>
#include <fstream>
#include <list>
#include <algorithm>
#include <functional>

int main(int argc, const char *argv[])
{
    std::fstream fin( argv[1] );

    int cases;
    fin >> cases;
    for( int i = 1; i <= cases; i++ ){
        std::cout << "Case #" << i << ": ";

        int n;
        fin >> n;
        std::list<double> naomi;
        std::list<double> ken;
        for (int b_n = 0; b_n < n; b_n++) {
            double w;
            fin >> w;
            naomi.push_back(w);
        }
        for (int b_n = 0; b_n < n; b_n++) {
            double w;
            fin >> w;
            ken.push_back(w);
        }

        naomi.sort();
        ken.sort();
        std::list<double> naomi_d = naomi;
        std::list<double> ken_d = ken;

//        std::cout << std::endl;
//        for (auto i = naomi.begin(); i != naomi.end(); i++) {
//            std::cout << *i << ", "; 
//        } std::cout << std::endl;
//         for (auto i = ken.begin(); i != ken.end(); i++) {
//            std::cout << *i << ", "; 
//        }std::cout << std::endl;
        
        int war = 0, d_war = 0;

        for (int i = 0; i < n; i++) {
            double C_n = naomi.front();
            double C_nd = naomi_d.front();
            
            auto ken_opt = std::find_if( ken.begin(), ken.end(), 
                    std::bind2nd( std::greater<double>(), C_n ) );

            if( ken_opt != ken.end() ){
                ken.erase( ken_opt );
                naomi.pop_front();
            }
            else
                war = ken.size();

            if( C_nd > ken_d.back() )
                d_war = ken_d.size();
            else{
                //check if every element is bigger
                auto n_itr = naomi_d.begin();
                auto k_itr = ken_d.begin();
                bool pass = true;
                for (int ii = 0; ii < naomi_d.size(); ii++) {
                    if( *n_itr < *k_itr )
                        pass = false;
                    n_itr++;
                    k_itr++;
                }
                if( pass )
                    d_war = ken_d.size();
                else{
                    naomi_d.pop_front();
                    ken_d.pop_back();
                }
            }

            //early termination
            if( d_war > 0 && war > 0 )
                break;



        }

        std::cout << d_war << " " << war ;
        


        std::cout << std::endl;
    }

    return 0;
}
