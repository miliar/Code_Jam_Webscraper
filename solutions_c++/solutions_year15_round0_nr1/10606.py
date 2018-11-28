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
#include <cstring>
#include <fstream>
#include <queue>

using namespace std;

int main(void){
	
	ifstream fin;
	ofstream fout;
	fin.open("in.txt", ios_base::in);
	fout.open("out.txt", ios_base::out);
	
	int t, T;
	fin>>T;
	for(t=0;t<T;t++){
		
		string shypeople;
		int smax;
		fin>>smax>>shypeople;
		
		int i;
		int curstanding = shypeople[0] - '0';
		int bring = 0;
		for(i=1;i<smax+1;i++){
			
			if(curstanding >= i){
				curstanding += (shypeople[i] - '0');
 			}
			else if (shypeople[i]!='0'){ 
				
				bring += i - curstanding;
				curstanding += bring + shypeople[i]-'0';
				
			}
		}
		
		fout<<"Case #"<<t+1<<": "<<bring<<endl;
	}

}