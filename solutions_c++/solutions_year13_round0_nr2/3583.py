#include <iostream>
#include <fstream>
#include <vector>
#include <stdint.h>

using namespace std;

// quick debug source - stack overflow
const char *byte_to_binary(int x)
{
    static char b[9];
    b[0] = '\0';

    int z;
    for (z = 128; z > 0; z >>= 1)
    {
        strcat(b, ((x & z) == z) ? "1" : "0");
    }

    return b;
}

void
    debug (
            uint32_t R, uint32_t C,
            vector<vector<uint32_t>> height,
            vector<vector<uint32_t>> reach)
{
    for (size_t row = 0; row < R; ++row) {
        for (size_t col = 0; col < C; ++col) {
            cout << height[row][col];
        }
        cout << endl;
    }
    cout << endl;

    for (size_t row = 0; row < R; ++row) {
        for (size_t col = 0; col < C; ++col) {
            cout << (byte_to_binary(reach[row][col])+6) << " ";
        }
        cout << endl;
    }        
    cout << endl;
    cout << endl;
}

int 
	main () 
{
	ifstream in = ifstream ("in.txt");
	ofstream out = ofstream ("out.txt");
		
	size_t T;	
	in >> T;

	for (size_t i = 1; i <= T; ++i) {
        size_t R; // rows
        size_t C; // cols

        in >> R;
        in >> C;

        const uint32_t NOT_HORIZONTAL   = 0x1; // 01
        const uint32_t NOT_VERTICAL     = 0x2; // 10    
        const uint32_t NONE             = 0;
        const uint32_t ALL              = 0x3; // 11

        vector<vector<uint32_t>> height(R, vector<uint32_t>(C, 0));
        vector<vector<uint32_t>> reach(R, vector<uint32_t>(C, ALL));

        // pro kazde policko se divam
        // jestli z dane strany lze jit az tak nizko, aniz by se pokazily predchozi

        for (size_t row = 0; row < R; ++row) {
            for (size_t col = 0; col < C; ++col) {
                uint32_t h;
                in >> h;
                height[row][col] = h;
            }
        }
        
        //debug(R,C,height,reach);

        {
            // left to right
            for (int row = 0; row < R; ++row) {
                uint32_t value = height[row][0];
                for (int col = 0; col < C; ++col) {
                    uint32_t h =  height[row][col];
                    if (h < value) {
                        reach[row][col] &= NOT_HORIZONTAL; 
                    }
                    value = std::max(value, h);
                }
            }
        }        
               
        //debug(R,C,height,reach);

        {
            // right to left
            for (int row = 0; row < R; ++row) {
                uint32_t value = height[row][C-1];
                for (int col = C-1; col >= 0; --col) {
                    uint32_t h = height[row][col];
                    if (h < value) {
                        reach[row][col] &= NOT_HORIZONTAL; 
                    }
                    value = std::max(value, h);
                }
            }
        }
                
        //debug(R,C,height,reach);

        {
            // top to bottom
            for (int col = 0; col < C; ++col) {
                uint32_t value = height[0][col];
                for (int row = 0; row < R; ++row) {
                    uint32_t h = height[row][col];
                    if (h < value) {
                        reach[row][col] &= NOT_VERTICAL; 
                    }
                    value = std::max(value, h);
                }
            }
        }
       
        //debug(R,C,height,reach);

        {
            // bottom to top
            for (int col = 0; col < C; ++col) {
                uint32_t value = height[R-1][col];
                for (int row = R-1; row >= 0; --row) {
                    uint32_t h = height[row][col];
                     if (h < value) {
                        reach[row][col] &= NOT_VERTICAL; 
                    }
                    value = std::max(value, h);
                }
            }
        }
                
        //debug(R,C,height,reach);

        bool result = true;
        for (size_t row = 0; row < R; ++row) {
            for (size_t col = 0; col < C; ++col) {
                if (reach[row][col] == NONE) {
                    result = NONE;
                }
            }
        }
        
        if (result) {
            out << "Case #" << i << ": YES" << endl;
        } else {
            out << "Case #" << i << ": NO" << endl;
        }
    }

    
    in.close();
    out.close();

    //system("pause");
}
