#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

unsigned int count_digit(const unsigned long long i) {
    unsigned long long temp = i;
    unsigned int digits = 0;
    while (temp != 0) {
        digits++;
        temp /= 10;
    }
    return digits;
}

bool is_edge(const unsigned long long i, const unsigned int digits) {
    unsigned long long temp = i;
    unsigned int half_way = digits / 2;
    while (half_way != 0) {
        if (temp % 10 != 9) {
            return false;
        }
        half_way--;
        temp /= 10;
    }
    return true;
}

int main(const int argc, const char ** argv) {
    if (argc < 2) {
        cout << "No input file specified" << endl;
        return -1;
    } else if (argc > 3) {
        cout << "Too many arguments" << endl;
        return -1;
    }
    
    ifstream input_file(argv[1]);
    if (input_file.is_open()) {
        ofstream output_file;
        if (argc == 3) {
            output_file.open(argv[2]);
        } else {
            output_file.open("out");
        }
        
        unsigned int case_count;
        input_file >> case_count;
        
        for (unsigned int case_num = 0; case_num < case_count; case_num++) {
            unsigned long long n;
            input_file >> n;
            unsigned int n_digits = count_digit(n);
            
            bool zero_zero;
            if (n % 10 == 0) {
                zero_zero = true;
                n--;
            } else {
                zero_zero = false;
            }
            
            unsigned long long count = 1, p = 1;
            while (p < n) {
                unsigned int p_digits = count_digit(p);
                if (n_digits == p_digits) {
                    unsigned long long cp = p, cn = n;
                    vector<unsigned int> sp;
                    do {
                        sp.push_back(cp % 10);
                        cp /= 10;
                    } while (cp != 0);
                    vector<unsigned int> sn;
                    do {
                        sn.push_back(cn % 10);
                        cn /= 10;
                    } while (cn != 0);
                    bool match = true;
                    for (unsigned int i = 0; i < n_digits / 2; i++) {
                        if (sp[i] != sn[n_digits - 1 - i]) {
                            match = false;
                            break;
                        }
                    }
                    if (match) {
                        unsigned long long next_reverse = 0;
                        for (unsigned int i : sp) {
                            next_reverse *= 10;
                            next_reverse += i;
                        }
                        if (next_reverse <= n && next_reverse > p + 1 && next_reverse != p) {
                            p = next_reverse;
                        } else {
                            p++;
                        }
                    } else {
                        p++;
                    }
                } else if (is_edge(p, p_digits)) {
                    unsigned long long cp = p;
                    vector<unsigned int> sp;
                    do {
                        sp.push_back(cp % 10);
                        cp /= 10;
                    } while (cp != 0);
                    
                    unsigned long long next_reverse = 0;
                    for (unsigned int i : sp) {
                        next_reverse *= 10;
                        next_reverse += i;
                    }
                    
                    if (next_reverse <= n && next_reverse > p + 1) {
                        p = next_reverse;
                    } else {
                        p++;
                    }
                } else {
                    p++;
                }
                count++;
            }
            
            if (zero_zero) {
                count++;
            }
            cout << "Case #" << case_num + 1 << " CLEAR" << endl;
            output_file << "Case #" << case_num + 1 << ": " << count << endl;
        }
        
        output_file.close();
        input_file.close();
    } else {
        cout << "Cannot find input file: " << argv[1] << endl;
        return -1;
    }
    
    return 0;
}
