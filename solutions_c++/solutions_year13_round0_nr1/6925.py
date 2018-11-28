#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{

    if(argc < 3)
    {
            cout << "Oops - not enough command line parameters\n\n";
            system("PAUSE");
            return EXIT_FAILURE;
    }   
    
    ifstream input;
    input.open(argv[1]);
    
    ofstream output;
    output.open(argv[2]);
    
    int m_cases;
    input >> m_cases;
    
    char * m_result_text[4] = {"Game has not completed", "X won", "O won", "Draw"};
    
    for(int count =0; count < m_cases; count++)
    {
        char m_game[10][4];  // we will look at the game as 10 possible quad outcomes
        char * m_p = m_game[0];
        int m_board_full = 1;
        for(int inner = 0; inner < 16; inner++) 
        {
                input >> * m_p;
                if(*m_p == '.') m_board_full = 0;
                m_p++;
        }
        // ok. thats the core data read - next transpose to the next four!
        int row_index = 4; 
        for(int outer =0; outer < 4; outer++)
        {
                for(int inner = 0; inner < 4; inner++)
                {
                     m_game[row_index][inner] = m_game[inner][outer];   
                }
                row_index++;
        }
        // and finally the diagonal!
        for(int outer = 0; outer < 4; outer++)
        {
            m_game[8][outer] = m_game[outer][outer];    
            m_game[9][outer] = m_game[outer][3 - outer];    
        } 
        //
        // Next check for the result by trying each of the 10 possible lines
        //
        int result = 0; //incomplete is the default
        for(int outer = 0; outer < 10; outer++)
        {
            int m_xcount = 0;      
            int m_ocount = 0;      
            int m_tcount = 0;  
            for(int inner = 0; inner < 4; inner++)
            {
                    if(m_game[outer][inner] == '.') break;
                    else if(m_game[outer][inner] == 'X') m_xcount++;
                    else if(m_game[outer][inner] == 'O') m_ocount++;
                    else m_tcount++;
                    if(m_xcount && m_ocount) break; 
            } 
            // speed could be improved here - but not necessary!
            if((m_xcount + m_tcount) >= 4)
            {
                  result = 1; // x win
                  break;         
            }   
            // speed could be improved here - but not necessary!
            else if((m_ocount + m_tcount) >= 4)
            {
                  result = 2; // o win
                  break;         
            }  
            else if(!result && m_board_full) result = 3; // draw 
            //
            // Just send to the file!
            //
        }       
        output << "Case #" << count+1 << ": " << m_result_text[result] << "\n";
    }
    
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
