struct FlipCounter
{
  static int flipsToTarget(const std::string& input, const char target);
};

int FlipCounter::flipsToTarget(const std::string& input, const char target)
{
  for (int i = input.size()-1; i >= 0; i--) {
    if (input[i] != target) {
      if (target == '+') return FlipCounter::flipsToTarget(input.substr(0,i+1), '-') + 1;
      else return FlipCounter::flipsToTarget(input.substr(0,i+1), '+') + 1;
    }
  }
  return 0; // no flips necessary if all checks out                                                                                                                       
}

int main() {
  unsigned int input_size;
  std::cin >> input_size;
  std::vector<std::string> inputs;
  for (unsigned int i = 0; i < input_size; i++) {
    std::string in;
    std::cin >> in;
    inputs.push_back(in);
  }
  for (unsigned int i = 0; i < inputs.size(); i++) {
    //std::cout << inputs[i] << std::endl;                                                                                                                                
    std::cout << "Case #" << i+1 << ": " << FlipCounter::flipsToTarget(inputs[i], '+') << std::endl;
  }
}

