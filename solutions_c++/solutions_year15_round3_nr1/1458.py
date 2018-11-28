#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <numeric> 

#include <boost/unordered_set.hpp>
#include <boost/unordered_map.hpp>
#include <boost/foreach.hpp>
#include <boost/range/irange.hpp>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/mpfr.hpp>
#include <boost/rational.hpp>


using namespace boost;
using namespace multiprecision;
using namespace std;


template <typename T>
struct node
{
  T solution;
  node<T> * previous;
  
  node(T & solution, node<T> * previous = NULL) :
    solution(solution), previous(previous)
  {
    
  }
};

template <typename T>
void print_node(node<T> * current_node, string sep)
{
  string current_sep = "";;
    while (current_node != NULL)
    {
      cout << current_sep << current_node->solution;
      current_node = current_node->previous;
      current_sep = sep;
    }
}

struct solution
{
  int x, y;
  
};

int main(int argc, char * argv[])
{
  
  int T;
  
  cin >> T;
  
  BOOST_FOREACH(int t, irange(0, T))
  {
    int R, C, W;
    
    cin >> R;
    cin >> C;
    cin >> W;
    
   
    
    int trials = 0;
    BOOST_FOREACH(int r, irange(0, R))
    {
      trials += C / W;
    }
    
    //cout << trials;
    
    if (C % W == 0)
    {
      trials += W - 1;
    }
    else
    {
      trials += W;
    }
    //int new_C = W + C % W;
    
    
    cout << "Case #" << (t+1) << ": " << trials << endl; // << count << endl;
    
    

    
    //cout << endl;
    
  }
  
  //print_node(current, " <- ");
  //cout << endl;
  
  return 0;
}