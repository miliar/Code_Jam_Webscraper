#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <utility>

int main() {
  std::ifstream file;
  file.open("input.txt");
  std::ofstream o("output.txt");

  std::string line;
  std::getline(file, line);
  std::string parties;
  std::string per_party;
  int current_case = 1;
  while(std::getline(file, parties) && std::getline(file, per_party)) {
    std::stringstream parties_stream;
    parties_stream.str(per_party);
    std::multimap<int, std::string, std::greater<int> > heap;
    int number_of_parties = std::stoi(parties);
    for (int i = 0; i < number_of_parties; ++i) {
      int current_party_members;
      parties_stream >> current_party_members;
      heap.insert(std::make_pair(current_party_members, std::string(1, 'A' + i)));
    }
    std::stringstream order;
    while (heap.size() > 0) {
      if (heap.size() > 3) {
	int top = heap.begin()->first;
	if (top > 2) {
	  order << heap.begin()->second << heap.begin()->second << " ";
	  auto new_top_pair = std::make_pair(heap.begin()->first - 2, heap.begin()->second);
	  heap.erase(heap.begin());
	  if (new_top_pair.first > 0) { 
	    heap.insert(new_top_pair); 
	  }
	} else {
	  int second_top = (++heap.begin())->first;
	  int third_top = (++++heap.begin())->first;
	  if (second_top - third_top > 1) {
	    auto top_iterator = heap.begin();
	    auto second_top_iterator = ++heap.begin();
	    order << top_iterator->second << second_top_iterator->second << " ";
	    auto new_top_pair = std::make_pair(top_iterator->first - 1, top_iterator->second);
	    auto new_second_pair = std::make_pair(second_top_iterator->first - 1, second_top_iterator->second);
	    heap.erase(top_iterator);
	    heap.erase(second_top_iterator);
	    if (new_top_pair.first > 0) { 
	      heap.insert(new_top_pair); 
	    }
	    if(new_second_pair.first > 0) {
	      heap.insert(new_second_pair);
	    }
	  } else {
	    order << heap.begin()->second << heap.begin()->second << " ";
	    auto new_top_pair = std::make_pair(heap.begin()->first - 2, heap.begin()->second);
	    heap.erase(heap.begin());
	    if (new_top_pair.first > 0) { 
	      heap.insert(new_top_pair);
	    }
	  }
	}
      } else if (heap.size() == 3) {
	auto top_iterator = heap.begin();
	order << top_iterator->second << " ";
	auto new_top_pair = std::make_pair(heap.begin()->first - 1, heap.begin()->second);
	heap.erase(heap.begin());
	if (new_top_pair.first > 0) { 
	  heap.insert(new_top_pair); 
	}
      } else {
	auto top_iterator = heap.begin();
	auto second_top_iterator = ++heap.begin();
	order << top_iterator->second << second_top_iterator->second << " ";
	auto new_top_pair = std::make_pair(top_iterator->first - 1, top_iterator->second);
	auto new_second_pair = std::make_pair(second_top_iterator->first - 1, second_top_iterator->second);
	heap.erase(top_iterator);
	heap.erase(second_top_iterator);
	if (new_top_pair.first > 0) { 
	  heap.insert(new_top_pair); 
	}
	if(new_second_pair.first > 0) {
	  heap.insert(new_second_pair);
	}	

      }
    }
    o << "Case #" << current_case << ": " << order.str() << std::endl;
    ++current_case;
  } 
}
