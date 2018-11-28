#include <iostream>
#include <fstream>
#include <set>
#include <algorithm>

using namespace std;

multiset<int, greater<int> > Q;
multiset<int, greater<int> > P;

int main()
{
	int n,N;
	ifstream fin("B-small-attempt8.in");
	//ifstream fin("input.txt");
	ofstream fout("output.txt");
	
	fin>>N;

	for(n=0;n<N;n++){
		int d,t;
		Q.clear();
		fin>>d;

		for(int i=0;i<d;i++){
			fin>>t;
			Q.insert(t);
		}
		P = Q;
		int size = *(Q.begin());
		int min = size;

		for(int i=1;i<=size;i++){
			int temp = *(Q.begin());
			Q.erase(Q.begin());
			Q.insert(temp/2);
			Q.insert(temp - temp/2);
			if(min > *(Q.begin()) + i)
				min = *(Q.begin()) + i;
		}
		Q = P;
		for(int i=1;i<=size;i++){
			int temp = *(Q.begin());
			Q.erase(Q.begin());
			if(temp == 9){
				Q.insert(temp/3);
				Q.insert(temp - temp/3);
			}
			else{
				Q.insert(temp/2);
				Q.insert(temp - temp/2);
			}
			if(min > *(Q.begin()) + i)
				min = *(Q.begin()) + i;
		}


		fout<<"Case #"<<n+1<<": "<<min<<endl;
	}

	return 0;
}
