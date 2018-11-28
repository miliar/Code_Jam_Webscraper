#include <fstream>
#include <vector>

int main(const int argc, const char ** argv) {
    // Text file to read the input from
    std::ifstream input_file(argv[1]);
    if (input_file.is_open()) {
        // Text file to write the output to
        std::ofstream output_file("output");
        
        unsigned int case_count;
        input_file >> case_count;
        
        for (unsigned int case_num = 0; case_num < case_count; case_num++) {
            unsigned int shyness_max;
            input_file >> shyness_max;
            
            std::string audience;
            input_file >> audience;
            
            unsigned int friends = 0, audience_count = 0;
            for (unsigned int i = 0; i < shyness_max + 1; i++) {
                unsigned int audience_num = (audience[i] - '0'); // Convert char to int
                if ((audience_num > 0) && (audience_count < i)) {
                    // Not enough people, invite more friends
                    friends += (i - audience_count);
                    audience_count += friends;
                }
                audience_count += audience_num;
            }
            
            // Write result
            output_file << "Case #" << case_num + 1 << ": " << friends << std::endl;
        }
        
        output_file.close();
        input_file.close();
    }
    
    return 0;
}
