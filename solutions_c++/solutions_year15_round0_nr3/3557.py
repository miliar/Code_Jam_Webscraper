#include <iostream>
#include <fstream>
using namespace std;

ifstream reader("C:\\Personal\\Programming Contests\\GCJ-2015\\Qualification\\C\\input.txt");
ofstream writer("C:\\Personal\\Programming Contests\\GCJ-2015\\Qualification\\C\\Soutput.txt");


	int solve_it(int a, int b){
		//49-105-106-107
		if(a == 49)
			return b;
		if(a == -49)
			return b*-1;
		if(a == 105)
		{
			if(b == 49) return a;
			if(b == -49) return -1*a;
			if(b == 105) return -49;
			if(b == -105) return 49;
			if(b == 106) return 107;
			if(b == -106) return -107;
			if(b == 107) return -106;
			if(b == -107) return 106;
		}
		if(a == -105)
		{
			if(b == -49) return a;
			if(b == 49) return -1*a;
			if(b == -105) return -49;
			if(b == 105) return 49;
			if(b == -106) return 107;
			if(b == 106) return -107;
			if(b == -107) return -106;
			if(b == 107) return 106;
		}
		if(a == 106)
		{
			if(b == 49) return a;
			if(b == -49) return -1*a;
			if(b == 105) return -107;
			if(b == -105) return 107;
			if(b == 106) return -49;
			if(b == -106) return 49;
			if(b == 107) return 105;
			if(b == -107) return -105;
		}
		if(a == -106)
		{
			if(b == -49) return a;
			if(b == 49) return -1*a;
			if(b == -105) return -107;
			if(b == 105) return 107;
			if(b == -106) return -49;
			if(b == 106) return 49;
			if(b == -107) return 105;
			if(b == 107) return -105;
		}
		if(a == 107)
		{
			if(b == 49) return a;
			if(b == -49) return -1*a;
			if(b == 105) return 106;
			if(b == -105) return -106;
			if(b == 106) return -105;
			if(b == -106) return 105;
			if(b == 107) return -49;
			if(b == -107) return 49;
		}
		if(a == -107)
		{
			if(b == -49) return a;
			if(b == 49) return -1*a;
			if(b == -105) return 106;
			if(b == 105) return -106;
			if(b == -106) return -105;
			if(b == 106) return 105;
			if(b == -107) return -49;
			if(b == 107) return 49;
		}
	}

	bool doit(){
		int X, L;
		reader >> L >> X;
		string s;
		reader >> s;
		int curr = static_cast<int>(s[0]);
		int found_state = 0; //0: nothin, 1: i, 2:j, 3:k
		//cout << curr << " ";
		for(int i = 1; i < X*L; i++){
			if((found_state == 0 && curr == 105) ||
			   (found_state == 1 && curr == 106) ||
			   (found_state == 2 && curr == 107)) {
				curr = static_cast<int>(s[i%L]);
				found_state++;
				continue;
			}
			curr = solve_it(curr, static_cast<int>(s[i%L]));
			//cout << curr << " ";
		}
		//cout << endl;
		if((found_state == 2 && curr == 107) ||
	       (found_state == 3 && curr == 49))
	       return true;
	    else return false;
	}

	int main() {
		int T;
		reader >> T;
		for(int i = 1; i <= T; i++){
			bool ans = doit();
			writer << "Case #" << i << ": ";
			if(ans) writer << "YES" << endl;
			else writer << "NO" << endl;
		}
	}
