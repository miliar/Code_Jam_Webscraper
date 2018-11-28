#include <iostream>
#include <vector>
typedef std::vector<int> vi;

int main(){
  std::vector<int> a;
  
  int T,g1,g2;
  std::cin >> T;
  for(int i=0;i<T;++i){
    std::cout << "Case #" << (i+1) << ": ";
    std::vector<vi > m1(4,vi(4,0));
    std::vector<vi > m2(4,vi(4,0));
    std::cin >> g1;
    g1--;
    for(int a=0;a<4;++a)
      for(int b=0;b<4;++b){
	std::cin >> m1[a][b];
      }
    std::cin >> g2;
    g2--;
    for(int a=0;a<4;++a)
      for(int b=0;b<4;++b){
	std::cin >> m2[a][b];
      }
    std::vector<int> r1 = m1[g1];
    std::vector<int> r2 = m2[g2];
    int count=0;
    int val;
    for(int a=0;a<4;++a)
      for(int b=0;b<4;++b)
	if(r1[a]==r2[b]){
	  ++ count;
	val = r1[a];
	}
    
    if(count == 0){
      std::cout << "Volunteer cheated!" << std::endl;
	
    }
    else if(count == 1){
      std::cout <<  val  << std::endl;
    }
    else{
      std::cout << "Bad magician!" << std::endl;
    }
  }
  return 0;
} 
