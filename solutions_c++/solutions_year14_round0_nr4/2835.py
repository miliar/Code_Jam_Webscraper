#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int main(int argc, char *argv[])
{
  if (argc < 2) {
    std::cout << "Usage: magic_trick [input_file]" << std::endl;
    return 0;
  }

  const char * filename = argv[1];  

  std::ifstream in(filename);
  if(!in.is_open()){
    std::cout << "error opening file " << filename << std::endl;
    return -1;
  }

  std::ofstream out("out.txt");
  if(!out.is_open()){
    std::cout << "error creating output file" << std::endl;
    return -2;
  }

  int test_count = 0;
  in >> test_count;

  for (int i = 0; i < test_count; ++i) {
    int blocks_count = 0;
    in >> blocks_count;
    std::vector<double> naomi_war;
    std::vector<double> ken_war;
    for (int k = 0; k < blocks_count; ++k) {
      double weight = 0;
      in >> weight;
      naomi_war.push_back(weight);
    }
    for (int k = 0; k < blocks_count; ++k) {
      double weight = 0;
      in >> weight;
      ken_war.push_back(weight);
    }

    std::sort(naomi_war.begin(), naomi_war.end());
    std::sort(ken_war.begin(), ken_war.end());
    std::vector<double> ken_dwar = ken_war;

    // std::cout << "naomi ";
    // for (int j = 0; j  < blocks_count; ++j ) {
    //   std::cout << naomi_war[j] << " ";
    // } 
    // std::cout << std::endl;
    // std::cout << "ken ";
    // for (int j = 0; j  < blocks_count; ++j ) {
    //   std::cout << ken_war[j] << " ";
    // } 
    // std::cout << std::endl;

    int naomi_war_score = 0;
    for (int bindex = 0; bindex < blocks_count; ++bindex) {
      double naomi_block = 0;
      double ken_block = 0;
      naomi_block = naomi_war[bindex];

      bool found_hevier = false;
      for (auto iter = ken_war.begin();
	    iter!=ken_war.end(); ++iter) {
	if (*iter > naomi_block){
	  ken_block = *iter;
	  found_hevier = true;
	  ken_war.erase(iter);
	  break;
	}
      }
      if (!found_hevier)
	ken_block = ken_war[0];

      if (naomi_block > ken_block)
	++naomi_war_score;
    }

    int naomi_dwar_score = 0;
    for (int k = 0; k < blocks_count; ++k) {
      bool min_naomi = false; //naomi has minimum elems
      bool max_ken = false; //ken has maximum elems
      // std::cout << ken_dwar[ken_dwar.size()-1] << std::endl;
      if (ken_dwar[ken_dwar.size()-1] > 
          naomi_war[naomi_war.size()-1])
	max_ken = true;
      if (naomi_war[0] < ken_dwar[0])
	min_naomi = true;

      if (naomi_war.size() == 1U) {
	if (naomi_war[0] > ken_dwar[0]){
	  ++naomi_dwar_score;
	  break;
	}
      }

      if (min_naomi || max_ken) {
	naomi_war.erase(naomi_war.begin());
        ken_dwar.erase(ken_dwar.end()-1);
      } else {
	naomi_war.erase(naomi_war.begin());
	ken_dwar.erase(ken_dwar.begin());
	++naomi_dwar_score;
      }

    // std::cout << "naomi ";
    // for (int j = 0; j  < naomi_war.size(); ++j ) {
    //   std::cout << naomi_war[j] << " ";
    // } 
    // std::cout << std::endl;
    // std::cout << "ken ";
    // for (int j = 0; j  < ken_dwar.size(); ++j ) {
    //   std::cout << ken_dwar[j] << " ";
    // } 
    // std::cout << std::endl;

    }

    out << "Case #" << i+1 << ": " 
	<< naomi_dwar_score << " "
	<< naomi_war_score << std::endl;
  }

  in.close();
  out.close();

  return 0;
}
