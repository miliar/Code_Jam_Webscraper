#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>



using namespace std;


void solve(int k, int arr1[][4], int arr2[][4], int a1, int a2) {
  int* row1 = arr1[a1-1];
  int* row2 = arr2[a2-1];
  
  int card = -1;
  bool stop = false;
  
  int i;
  for (i = 0; i < 4; i++)
  {
    for (int j = 0; j < 4; j++)
    {
      if (row1[i] == row2[j] && card < 0)
      {
        card = row1[i];
      }
      else if (row1[i] == row2[j])
      {
        printf("Case #%d: Bad magician!\n",k);
        return;
      }
    }
  }
  
  if (card < 0)
    printf("Case #%d: Volunteer cheated!\n",k);
  else
    printf("Case #%d: %d\n",k,card);
    
}

void parse_numbers(string s, int num[], int len){
    string d = " ";
    int n = 0;
    string t = "";
    size_t pos = 0;
    while ( ((pos = s.find(d)) != string::npos) && n < len) {
        t = s.substr(0, pos);
        if (!t.empty())
          num[n++] = atoi(t.c_str());
        s.erase(0, pos + d.length());
      }
      if (n < len) {
        t = s.substr(0, pos);
        if (!t.empty())
          num[n++] = atoi(t.c_str());
      }
}

void file_getline(ifstream& infile){
    string s="";    

    int arr1[4][4];
    int arr2[4][4];
    int a1, a2;
    
    getline(infile,s);
    int n = atoi(s.c_str());
    
    // iterate cases
    for (int k = 1; k <= n; k++)
    {
      // answer 1
      getline(infile,s);
      a1 = atoi(s.c_str());
      
      // get arrangement
      getline(infile,s);
      parse_numbers(s, arr1[0], 4);
      
            getline(infile,s);
      parse_numbers(s, arr1[1], 4);
      
            getline(infile,s);
      parse_numbers(s, arr1[2], 4);
      
            getline(infile,s);
      parse_numbers(s, arr1[3], 4);
      
            // answer 2
      getline(infile,s);
      a2 = atoi(s.c_str());
      
      // get arrangement
      getline(infile,s);
      parse_numbers(s, arr2[0], 4);
      
            getline(infile,s);
      parse_numbers(s, arr2[1], 4);
      
            getline(infile,s);
      parse_numbers(s, arr2[2], 4);
      
            getline(infile,s);
      parse_numbers(s, arr2[3], 4);
      
      solve(k, arr1, arr2, a1, a2);
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

