struct SheepCounter
{
  static unsigned long getLastCount(const unsigned long n);
};

unsigned long SheepCounter::getLastCount(const unsigned long n)
{
  if (n == 0) return -1;
  unsigned long last = 0;
  std::set<int> seen_digits;
  while (seen_digits.size() < 10) {
    last += n;
    unsigned long last_tmp = last;
    while (last_tmp > 0) {
      seen_digits.insert(last_tmp%10);
      last_tmp -= last_tmp%10;
      last_tmp /= 10;
    }
  }
  return last;
}

int main()
{
  unsigned int input_size;
  std::cin >> input_size;
  std::vector<unsigned long> inputs;
  for (unsigned int i = 0; i < input_size; i++) {
    unsigned long input;
    std::cin >> input;
    inputs.push_back(input);
  }
  for (unsigned int i = 0; i < inputs.size(); i++) {
    if (inputs[i] > 0) std::cout << "Case #" << i+1 << ": " << SheepCounter::getLastCount(inputs[i]) << std::endl;
    else std::cout << "Case #" << i+1 << ": INSOMNIA" << std::endl;
  }
}
