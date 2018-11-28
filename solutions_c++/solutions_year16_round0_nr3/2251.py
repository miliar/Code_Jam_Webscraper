// uses big int implementation from boost, 
// http://www.boost.org/

  #include <stdlib.h>
  #include <stdio.h>
#include <math.h>

  #include <iostream>
  #include <vector>
  #include <algorithm>
  #include <fstream>
  #include <string>
  #include <sstream>
  #include <unordered_set>
  #include <set>
  #include <bitset>
  #include <map>
  #include <boost/multiprecision/cpp_int.hpp>

  using namespace std;  
  using namespace boost::multiprecision;
  
  const int ND = 32;
  int128_t interpretBaseN(const bitset<ND> &a, int N) {  
    int128_t result = 0;
    int128_t base = 1;
    for (int i = ND-1; i >= 0; --i) {    
      if (a[i] == 1) {      
	result += base;
      }
      base *= N;
    }
    return result;
  }
  
  void generateNumber(int density, bitset<ND> &a) {  
    for (int i = 0; i < ND; ++i) {    
      if (rand()%1000 < density) {      
	a[i] = 1;
      }
    }
    a[0] = 1;
    a[ND-1] = 1;
  }
  
  void getPrimes(int n, unordered_set<int> &v) {  
    vector<char> cands(n+1, 'y');
    int mx = ceil(sqrt(n));
    for (int i = 2; i <= mx; ++i) {          
      int t = i * i;
      while (t <= n) {      
	cands[t] = 'n';
	t += i;
      }
    }
    for (int i = 2; i <= n; ++i) {    
      if (cands[i] == 'y') {      
	v.insert(i);
      }
    }
  }
  
   const char *sequenceToString(int128_t a) {  
    string s;
    if (a == 0) {
      s = "0";
    } else {    
      while (a != 0) {      
	int t = static_cast<int> (a % 10);
	char c = '0' + t;	
	s.push_back(c);	
	a = a / 10;
      }
    }
    reverse(s.begin(), s.end());
    //cout << s << endl;
    char *cstr = new char[s.length()+1];
    strcpy (cstr, s.c_str());
    return cstr;  
  }


  int main() {    
    ifstream input("in.txt");
    FILE *out;
    out = fopen("out.txt", "w");
    string s;
    getline(input, s);	  
    size_t sz;
    int T = stoi(s, &sz);
    for (int iter = 1; iter <= T; ++iter) {
    
      getline(input, s);
		  istringstream ss(s);		  
		  int N_;
		  ss >> N_;
		  int J;
		  ss >> J;
    unordered_set<int> primes;
    int n = 10000;
    getPrimes(n, primes);       
    map<int128_t, vector<int> > jamcoins;
    // Generate jamcoins.
    int density; 
    int count = 0;
    while (jamcoins.size() < J && count < 10000) {    
      bitset<ND> bs;
      density = rand() % 1000 + 1;
      generateNumber(density, bs);
      bool isJamcoin = true;
      int128_t interp;
      vector<int> divisors;
      for (int base = 2; base <= 10; ++base) {      
	interp = interpretBaseN(bs, base);
	unordered_set<int>::iterator it = primes.begin();
	bool hasDivisor = false;
	for (; it != primes.end(); ++it) {	
	  if (interp != (*it)  &&  interp % (*it) == 0) {	  
	    hasDivisor = true;
	    divisors.push_back(*it);
	    break;
	  }
	}
	if (!hasDivisor) {	  
	  isJamcoin = false;
	  break;
	}	
      }
      if (isJamcoin) {      
	jamcoins[interpretBaseN(bs, 10)] = divisors;
	cout << jamcoins.size() << endl;
      }
      ++count;
    }	 
	  		 	  
		  fprintf(out, "Case #%d:\n", iter);
		  map<int128_t, vector<int> >::iterator myIt = jamcoins.begin();		   
		  for (; myIt != jamcoins.end(); ++myIt) {
		    const char *temp = sequenceToString(myIt->first);
		    vector<int> v = myIt->second;
		    fprintf(out, "%s %d %d %d %d %d %d %d %d %d\n", temp, v[0], v[1], v[2], v[3], v[4], 
		      v[5], v[6], v[7], v[8]);
		  }
	  }	  
	  fclose(out);	  
	  return 0;
  }


