#include <fstream>
#include <algorithm>
#include <stack>
#include <queue>
#include <cmath>
#include <stdlib.h>
using namespace std;

int main(){
	ifstream fin;
	ofstream fout;

	fin.open("A-large.in");
	fout.open("Alargeoutput.txt");

	int T;
	fin >> T;
	for(int t=1 ; t<=T ; t++){
		int A, N ,ans, a;
		fin>> A >> N;
		a= A;
		int *mote = new int [N];
		int *add = new int [N];
		int *del = new int [N];
		for(int i=0 ;i <N ; i++){
			fin >> mote[i];
			add[i] = 0;
		}
		sort(mote, mote+N);

		del[0] = N;
		ans = N;
		
		while(A <=mote[0]){
			if(a==1){break;}
			A+=A-1;
			add[0]++;
		}
		A+=mote[0];
		for(int i=1 ; i<N ; i++){
			del[i] = N-i+ add[i-1];
			if(del[i]<ans) ans = del[i] ;
			add[i] = add[i-1];
			while(A <= mote[i]){
				if(a==1){break;}
				A+=A-1;
				add[i]++;
			}
			A+=mote[i];
		}
		if(add[N-1]<ans) ans = add[N-1];
		if(a==1){ans = N;}
		fout << "Case #" << t << ": " << ans << endl;
	}
	fin.close();
	fout.close();
}