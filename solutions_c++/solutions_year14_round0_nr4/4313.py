#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <list> 
using namespace std;

int main() {
	int T;
	int n;
	double aux;
	
	

	cin >> T;
	for (int i=1; i<=T; i++) {
	  list<double> ken1, ken2, naomi1, naomi2;  
	
	  cin >> n;
	  for(int j=0; j<n; j++) {
	    cin >> aux;
	    naomi1.push_back(aux);
	    naomi2.push_back(aux);
	  }
	  for(int j=0; j<n; j++) {
	    cin >> aux;
	    ken1.push_back(aux);
	    ken2.push_back(aux);
	  }
	  
	    
	  ken1.sort();
	  ken2.sort();
 	  naomi1.sort();
 	  naomi2.sort();
 	  
 	  int war=0, dec=0;
 	  
  	while(!naomi1.empty()) {
  	  if(naomi1.back() > ken1.back()) {
  	    war++;
  	    naomi1.pop_back();
  	    ken1.pop_front();
  	  }
  	  else {
  	    double np = naomi1.back();
 	      list<double>::iterator it = ken1.begin();
 	      while(*it < np && it != ken1.end()) advance(it,1);
 	      ken1.erase(it);
 	      naomi1.pop_back();
 	    }
 	  }
 	  
// 	  while(naomi2.back() < ken2.back()) {
// 	    naomi2.pop_back();
// 	    ken2.pop_back();
// 	  }
 	  
 	  while(!naomi2.empty()) {
 	    double np = ken2.front();
      list<double>::iterator it = naomi2.begin();
      while(*it < np && it != naomi2.end()) advance(it,1);
      if (it == naomi2.end()) break;
      naomi2.erase(it);
      ken2.pop_front();
      dec++;
 	  }
 	  
	  printf("Case #%d: %d %d \n", i, dec, war);
	  
  }
		
}

