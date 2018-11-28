#include <fstream>
#include <vector>
#include <utility>
using std::vector;
using std::pair;
vector<short > result;  // -1 for multiple answers
                        // 0 for volunteer cheat
struct ans_case{
    short table[4][4];
    short answer;
};
vector<pair<ans_case,ans_case> > input_table;
                        
void input(){
    std::ifstream ifp("input.txt");
    int case_size;
    ifp >> case_size;
    for (size_t i = 0; i < case_size*2; ++i){
        ans_case temp;
        ifp >> temp.answer;
        for (size_t j = 0; j < 4; ++j)
            for (size_t k = 0; k < 4; ++k)
                ifp >> temp.table[j][k];
        if (i%2==0)
            input_table.push_back(pair<ans_case,ans_case>(temp,ans_case()));
        else
            input_table.back().second=temp;
    }
    ifp.close();
}

void output(){
    std::ofstream ofp("output.txt");
    for (size_t i = 0; i < result.size(); ++i){
        ofp << "Case #"<<i+1<<": ";
        switch (result[i]){
            case 0: ofp << "Volunteer cheated!"; break;
            case -1: ofp << "Bad magician!"; break;
            default: ofp << result[i];
        }
        ofp << std::endl;
    }
    ofp.close();
}

void algorithm(){
    for (size_t i = 0; i < input_table.size(); ++i){
        const short* row1pt=input_table[i].first.table[input_table[i].first.answer-1]; 
        const short* row2pt=input_table[i].second.table[input_table[i].second.answer-1];
        vector<short> candidates;
        for (size_t j = 0; j < 4; ++j)
            for (size_t k = 0; k < 4; ++k)
                if (row1pt[j] == row2pt[k]) candidates.push_back(row1pt[j]);
        switch (candidates.size()){
            case 0: result.push_back(0);break;
            case 1: result.push_back(candidates[0]);break;
            default: result.push_back(-1);break;
        }
    }
}

int main()
{
    input();
    algorithm();
    output();
    return 0;
}