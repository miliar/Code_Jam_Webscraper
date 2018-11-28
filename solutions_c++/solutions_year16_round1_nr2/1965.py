#include <fstream>
#include<vector>
#include <algorithm>
using namespace std;


int main(){
	int t;
	ifstream in("B-large.in");
	ofstream out("soldier.out"); 
	in >> t;
	for (int tt = 0; tt < t;tt++){
		int n,tmp,max = 0;
		in >> n;
		vector<int> a;
		a.clear();
		int count[2501];
		for (int i = 1; i <= 2500; i++) count[i] = 0;
		for (int i = 0; i < 2*n-1;i++)
			for (int j = 0; j <n;j++){
				in >> tmp;
				count[tmp] ++;
				if (tmp > max) max = tmp;
			}
		for (int i = 1; i <= max;i++)
			if (count[i] %2 == 1) a.push_back(i);
		sort(a.begin(),a.end());
		out << "Case #" << tt+1 << ": ";
		for (int i = 0; i < a.size();i++)
			out << a[i] << ' ';
		out<< endl;			
	}
	in.close();
	out.close();
}
