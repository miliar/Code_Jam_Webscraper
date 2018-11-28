#include <iostream>
#include <fstream>
#include <string>
#include <queue>
using namespace std;

int flip (int x, int p, int max){
	if (p <= max){
		int ans = x;
		for (int i=1 ; i<= p/2+1 ; i++){
			int check1 = x&(1<<(max-(p-i+1)));
			int digit1;
			if (check1 == 0){
				digit1 = 1;
			}
			else {
				digit1 =0;
			}
			int check2 = x&(1<<(max-i));
			int digit2;
			if (check2 == 0){
				digit2= 1;
			}
			else {
				digit2= 0;
			}
			ans ^= (-digit1 ^ ans)&(1<<(max-i));
			ans ^= (-digit2^ans)&(1 <<max-(p-i+1));
		}
		return ans;
	}
}



int main () {

  ifstream myfile ("B-small-attempt0.in");
  ofstream ofile ("ofile.txt");
  int t;
  myfile >> t;
  string line;
  getline(myfile,line);
  for (int z=1; z<=t ; z++){
  	  
      getline (myfile,line);
      int start = 0;
      int max =0;
      for (string::iterator it = line.begin(); it!=line.end(); ++it){
      	max ++;
		start = 2*start;
      	if (*it == '+'){
      		start ++;
		  }
	  }
	  queue<int> Q;
	  Q.push(start);
	  vector<int> dist(2<<max,0);
	  while (!Q.empty()){
		int u = Q.front();
		Q.pop();
		if (u == (1<<max)-1){
			ofile << "Case #" << z << ": " << dist[u] << endl;
			break;
		}
		else {
		for (int i=1; i<=max; i++){
			int v = flip(u, i, max);
			if (!dist[v]){
				dist[v] = dist[u] +1;
				Q.push(v);
			}
			
		}
			
		}			
	}
	}
}
