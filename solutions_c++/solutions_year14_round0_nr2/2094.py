#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>



using namespace std;


void solve(int k, double c, double f, double x) {
  
  int n = 0; // number of farms
  double curr_rate = 2;
  double total = 0;
  bool stop = false;
  
  while (!stop) {
    double stay = x/curr_rate;
    double buy = c/curr_rate + x/(2+(n+1)*f);
    if (stay <= buy) {
      total += stay;
      stop  = true;
    }
    else {
      total += c/curr_rate;
      n++;
      curr_rate = 2 + n*f;
    }
  }
  
  printf("Case #%d: %.7f\n", k, total);
    
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
    
    double val[3];
    
    getline(infile,s);
    int n = atoi(s.c_str());
    
    // iterate cases
    for (int k = 1; k <= n; k++)
    {
      // get values
      getline(infile,s);
      parse_numbers(s, val, 3);
 
      solve(k, val[0], val[1], val[2]);
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

