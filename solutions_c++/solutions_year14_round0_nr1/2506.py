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
  fin.open("A-small-attempt0.in", ios_base::in);
      ofstream fout;

    fout.open("asmall.txt",ios_base::out);
    
  int t, T;
  fin>>T;
  
  for(t=0;t<T;t++){
  
    int data[4][4];
    
    int row;
    fin>>row;
    int i,j;
    for(i=0;i<4;i++){
      for(j=0;j<4;j++){
	fin>>data[i][j];
      }
    }
    
    int cnt[16] = {0};
    
    for(i=0;i<4;i++){
    
      cnt[data[row-1][i]-1]++;
    
    }
    
    fin>>row;
    for(i=0;i<4;i++){
      for(j=0;j<4;j++){
	fin>>data[i][j];
      }
    }
    
    
    for(i=0;i<4;i++){
    
      cnt[data[row-1][i]-1]++;
    
    }
    
    int cnt1 = 0;
    int cnt2 = 0;
    int in = -1;
    for(int i = 0; i<16; i++){
      if(cnt[i]==1) cnt1++;
      else if(cnt[i]==2){
	cnt2++;
	in=i;
      }
    
    }
    fout<<"Case #"<<t+1<<": ";
    if(cnt1==6 && cnt2==1) fout<<in+1<<endl;
    else if(cnt1==8 && cnt2==0) fout<<"Volunteer cheated!"<<endl;
    else fout<<"Bad magician!"<<endl;
  
  }
  
  
  
  
  fin.close();
  
    
  fout.close();



  return 0;
}