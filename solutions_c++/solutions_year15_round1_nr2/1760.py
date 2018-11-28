#include <iostream>
#include <fstream>
#include <vector>
#include <set>
using namespace std;

vector<int> Q;
vector<int> P;
int mm,b;

int check(int num){
	__int64 t = num/b;
	if(t == 0)
		return num;
	t = t*mm;
	
	for(int i=0;i<b;i++){
		num -=  t/Q[i];
		if(t%Q[i] != 0){
			P[i] -= t%Q[i];
			if(P[i] < 0){
				num--;
				P[i] = Q[i] + P[i];
			}
		}		
	}
	return check(num);
}

int main()
{
	int n,N;
	ifstream fin("B-small-attempt0.in");
	ofstream fout("output.txt");
	
	fin>>N;

	for(n=0;n<N;n++){
		int num;
		fin>>b>>num;

		Q.clear();
		Q.resize(b);
		P.clear();
		P.resize(b,0);
		mm = 10000000;
		for(int i=0;i<b;i++){
			fin>>Q[i];
			if(Q[i] < mm)
				mm = Q[i];
		}

		num = check(num);
		int pivot;
		if(num == 0){
			int aa = 1000000;
			for(int i=b-1;i>=0;--i){
				if(Q[i]-P[i] < aa){
					aa = Q[i]-P[i];
					pivot = i;
				}
			}
		}
		else{
			multiset<pair<int,int> > T;
			T.clear();
			for(int i=0;i<b;i++){
				T.insert(make_pair(P[i],i));
			}
			
			multiset<pair<int,int> >::iterator pos;
			for(int i=0;i<num;i++){
				pos = T.begin();
				pivot = pos->second;
				T.insert(make_pair(pos->first + Q[pos->second],pos->second));
				T.erase(pos);
			}
		}


		fout<<"Case #"<<n+1<<": "<<pivot+1<<endl;
	}


	return 0;
}


//fout.setf(ios::fixed);
//fout.precision(6);