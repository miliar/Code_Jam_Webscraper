
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

constexpr int row_max = 4;
constexpr int col_max = 4;

class Turn{
public:
  int answer;
  int cards[row_max][col_max];
};

bool getTurn(Turn &turn){
  std::string line;
  if(!std::getline(std::cin, line)) return false;
  turn.answer = atoi(line.c_str());

  for(int i=0;i<row_max;i++){
    if(!std::getline(std::cin, line)) return false;
    std::stringstream ss(line);
    for(int j=0;j<col_max;j++){
      ss >> turn.cards[i][j];
    }
  }
  return true;
}

std::vector<int> getCandidate(const Turn &turn){
  std::vector<int> candidate;
  for(int i=0;i<col_max;i++){
    candidate.push_back(turn.cards[turn.answer-1][i]);
  }
  return std::move(candidate);
}

std::vector<int> shrinkCandidate(const std::vector<int> &previous, const std::vector<int> &current){
  auto candidate = previous;
  for(auto i : previous){
    if(std::find(current.begin(), current.end(), i) == current.end()){
      //新しい候補に発見できない要素を削除
      candidate.erase(std::remove(candidate.begin(), candidate.end(), i), candidate.end());
    }
  }
  return std::move(candidate);
}

int main(){
  int cases;
  {
    std::string line;
    if(!std::getline(std::cin, line)) return false;
    cases = atoi(line.c_str());
  }
  std::vector<Turn> turns;
  while(true){
    Turn turn;
    if(getTurn(turn)){
      turns.push_back(turn);
    }
    else{
      break;
    }
  }
  std::cerr << "cases" << cases << std::endl;

  int current_case = 1;
  std::vector<int> previous_candidate;
  bool is_first_turn = true;
  int turn_counter = 0;
  for(auto turn : turns){
    std::vector<int> candidate = getCandidate(turn);
    if(is_first_turn){
      previous_candidate = candidate;
      is_first_turn = false;
    }
    else{
      auto new_candidate = shrinkCandidate(previous_candidate, candidate);
      if(new_candidate.size() == 0){
        printf("Case #%d: Volunteer cheated!\n", current_case);
        current_case++;
        is_first_turn = true;
        turn_counter = 0;
        continue;
      }

      if(new_candidate == candidate){
        printf("Case #%d: Bad magician!\n", current_case);
        current_case++;
        is_first_turn = true;
        turn_counter = 0;
        continue;
      }

      if(new_candidate.size() == 1){
        printf("Case #%d: %d\n", current_case, new_candidate[0]);
        current_case++;
        is_first_turn = true;
        turn_counter = 0;
        continue;
      }
      previous_candidate = new_candidate;
      turn_counter++;
      if(turn_counter == 1){
        printf("Case #%d: Bad magician!\n", current_case);
        current_case++;
        is_first_turn = true;
        turn_counter = 0;
        continue;
      }
    }
  }

  return 0;
}
