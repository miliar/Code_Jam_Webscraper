#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

long long data[1000000]; long long total;
long long str[3500];

void FunctoString(long long x){
	long long y;
	total=0;
	while(x>0){
		y = x % 10;
		//fout<<"y : "<<y<<" total : "<<total<<endl;
		x = x / 10;
		str[total] = y;
		total++;
	}
}

bool palindrom(){
	int i=0;
	bool p = true;
	i = 0;
	while(i<=total/2 && p){
		//fout<<str[i]<<" "<<str[total-1-i]<<endl;
		if(str[i] != str[total-1-i]) p = false;
		i++;
	}
	return p;
}

void generate(){
	for(int i=1; i<=1000000; i++){
		data[i] = 0;
	}
	for(int i=1; i<=1000; i++){
		data[i*i] = i;
	}
}

bool kuadrat(long long x){
	bool found = false;
	if(data[x] != 0){
		found = true;
		//fout<<"kuadrat : "<<data[x]<<endl;
	}
	else
	return found;
}

int main(){
	int N;
	long long A, B, count;
	ifstream fin ("C-small-attempt0.in");
	ofstream fout ("output.out");
	generate();
	//FunctoString(101);
	//fout<<palindrom();
	fin>>N;
	for(int j=1; j<=N; j++){
		fin>>A>>B;
		count = 0;
		total = 0;
		fout<<"Case #"<<j<<": ";
		for(long long i = A; i<=B; i++){
			//fout<<i<<endl;
			FunctoString(i);
			if(palindrom() && kuadrat(i)){
				FunctoString(data[i]);
				if(palindrom()){
					count++;
					//fout<<"palindrom : "<<i<<endl;
				}
			}
		}
		fout<<count<<endl;
	}
	
	return 0;
}