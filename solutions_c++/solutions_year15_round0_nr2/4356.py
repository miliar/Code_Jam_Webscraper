#include<iostream>
#include<fstream>
#include<queue>
#include<algorithm>

using namespace std;

long D,ms;



void solve(int* ary,int mins,long s){
	/*
	cout << mins << " " << s << endl;
	cout << "ary : ";
	for(long i=0;i<s;i++){
		cout << ary[i] << " ";
	}
	cout << endl;
	*/
	
	//check if done
	bool isDone = true;
	for(long i=0;i<s;i++){
		if(ary[i] != 0){
			isDone = false;
			break;
		}
	}
	
	if(isDone){
	 	if (mins < ms){
			ms = mins;
		}
		return;
	}
	if(mins > ms){
		return;
	}
	
	//try eating
	int* tmp = new int[s];
	for(long i=0;i<s;i++){
		if(ary[i] > 0)
			tmp[i] = ary[i] - 1;
	}
	solve(tmp,mins+1,s);
	
	//try division
	//cout << "division " << endl;
	sort(ary,ary+s);
	int p = ary[s-1];
	//cout << "max " << p << endl;
	if(p > 1){
		for(int j=1;j<=p/2;j++){
			int p2 = j;
			int p3 = p - p2;
		
			tmp = new int[s+1];
			for(long i=0;i<s-1;i++){
				tmp[i] = ary[i];
			}
			tmp[s-1] = p2;
			tmp[s] = p3;
			solve(tmp,mins+1,s+1);			
		}
		
		/*
		int p2 = p/2;
		int p3 = p - p2;
		
		tmp = new int[s+1];
		for(long i=0;i<s-1;i++){
			tmp[i] = ary[i];
		}
		tmp[s-1] = p2;
		tmp[s] = p3;
		solve(tmp,mins+1,s+1);
		*/
	}
}


int main(){	
	
	ifstream fin("daa.in");
	ofstream fout("data.out");
	
	int T;
	
	fin >> T;
	
	for(int t=0;t<T;t++){
		D = 0;
		ms = 0;
		fin >> D;
		int* ds = new int[D];
		
		for(long i=0;i<D;i++){
			fin >> ds[i];
			if(ds[i] > ms){
				ms = ds[i];
			}
		} 
		
		
		long n =0;
		
		solve(ds,n,D);		
	
		//cout << ms << endl;
		fout << "Case #" << t+1 << ": " << ms << endl;
	}
		
	fin.close();
	fout.close();
}

