
#include <iostream>

int main () {

    size_t num_cases = 0;

    std::cin >> num_cases;

    for (size_t i = 0; i < num_cases; ++i) {
   
        size_t n = 0;
        size_t m = 0;

        std::cin >> n;
        std::cin >> m;

        size_t cells[n][m];

        size_t min = 100;
        size_t max = 0;

        for (size_t row = 0; row < n; ++row) {
        
            for (size_t col = 0; col < m; ++col) {
            
                std::cin >> cells[row][col]; 

                if (cells[row][col] < min) min = cells[row][col];
                if (cells[row][col] > max) max = cells[row][col];

            }
        }

        bool good = true;
        for (size_t j = 0; j < n; ++j) {
            for(size_t k = 0; k < m; ++k) {

                size_t h = cells[j][k];

                bool col_good = true;
                bool row_good = true;

                for(size_t s = 0; s < n; ++s) {

                    if (cells[s][k] > h) {
                        col_good = false;
                        break;
                    }
                }

                for(size_t t = 0; t < m; ++t) {
                
                    if (cells[j][t] > h) {
                        row_good = false;
                        break;
                    }
                }
                
                good = (col_good || row_good);
                if (!good) break;
            }
            if (!good) break;
        }

        
        std::cout << "Case #" << i+1 << ": ";
        if (good) {
            std::cout << "YES";
        } else {
            std::cout << "NO";
        }

        std::cout << std::endl;
    }

    return 0;
}
