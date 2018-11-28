#include <iostream>
#include <fstream>
using namespace std;

void magician(const char* filename)
{
        int max_line = 65536;

        ifstream input(filename);
        int num_tests;
        input >> num_tests;
        input.ignore(max_line, '\n'); 

        for (int case_num = 1; case_num <= num_tests; case_num++) {
                cout << "Case #" << case_num << ": ";
                
                int output[17] = {0};
                int first_ans;
                
                // Read first row num volunteer suggested.
                input >> first_ans;
                first_ans -= 1;                 // -1 to make it C row index.
                input.ignore(max_line, '\n');     // Move to next line.
                        
                // Skip all lines before the one pointed by volunteer.
                int i = 0;
                while (i < first_ans) {
                        input.ignore(max_line, '\n');i++;
                }
                
                // Read the row pointed by volunteer and mark the values.
                int val;
                for (int j = 0; j < 4; j++) {
                        input >> val;
                        output[val]++;
                }
           
                // skip rest of the lines from first arrangement.
                while (i < 4) {
                        input.ignore(max_line, '\n');i++;
                }
        
                // Read second row num volunteer suggested.
                int second_ans;
                input >> second_ans;           
                second_ans -= 1;               // -1 to make it C row index.
                input.ignore(max_line, '\n');    // Move to next line.
        
                // Skip all lines before the one pointed by volunteer.
                i = 0;
                while (i < second_ans) {
                        input.ignore(max_line, '\n');i++;
                }
        
                // Read the row pointed by volunteer and mark the values.
                for (int j = 0; j < 4; j++) {
                        input >> val;
                        output[val]++;
                }
                
                // skip rest of the lines from first arrangement.
                while (i < 4) {
                        input.ignore(max_line, '\n');i++;
                }
                
                int final;
                int matches = 0;
                for (int i = 1; i < 17; i++) {
                        if (output[i] == 2) {
                                final = i;
                                matches++;
                        }
                }
                
                if (matches == 1) {
                        cout << final << endl;
                }
                else if (matches > 1) {
                        cout << "Bad magician!" << endl;
                }
                else {
                        cout << "Volunteer cheated!" << endl;
                }
        }
}

int main(int argc, char* argv[]) {
        if ( argc != 2 ) {
                cout<<"usage: "<< argv[0] <<" <filename>\n";
        }

        magician(argv[1]);
        return 0;
}
