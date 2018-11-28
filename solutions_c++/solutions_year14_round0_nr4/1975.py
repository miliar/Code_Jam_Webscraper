#include <iostream>
#include <vector>
#include <algorithm>
typedef std::pair<double,int> pdi;
typedef std::vector<pdi> vp;



int main(){

  
  int T;
  int N;
  double tmp;
  std::cin >> T;
  for(int t=1;t<=T;++t){
    std::cin >> N;
    // vd naomi(N,0);
    // vd ken(N,0);
    // for(int i=0;i<N;++i){
      
    //   cin >> naomi[i];
    // for(int i=0;i<N;++i)
    //   cin >> ken[i];
    vp w;
    for(int i=0;i<N;++i){
      std::cin >> tmp;
      w.push_back(pdi(tmp,0));      
    }
    for(int i=0;i<N;++i){
      std::cin >> tmp;
      w.push_back(pdi(tmp,1));      
    }
    std::sort(w.begin(),w.end());
    //std::reverse(w.begin(),w.end());   
    int ken = 0;
    int katie=0;
    for(int i=0;i<2*N;++i){
      if(w[i].second ==0){
	++katie;
      }
      else if(katie >0){
	++ken;
	--katie;
      }
    }
    int honest = N-ken;
    ken = 0;
    katie=0;
    for(int i=0;i<2*N;++i){
      if(w[i].second ==1){
	++ken;
      }
      else if(ken >0){
	--ken;
	++katie;
      }
    }
    
    std::cout << "Case #" << t << ": " << katie << " " << honest << std::endl;
    
  }
  
}


// x x x y y y x y 
// 1 2 3 2 1 0 1 0 
// x y y  y x x  y y y 
// 1 0 -1 -2 -1 0 
// x y y y x x x y 
// 0 1 2 3 3 3 3 3
 
