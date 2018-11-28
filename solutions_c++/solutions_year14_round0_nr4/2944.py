#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<double> BlockWeights;

/*size_t PlayDeceitfulWar(const BlockWeights & naomis_blocks, const BlockWeights & kens_blocks)
{
  BlockWeights::const_iterator naomis_choice = naomis_blocks.begin();
  BlockWeights::const_reverse_iterator kens_choice = kens_blocks.rbegin();
  while (naomis_choice != naomis_blocks.end())
  {
    if (*naomis_choice > *kens_choice) 
    {
      return naomis_blocks.end() - naomis_choice;
    }
    ++naomis_choice;
    ++kens_choice;
  }
  return 0;
}*/

size_t PlayDeceitfulWar(BlockWeights & naomis_blocks, BlockWeights & kens_blocks)
{
  BlockWeights::const_iterator kens_choice = kens_blocks.begin();
  BlockWeights::iterator naomis_choice;
  size_t result = 0;
  while (kens_choice != kens_blocks.end())
  {
    naomis_choice = upper_bound(naomis_blocks.begin(), naomis_blocks.end(), *kens_choice);
    if (naomis_choice != naomis_blocks.end()) 
    {
      ++result;
      naomis_blocks.erase(naomis_choice);
    }
    ++kens_choice;
  }
  return result;
}

size_t PlayWar(const BlockWeights & naomis_blocks, const BlockWeights & kens_blocks)
{
  BlockWeights::const_iterator kens_choice = kens_blocks.begin();
  BlockWeights::const_iterator naomis_choice = naomis_blocks.begin();
  
  while (naomis_choice != naomis_blocks.end()
         && (kens_choice = upper_bound(kens_choice, kens_blocks.end(), *naomis_choice)) != kens_blocks.end())
  {
    ++naomis_choice;
    ++kens_choice;
  }

  return naomis_blocks.end() - naomis_choice;
}

int main(int argc, char** argv)
{
  size_t number_of_testcases;
  cin >> number_of_testcases;
  for (size_t tc_number = 1; tc_number <= number_of_testcases; ++tc_number)
  {
    size_t number_of_blocks;
    cin >> number_of_blocks;
    
    BlockWeights naomis_blocks(number_of_blocks);
    for (size_t i = 0; i < number_of_blocks; ++i) cin >> naomis_blocks[i];
    std::sort(naomis_blocks.begin(), naomis_blocks.end());
    
    BlockWeights kens_blocks(number_of_blocks);
    for (size_t i = 0; i < number_of_blocks; ++i) cin >> kens_blocks[i];
    std::sort(kens_blocks.begin(), kens_blocks.end()); 
    
    const size_t war_score = PlayWar(naomis_blocks, kens_blocks);
    const size_t deceitful_war_score = PlayDeceitfulWar(naomis_blocks, kens_blocks);
    cout << "Case #" << tc_number << ": " << deceitful_war_score << " " << war_score << endl;
  }
}