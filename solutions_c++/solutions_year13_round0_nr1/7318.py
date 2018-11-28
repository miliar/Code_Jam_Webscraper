#include <string>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <sstream>


using namespace std;
class PlayerMoves {
public:
    PlayerMoves() {
        rows.resize(4);
        columns.resize(4);
        bottom_l_top_r = 0;
        top_l_bottom_r = 0;
    }
    void has_a_point(int x, int y) {
        columns[x]++;
        rows[y]++;
        if (x == y) {

            ++top_l_bottom_r;
        } else if ((x == 3 && y == 0) || (x == 2 && y == 1) || (x == 1 && y == 2) || (x == 0 && y == 3))
            ++bottom_l_top_r;
    
    }
    bool wins(int x, int y) const {
        if (columns[x] >= 4 || rows[y] >= 4 || bottom_l_top_r >= 4 || top_l_bottom_r >= 4)
            return true;
        return false;
    }
    void reset() {
        rows.clear();
        rows.resize(4);
        columns.clear();
        columns.resize(4); 
        bottom_l_top_r = 0;
        top_l_bottom_r = 0;
    }
    vector<int> rows, columns;
    int bottom_l_top_r, top_l_bottom_r;
};
void append_winner(int game, string winner, vector<string> &results) {
    stringstream res;
    res << "Case #" << game << ": " << winner << endl;
    results.push_back(res.str());
}
int main(int argc, char* argv[]) {
    string filename = argv[1];
    ifstream input_file(filename.c_str());    
    vector<vector <int> > horizontal(4), vertical(4);
    if (input_file.is_open()) {
        vector<string> winners;
        PlayerMoves Xes, Oes;
        string line;
        int cases, game_number = 0, num_empty = 0;
        bool case_line = true, have_a_winner = false;
        int y = 0;
        while(input_file.good()) {
            getline(input_file, line);
            if (case_line) {
                case_line = false;
                
                
                if (line.empty()) {
                    if (!have_a_winner && game_number > 0) {
                        string no_win = num_empty > 0 ? "Game has not completed" : "Draw";
                        append_winner(game_number, no_win, winners);
                        Xes.reset(); Oes.reset();
                        num_empty = 0;
                    }
                    have_a_winner = false;
                    ++game_number;
                    continue;
                }
                ++game_number;
                have_a_winner = false;
                cases = atoi(line.c_str());
                
              
            } else {
                if (line.empty()) continue;
                if (!have_a_winner) {                    
                    for(int x = 0; x < 4; ++x) {
                        char player = line[x];
                        switch(player) {
                            case 'X' :
                                Xes.has_a_point(x, y);
                                break;
                            case 'O' :
                                Oes.has_a_point(x, y);
                                break;
                            case 'T' :
                                Xes.has_a_point(x, y);
                                Oes.has_a_point(x, y);
                                break;
                            default :
                                ++num_empty;
                                break;
                        }
                        if (Xes.wins(x, y)) {
                            append_winner(game_number, "X won", winners);
                            have_a_winner = true;
                            Xes.reset(); Oes.reset();
                            num_empty = 0;
                            break;
                        } else if (Oes.wins(x, y)) {
                            append_winner(game_number, "O won", winners);
                            have_a_winner = true;
                            Xes.reset(); Oes.reset();
                            num_empty = 0;
                            break;
                        }
                    }
                }
                ++y;
                if (y >= 4) {
                    y = 0;
                    case_line = true;
                }
            }
        }
        /*if (!have_a_winner && game_number > 0) {
            string no_win = num_empty == 0 ? "Game has not completed" : "Draw";
            append_winner(game_number, no_win, winners);
            num_empty = 0;
        }*/

        input_file.close();
        ofstream output_file("results.txt", ios_base::trunc);
        if (output_file.is_open()) {
            for (int i = 0; i < winners.size(); ++i) {
                output_file << winners[i];
            }
            output_file.close();
        }
    } else {
        cout << "Error opening file " << filename << endl;
    }    
    return 1;
}