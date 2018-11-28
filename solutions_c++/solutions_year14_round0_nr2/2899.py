#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main() {
	fstream fin("B-large.in");
	fstream fout("out.txt");

	int n;
    double i;
    double C, F, X;
    double time, nextTime;
    double speed;
    fin >> n;

    for(int in = 0; in < n; in++){
      speed = 2;
      i = 1;
      fin >> C >> F >> X;


      time = X/speed + 1;
      nextTime = time - 1;

      while(time > nextTime){
    	  time = nextTime;
    	  nextTime = 0;
    	  for(int j = 0; j < i; j++){
    		  nextTime += C/(speed + j*F);
    	  }
    	  nextTime += X/(speed + i*F);
    	  i++;
      }
      fout << "Case #" << in + 1 << ": "
    		  << fixed
    		  << setprecision(7)
    		  << time << endl;


    }
	return 0;
}
