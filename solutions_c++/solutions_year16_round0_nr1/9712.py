#include <iostream>  // includes cin to read from stdin and cout to write to stdout

using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define CASE "Case #"
#define COLON ": "
#define SPACE " "
#define INSOMNIA "INSOMNIA"
#define TEN_BITS 0x3FF

int main() {
    std::size_t line_count;
    cin >> line_count;  // read t. cin knows that t is an int, so it reads it as such.
    for (int line = 1; line <= line_count; ++line) {
        std::size_t original_input;
        cin >> original_input;  // read n and then m.
        if(original_input==0){
            cout << CASE << line << COLON << INSOMNIA <<'\n';
        }else{
            std::size_t last_input = original_input;
            std::size_t i = 1;
            std::size_t bit_buffer = 0;
            while((bit_buffer & TEN_BITS) != TEN_BITS ){
                std::size_t input = original_input*(i++);
                last_input = input;
                while(input != 0){
                    std::size_t digit = input % 10;
                    input /= 10;
                    bit_buffer |= 1<<digit;
                    if((bit_buffer & TEN_BITS) == TEN_BITS ) break;
                }
            }
            cout << CASE << line << COLON << last_input <<'\n';
        }
    }
}
