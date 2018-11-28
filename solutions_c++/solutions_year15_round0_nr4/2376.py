#include <fstream>
#include <algorithm>

int main(const int argc, const char ** argv) {
    // Text file to read the input from
    std::ifstream input_file(argv[1]);
    if (input_file.is_open()) {
        // Text file to write the output to
        std::ofstream output_file("output");
        
        unsigned int case_count;
        input_file >> case_count;
        
        for (unsigned int case_num = 0; case_num < case_count; case_num++) {
            unsigned int x, r, c;
            input_file >> x >> r >> c;
            
            std::string winner("GABRIEL");
            if (((r * c) % x != 0) || ((x > 2) && (x / 2 >= std::min(r, c))) || (x >= 7)) {
                winner = "RICHARD";
            }
            
            // Write result
            output_file << "Case #" << case_num + 1 << ": " << winner << std::endl;
        }
        
        output_file.close();
        input_file.close();
    }
    
    return 0;
}
