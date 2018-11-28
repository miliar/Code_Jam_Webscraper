#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <numeric> 

#include <boost/unordered_set.hpp>
#include <boost/foreach.hpp>
#include <boost/range/irange.hpp>

// #include <boost/multiprecision/mpfr.hpp>

using namespace boost;
//using namespace multiprecision;
using namespace std;


int Bgcd(int a, int b)
{
    for (;;)
    {
        if (a == 0) return b;
        b %= a;
        if (b == 0) return a;
        a %= b;
    }
}

int Blcm(int a, int b)
{
    int temp = Bgcd(a, b);

    return temp ? (a / temp * b) : 0;
}


struct Barber
{
  int time;
  int index;
  int time_taken;
};

bool sort_on_time(Barber * b1, Barber * b2)
{
  return b1->time < b2->time;
}

bool sort_on_index(const Barber * b1, const Barber * b2)
{
  return b1->index < b2->index;
}



int main(int argc, char * argv[])
{
  
    int T;
  
  cin >> T;
  
  BOOST_FOREACH(int t, irange(0, T))
  {
    
    int B, N;
    
    cin >> B;
    cin >> N;
    

    
    std::vector<int> M;
    M.resize(B);
    
    std::list<Barber *> barbers_available;
    std::list<Barber *> barbers_busy;

    
    BOOST_FOREACH(int k, irange(0, B))
    {

      cin >> M[k];
      Barber * b = new Barber;
      b->index = k;
      b->time_taken = M[k];
      b->time = 0;
      barbers_available.push_back(b);
      
    }
    
    int multiple = std::accumulate(M.begin(), M.end(), 1, Blcm);


    std::vector<int> haircuts_each_multiple;
    int total_haircuts_each_multiple = 0;
    BOOST_FOREACH(int k, irange(0, B))
    {
      haircuts_each_multiple.push_back(multiple / M[k]);
      total_haircuts_each_multiple += multiple / M[k];
    }
    
    int new_N;
    
    new_N = N % total_haircuts_each_multiple;
    
    if (new_N == 0)
      new_N = total_haircuts_each_multiple;
    
    
 
    Barber * last_barber;
    BOOST_FOREACH(int n, irange(0, new_N))
    {
      if (barbers_available.size() == 0)
      {
	
	barbers_busy.sort(sort_on_time);
	
	int time = barbers_busy.front()->time;
	
	while (barbers_busy.size() > 0 && barbers_busy.front()->time == time)
	{
	  barbers_available.push_back(barbers_busy.front());
	  barbers_busy.pop_front();
	}
      }
      
      barbers_available.sort(sort_on_index);
      
      barbers_available.front()->time += barbers_available.front()->time_taken;
      barbers_busy.push_back(barbers_available.front());
      last_barber = barbers_available.front();
      barbers_available.pop_front();
      
    }
    
    
    cout << "Case #" << (t+1) << ": " << (last_barber->index+1) << endl;
    

	  
  }
}