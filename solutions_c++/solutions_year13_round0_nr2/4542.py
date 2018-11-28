#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;

size_t rows;
size_t cols;

void Deep(size_t row, vector< vector<bool> >& lawn) {
    for (size_t i = 0; i < cols; ++i) {
        lawn[row][i] = false;  
    }
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    size_t n;
    cin >> n;
    //cout << "!";
    for (size_t i = 0; i < n; ++i) {
        cin >> rows;
        cin >> cols;
        //cout << "!";
        vector< vector<int> > pattern(rows, vector<int>(cols));
        for (size_t row = 0; row < rows; ++row) {
            for (size_t col = 0; col < cols; ++col) {
                int length;
                cin >> length;
                pattern[row][col] = length;    
            }   
        } 
        vector< vector<int> > lawn(rows, vector<int>(cols, 100));
  
        for (size_t row = 0; row < rows; ++row) {
            int max = 0;
            for (size_t col = 0; col < cols; ++col) {
                if (pattern[row][col] > max) {
                    max = pattern[row][col];
                }    
            }
            
            for (size_t col = 0; col < cols; ++col) {
                if (lawn[row][col] > max) {
                    lawn[row][col] = max;
                }
            }
            
        }
         
        for (size_t col = 0; col < cols; ++col) {
            int max = 0;
            for (size_t row = 0; row < rows; ++row) {
                if (pattern[row][col] > max) {
                    max = pattern[row][col];
                }    
            }
            
            for (size_t row = 0; row < rows; ++row) {
                if (lawn[row][col] > max) {
                    lawn[row][col] = max;
                }
            }
            
        }       
        bool result = true;
        for (size_t row = 0; row < rows; ++row) {
            for (size_t col = 0; col < cols; ++col) {
                if (lawn[row][col] != pattern[row][col]) {
                    result = false;   
                }              
            }   
        } 
        if (result) {
            cout << "Case #" << i + 1 <<": YES" << std::endl; 
        } else {
            cout << "Case #" << i + 1 <<": NO" << std::endl; 
        }
        
    }
    return 0;      
}
