#include <bits/stdc++.h>
#include <vector>
#include <queue>
using namespace std;
long long int myPow(long long int x, long long int p)
{
  if (p == 0) return 1;
  if (p == 1) return x;

  long long int tmp = myPow(x, p/2);
  if (p%2 == 0) return tmp * tmp;
  else return x * tmp * tmp;
}
int main(){
	ifstream fin("test.txt");
	ofstream fout("testrespuesta.txt");
	long int t;
	fin>>t;
	int k,c,s;
	for(long int i=0; i<t; i++){
		fin>>k>>c>>s;
		queue<long long int> cola;
		for(int j=0; j<k; j++){
			cola.push(myPow(k,c-1)*j+1);
		}
		fout<<"Case #"<<i+1<<":";		
		if(cola.size()<=s){
			int longi=cola.size();
		for(int w=0;w<longi;w++){
			fout<<" "<<cola.front();
			cola.pop();
		}
		}else{
			fout<<"IMPOSSIBLE";
		}	
		fout<<"\n";
	}
}
