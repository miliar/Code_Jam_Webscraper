#include "sheep.h"

#include <assert.h>

Sheep::Sheep(int initial_val){
  for(int i=0; i<10; i++)
    digits_seen_[i]=false;

  initial_value_ = IntToVector(initial_val);
  number_ = initial_value_;
  MarkDigitsSeen();
}


void Sheep::Next(){
  int carry_over = 0;
  int digit;
  for(unsigned int i=0; i<number_.size(); i++){
    if (i<initial_value_.size())
      digit = initial_value_[i];
    else
      digit = 0;
    
    number_[i] += digit + carry_over;
    carry_over = 0;
    if (number_[i] >= 10){
      number_[i] -= 10;
      carry_over = 1;
    }
  }
  
  if(carry_over == 1)
    number_.push_back(1);

  MarkDigitsSeen();
}

std::vector<int> Sheep::IntToVector(int integer){
  assert(integer >= 0);

  
  std::vector<int> result;

  if (integer == 0){
    result.push_back(0);
  } else {
    while(integer > 0){
      result.push_back(integer % 10);
      integer /= 10;
    }
  }

  return result;
}

std::string Sheep::Display() const{
  std::string result="";

  auto itr = number_.rbegin();
  for(; *itr == 0 && itr != number_.rend(); itr++);

  for(; itr != number_.rend(); itr++){
    result += static_cast<char>(*itr + '0');
  }

  if (result == "")
    return "0";
  else
    return result;
}
bool Sheep::AllDigitsSeen() const{
  for(int i=0; i<10; i++)
    if(digits_seen_[i] == false)
      return false;
  return true;
}

void Sheep::MarkDigitsSeen() {
  for(const auto& digit: number_)
    digits_seen_[digit] = true;
}
