#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;

long long get(long long i,long long j){
	long long signi=1, signj=1;
	if(i<0){
		signi=-1;
		i*=-1;
	}
    if(j<0){
		signj=-1;
		j*=-1;
	}
	
	
	if(i>1){
		i -= 'i';
		i++;
	}
	else
	i--;
	
	if(j>1){
		j -= 'i' ;
		j++;
	}
	else
	j--;
	
//	cout << i << j << endl;
	long long a[4][4]={
		{1    ,  'i'   ,   'j'  ,   'k'},
		{'i'  ,  -1    ,   'k'  ,   -1*'j'},
		{'j'  , -1*'k' ,   -1  ,   'i'},
		{'k'  ,  'j'   ,   -1*'i'  ,   -1},
	};
	return a[i][j]*signi*signj;
}
void add(vector<long long>& v, string line){
		for(long long i=0; i<line.size(); i++){
			v.push_back(line[i]);
		}
}
void print (vector<long long > v){
	for(long long i=0; i<v.size(); i++){
		cout << v[i] << "  ";
	}
	cout << endl;
}
bool check(vector<long long>& v){
	if(v.size() <= 4 && v[0] == 'i' &&v[1] == 'j'  &&v[2] == 'k' ){
		if(v.size() ==4 ){
			if( v[3] == 1){
				return true;
			}
			return false;
		}
		return true;
	}
	return false;
}
main(){
	ifstream fin("C-small-attempt0.in");
	ofstream fout("output.txt");
	//ofstream f("in2.txt");

	long long t, ta;
	fin >> t;
	//f << t << endl;
	for(long long c=1; c<=t; c++){

		long long l, x;
		fin >> l >> x;
		//f << l << " " << x << endl;
	 	string line, waste;
		fin >> line;
		//f << line << endl;
		getline(fin,waste);


		vector< long long > current;
		add(current, line);
		x--;
		long long cword='i';
//		cout << line <<endl;
		for(long long i=0; i<current.size(); i++){

		//	reduce(current);
			if(current.size() <= i+1){
				if(x>0){
					add(current, line);
					x--;
				}
			}
			
			if(current[i] == cword){
				cword++;
			}
		 	else if(current.size() > i+1){

				long long temp=get(current[i], current[i+1]);
				current.erase(i+current.begin());
				current.erase(i+current.begin());
				current.insert(i+current.begin(), temp);
				i--;
			}

		}
		//cout << c <<endl;
		//prlong long(current);
		if(check(current)){
			fout << "Case #" << c << ": Yes" << endl;
		}
		else{
			fout << "Case #" << c << ": No" << endl;
		}

		
	}
//	system("pause");
}
