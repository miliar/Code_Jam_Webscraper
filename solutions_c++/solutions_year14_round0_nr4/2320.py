#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <map>
#include <fstream>
#include <unordered_map>
#include <cstring>

using namespace std;

main (int argc, char const *argv[])
{

  ifstream fin;
  fin.open("D-large.in", ios_base::in);
  
  FILE *fout = fopen("gimmesomeoutput.out", "w");
  
  int t, T;
  fin>>T;
  for(t=0;t<T;t++){
  
    int n;
    fin>>n;
    
    vector<double> d1(n);
    vector<double> d2(n);
    
    for(int i=0;i<n;i++) fin>>d1[i];
    for(int i=0;i<n;i++) fin>>d2[i];
   
    sort(d1.begin(), d1.end());
    sort(d2.begin(), d2.end());
    
    int totalWAR = 0;
    
    int leftKen = 0;
    int rightKen = n-1;
    for(int i = n-1; i>=0; i--){
    
      if(d1[i] > d2[rightKen]){
	leftKen++;
	totalWAR++;
      }
      else{
      
	rightKen--;
	
      }
      
    
    }
    
    int totalDWAR = 0;
    
    int leftNaomi = 0;
    leftKen = 0;
    
    while(leftNaomi<n){
    
      while(leftNaomi<n && d1[leftNaomi]<d2[leftKen]){
      
	leftNaomi++;
      
      }
      
      if(leftNaomi<n){
      
	leftNaomi++;
	leftKen++;
        totalDWAR++;
      
      }
    
    
    }
    
    fprintf(fout, "Case #%d: %d %d\n", t+1, totalDWAR, totalWAR);
    
    
 
  }
  
  fin.close();
     
  fclose(fout);

  return 0;
}