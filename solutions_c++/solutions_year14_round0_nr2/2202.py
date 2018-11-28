#include <iostream>
#include <vector>
typedef std::vector<int> vi;

int main(){
  std::vector<int> a;
  
  int T;
  double C,F,X;
  std::cin >> T;
  std::cout.precision(8);
  std::cout.setf( std::ios::fixed, std:: ios::floatfield );
  for(int t=1;t<=T;++t){
    std::cin >> C >> F >> X;    
    double pf = 2.0;
    double best= X/pf;
    double time_used =0;
    while(1){
      double time_to_farm = C/pf;
      double time_to_goal = X/pf;
      best = std::min(best,time_used+time_to_goal);
      if(time_used > best){
	std::cout << "Case #" << t << ": " << best << std::endl;
	break;	
      }
      time_used += time_to_farm;
      pf = pf +F;
      //std::cerr << t << " " << time_used << " " << pf << " " << best << std::endl;
    }
    
  }
  return 0;
}
	
  
