#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>



using namespace std;


void quicksort_helper(double array[], int a, int b) {
	if (a >= b) return;
	swap(array[a], array[a + (rand() % (b - a + 1))]);
	int m = a;
	for (int i = a+1; i <= b; i++) {
		if (array[i] < array[a]) {
			swap(array[++m], array[i]);
    }
	}
	swap(array[a],array[m]);
	quicksort_helper(array, a, m-1);
	quicksort_helper(array, m+1, b);
}

void quicksort(double array[], int len) {
    quicksort_helper(array, 0, len-1);
  }

int solve_war(double val_n[], double val_k[], int n) {
  if (n < 1) return 0;
  int win = (val_n[n-1] > val_k[n-1]) ? 1 : 0;
  int res = 0;
  if (win) 
    res = solve_war(val_n, val_k+1, n-1);
  else
    res = solve_war(val_n, val_k, n-1);
  return win + res;
}

int solve_deceit(double val_n[], double val_k[], int n) {
  if (n < 1) return 0;
  if (n == 1) return (val_n[0] > val_k[0]) ? 1 : 0;
  
  
  if (val_n[0] < val_k[0]) 
    return solve_deceit(val_n+1, val_k, n-1);
  else
    return 1 + solve_deceit(val_n+1,val_k+1,n-1);
}

void solve(int k, double val_n[], double val_k[], int n) {
  quicksort(val_n,n);
  quicksort(val_k,n);
  int d = solve_deceit(val_n, val_k, n);
  int w = solve_war(val_n,val_k,n);
  printf("Case #%d: %d %d\n", k, d, w);
}

void parse_numbers(string s, double num[], int len){
    string d = " ";
    int n = 0;
    string t = "";
    size_t pos = 0;
    while ( ((pos = s.find(d)) != string::npos) && n < len) {
        t = s.substr(0, pos);
        if (!t.empty())
          num[n++] = atof(t.c_str());
        s.erase(0, pos + d.length());
      }
      if (n < len) {
        t = s.substr(0, pos);
        if (!t.empty())
          num[n++] = atof(t.c_str());
      }
}

void file_getline(ifstream& infile){
    string s="";    
        
    getline(infile,s);
    int t = atoi(s.c_str());
    
    // iterate cases
    for (int k = 1; k <= t; k++)
    {
      getline(infile,s);
      int n = atoi(s.c_str());
    
      double val_n[n];
      double val_k[n];
      // get values
      getline(infile,s);
      parse_numbers(s, val_n, n);

      getline(infile,s);
      parse_numbers(s, val_k, n);
 
      solve(k, val_n, val_k, n);
  }

}


int main(int argc, char* argv[]) {
  
  if (argc < 2)
    return -1;
    
  char* filename = argv[1];
    
  ifstream infile;
  infile.open(filename);
  if(infile) {
    file_getline(infile);
    infile.close();
  } 
}

