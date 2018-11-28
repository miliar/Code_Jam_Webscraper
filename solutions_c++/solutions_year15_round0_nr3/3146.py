#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
using namespace std;

int get(int i,int j){
	int signi=1, signj=1;
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
	int a[4][4]={
		{1    ,  'i'   ,   'j'  ,   'k'},
		{'i'  ,  -1    ,   'k'  ,   -1*'j'},
		{'j'  , -1*'k' ,   -1  ,   'i'},
		{'k'  ,  'j'   ,   -1*'i'  ,   -1},
	};
	return a[i][j]*signi*signj;
}
void add(vector<int>& v, string line){
		for(int i=0; i<line.size(); i++){
			v.push_back(line[i]);
		}
}
void print(vector<int > v){
	for(int i=0; i<v.size(); i++){
		cout << v[i] << "  ";
	}
	cout << endl;
}
bool check(vector<int> v){
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
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	//ofstream f("in2.txt");

	int t, ta;
	fin >> t;
//	f << t << endl;
	for(int c=1; c<=t; c++){
		int l, x;
		fin >> l >> x;
	//	f << l << " " << x << endl;
	 	string line, waste;
		fin >> line;
		//f << line << endl;
		getline(fin,waste);


		vector<int > current;
		add(current, line);
		x--;
		int cword='i';
//		cout << line <<endl;
		for(int i=0; i<current.size(); i++){
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

				int temp=get(current[i], current[i+1]);
				current.erase(i+current.begin());
				current.erase(i+current.begin());
				current.insert(i+current.begin(), temp);
				i--;
			}

		}
		//cout << c <<endl;
		//print(current);
		if(check(current)){
			fout << "Case #" << c << ": Yes" << endl;
		}
		else{
			fout << "Case #" << c << ": No" << endl;
		}

		
	}
	system("pause");
}
