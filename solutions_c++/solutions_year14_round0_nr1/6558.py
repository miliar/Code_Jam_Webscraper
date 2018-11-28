#include <iostream>
#include <algorithm>
#include <iterator>
#include <set>

struct null_output_iterator : 
    std::iterator< std::output_iterator_tag,
                   null_output_iterator > {
    /* no-op assignment */
    template<typename T>
    void operator=(T const&) { }

    null_output_iterator & operator++() { 
        return *this; 
    }

    null_output_iterator operator++(int) { 
        return *this;
    }

    null_output_iterator & operator*() { return *this; }
};

struct input_case {
  std::set<int> first;
  std::set<int> second;
};

std::set<int> read_hint(std::istream& in) {
  int row;
  in >> row;

  std::istream_iterator<int> it(in);
  std::advance(it, (row-1)*4);

  std::set<int> result;
  std::copy_n(it, 4, std::inserter(result, result.begin()));

  std::advance(it, (4-row)*4);
  return result;
}

std::istream& operator>>(std::istream& in, input_case& input) {
  input.first = read_hint(in);
  input.second = read_hint(in);
  return in;
}

int solve_case(input_case input) {
  std::set<int> intersection;
  std::set_intersection(input.first.begin(), input.first.end(), input.second.begin(), input.second.end(), std::inserter(intersection, intersection.begin()));
  if(intersection.size() == 0) return -1;
  if(intersection.size() > 1) return 0;
  return *intersection.begin();
}

void print_case(std::ostream& out, int value) {
  if(value == -1) out << "Volunteer cheated!";
  else if(value == 0) out << "Bad magician!";
  else out << value;
}

int main() {
  int num_cases;
  std::cin >> num_cases;
  std::vector<input_case> cases;
  std::copy_n(std::istream_iterator<input_case>(std::cin), num_cases, std::back_inserter(cases));
  std::for_each(cases.begin(), cases.end(), [](input_case const& c) {
      static int case_nr = 1;
      std::cout << "Case #" << case_nr << ": ";
      print_case(std::cout, solve_case(c));
      std::cout << "\n";
      case_nr++;
    });
}
