#include <fstream>
#include <string>
#include <unordered_map>

std::unordered_map<char, std::unordered_map<char, char>> table;

char multiply(const char left, const char right) {
    if (left < 0) {
        return table[left * -1][right] * -1;
    } else {
        return table[left][right];
    }
}

std::string::iterator find_char(const std::string::iterator& begin, const std::string::iterator& end, const char c) {
    char previous;
    for (auto it = begin; it < end; it++) {
        if (it > begin) {
            *it = multiply(previous, *it);
        }
        if (*it == c) {
            return it;
        }
        previous = *it;
    }
    return end;
}

int main(const int argc, const char ** argv) {
    std::unordered_map<char, char> table1{{1, 1}, {'i', 'i'}, {'j', 'j'}, {'k', 'k'}};
    std::unordered_map<char, char> tablei{{1, 'i'}, {'i', -1}, {'j', 'k'}, {'k', 'j' * -1}};
    std::unordered_map<char, char> tablej{{1, 'j'}, {'i', 'k' * -1}, {'j', -1}, {'k', 'i'}};
    std::unordered_map<char, char> tablek{{1, 'k'}, {'i', 'j'}, {'j', 'i' * -1}, {'k', -1}};
    table.emplace(1, table1);
    table.emplace('i', tablei);
    table.emplace('j', tablej);
    table.emplace('k', tablek);
    
    // Text file to read the input from
    std::ifstream input_file(argv[1]);
    if (input_file.is_open()) {
        // Text file to write the output to
        std::ofstream output_file("output");
        
        unsigned int case_count;
        input_file >> case_count;
        
        for (unsigned int case_num = 0; case_num < case_count; case_num++) {
            unsigned int l, x;
            input_file >> l >> x;
            
            std::string input;
            input_file >> input;
            
            std::string x_input;
            for (unsigned int i = 0; i < x; i++) {
                x_input += input;
            }
            
            std::string::iterator begin_i = x_input.begin();
            std::string::iterator found_i = x_input.end();
            std::string::iterator found_j = x_input.end();
            std::string::iterator found_k = x_input.end();
            do {
                found_i = find_char(begin_i, x_input.end(), 'i');
                if (found_i > x_input.end() - 3) {
                    break;
                }
                std::string::iterator begin_j = found_i + 1;
                
                do {
                    found_j = find_char(begin_j, x_input.end(), 'j');
                    if (found_j > x_input.end() - 2) {
                        break;
                    }
                    std::string::iterator begin_k = found_j + 1;
                    
                    do {
                        found_k = find_char(begin_k, x_input.end(), 'k');
                        if (found_k >= x_input.end() - 1) {
                            break;
                        } else if (found_k < x_input.end() - 1) {
                            begin_k = found_k + 1;
                            *begin_k = multiply(*found_k, *begin_k);
                        }
                    
                    } while(found_k != x_input.end());
                    
                    if (found_k == x_input.end() - 1){
                        break;
                    } else if (found_j < x_input.end() - 1) {
                        begin_j = found_j + 1;
                        *begin_j = multiply(*found_j, *begin_j);
                    }
                
                } while(found_j != x_input.end());
                
                if (found_k == x_input.end() - 1) {
                    break;
                } else if (found_i < x_input.end() - 1) {
                    begin_i = found_i + 1;
                    *begin_i = multiply(*found_i, *begin_i);
                }
                
            } while(found_i != x_input.end());
            
            if ((found_i != x_input.end()) && (found_j != x_input.end()) && (found_k != x_input.end())) {
                output_file << "Case #" << case_num + 1 << ": YES" << std::endl;
            } else {
                output_file << "Case #" << case_num + 1 << ": NO" << std::endl;
            }
        }
        
        output_file.close();
        input_file.close();
    }
    
    return 0;
}
