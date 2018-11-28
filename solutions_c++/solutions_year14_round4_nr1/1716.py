#include <iostream>
#include <fstream>
#include <set>

using namespace std;

multiset<int> Q;

int main()
{
	int n,N;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	
	fin>>N;

	for(n=0;n<N;n++){
		int num,ss;
		int temp;
		Q.clear();
		int i;
		fin>>num>>ss;
		for(i=0;i<num;i++){
			fin>>temp;
			Q.insert(temp);
		}
		multiset<int>::iterator pos,pp;
		int count=0;
		while(!Q.empty()){
			count++;
			if(Q.size() == 1)
				break;
			pp = pos = Q.begin();
			temp = ss - (*pos);
			for(++pp;pp!=Q.end();pp++)
				if(*pp > temp) break;
			pp--;
			if(pp != Q.begin()){
				Q.erase(pp);
				Q.erase(pos);
			}			
			else
				Q.erase(pos);
		}

		
		fout<<"Case #"<<n+1<<": "<<count<<endl;
	}


	return 0;
}


//fout.setf(ios::fixed);
//fout.precision(6);