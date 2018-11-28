#include <iostream>
#include <fstream>

struct InputData {
    unsigned int number;
};

bool *getNumbersDigits(unsigned int number) {
    bool *digits = new bool[10];
    for(unsigned int i = 0;i < 10; i++) {
        digits[i] = false;
    }
    while(number > 0) {
        unsigned int digit = number-((number/10)*10);
        digits[digit] = true;
        number /= 10;
    }
    return digits;
}

void processCase(InputData input_data, std::ofstream &output) {
    if(input_data.number == 0) {
        output << "INSOMNIA" << "\n";
        return;
    }
    bool digits[10];
    for(unsigned int i = 0;i < 10; i++) {
        digits[i] = false;
    }

    bool all_digits_found = false;
    int N = 1;
    do {
        bool *temp_digits = getNumbersDigits(input_data.number*N);

        for(unsigned int i = 0; i < 10;i++) {
            digits[i] = digits[i] || temp_digits[i];
        }
        delete[] temp_digits;


        all_digits_found = true;
        for(unsigned int i = 0; i < 10;i++) {
            if(digits[i] == false) {
                all_digits_found = false;
                break;
            }
        }
        N++;
    } while(!all_digits_found);

    output << input_data.number*(N-1) << "\n";
}

int main() {
    char file_name[50] = "./A-large.in";
    // std::cin >> file_name;
    std::ifstream input(file_name);
    std::ofstream output("output");
    
    
    
    unsigned int case_count;
    input >> case_count;
    for(unsigned int i = 0; i < case_count; i++) {
        InputData data;
        input >> data.number;
        output << "case #" << i+1 <<": ";
        processCase(data, output);
    }
    
    input.close();
    output.close();
    return 0;
}