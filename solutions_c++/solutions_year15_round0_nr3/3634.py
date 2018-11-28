/*
Name = Noman
*/


#include <stdlib.h>
#include <iostream>
#include <vector>
#include <fstream>


using namespace std;

long long compute
(long long i,long long j){
	long long S1=1, S2=1;
	if(i<0){
		S1=-1;
		i*=-1;
	}
    if(j<0){
		S2=-1;
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
	

	long long arr[4][4]={{1,'i','j','k'},{'i',-1,'k',-1*'j'},{'j',-1*'k' ,-1,'i'},{'k','j',-1*'i',-1},};
			
return arr[i][j]*S1*S2;
}
void insert
(vector<long long>& z, string inp){
		for(long long i=0; i<inp.size(); i++){
			z.push_back(inp[i]);
		}
}

bool chk(vector<long long>& z){
	if(z.size() <= 4 && z[0] == 'i' &&z[1] == 'j'  &&z[2] == 'k' ){
		if(z.size() ==4 ){
			if( z[3] == 1){
				return true;
			}
			return false;
		}
		return true;
	}
	return false;
}
int main(){
			ifstream fin("C-small-attempt1.in");
	
			ofstream fout("output.txt");
			ofstream f("in2.txt");

	long long cases, rep;
	fin >> cases;
	f << cases << endl;
	for(long long c=1; c<=cases; c++){

		long long Smax, rep;
		fin >> Smax >> rep;
		f << Smax << " " << rep << endl;
	 	string inp, waste;
		fin >> inp;
		f << inp << endl;
		getline(fin,waste);


		vector< long long > current;
		insert(current, inp);
		rep--;
		long long cw='i';

		for(long long i=0; i<current.size(); i++){


			if(current.size() <= i+1){
				if(rep>0){
					insert(current, inp);
					rep--;
				}
			}
			
			if(current[i] == cw){
				cw++;
			}
		 	else if(current.size() > i+1){
				long long temp=compute(current[i], current[i+1]);
				current.erase(i+current.begin());
				current.erase(i+current.begin());
				current.insert(i+current.begin(), temp);
				i--;
			}

		}
		
		if(chk(current)){
			fout << "Case #" << c << ": YES" << endl;
		}
		else{
			fout << "Case #" << c << ": NO" << endl;
		}}
	system("pause");
	return 0;
}
