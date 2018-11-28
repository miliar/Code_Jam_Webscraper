#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>
#include <iomanip>

using namespace std;

int main()
{
  ifstream fin("B-large.in");
  ofstream fout("B-largeans.out");
  int N;
  fin >> N;
  double cost, farm, goal, cookies=0.0, produce=2.0, tim=0.0, a, b;
  for(int i=0; i<N; i++){
    cookies=0.0000000000, produce=2.000000000, tim=0.000000000;
    fin >> cost >> farm >> goal;
    while(cookies<goal){
      a=goal/produce;
      b=cost/produce+goal/(produce+farm);
      if(a<b){
        tim+=goal/produce;
        cookies=goal;
      }
      else{
        cookies=0;
        tim+=cost/produce;
        produce+=farm;
      }
    }
    fout << "Case #" << i+1 << ": " << setprecision(10) << tim << endl;
  }
}
