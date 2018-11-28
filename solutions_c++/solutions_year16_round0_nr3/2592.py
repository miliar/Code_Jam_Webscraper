#include "math.h"
#include "iostream"
#include "fstream"
#include "vector"
#include "string"
#include "set"
#include "unordered_set"
#include "stack"
using namespace std;
void primen(vector <int> & primlist){
	//cout<<"start generating prime numbers"<<endl;
	for(int i=2;i<10000;i++){
		int pass=1;
		for(int k=0;k<primlist.size()&&primlist[k]<i;k++){
			if(i%primlist[k]==0){
				pass=0;
				break;
			}
		}
		if(pass==1){
			primlist.push_back(i);
			//cout<<i<<endl;
		}
	}
}


vector <int> nextcj( vector <int> pre, int N){
	vector <int> out;
	out=pre;
	for(int i=N-2;i>0;i--){
		if(pre[i]==0){
			out[i]=1;
			for(int j=i+1;j<N-1;j++){
				out[j]=0;
			}
		break;
		}
	}
	return out;	
}


long long int divi( vector <int> cj, int di, vector <int> primlist){
	long long int tar=0;
	for(int i=0;i<cj.size();i++){
		tar=tar*di+cj[i];
	}
	int pass=0;
	int x=0;
	for(x=0;x<primlist.size();x++){
		if(tar%primlist[x]==0){
			pass=1;
			break;
		}
	}
	if(pass==1){
		return primlist[x];
	}
	else return 0;
}
int main(){
	vector <int> primlist;
	primen(primlist);
	int T;
	ifstream in("inputs.txt");
	ofstream out("outputs.txt");
	T=1;
	int N=16, J=50;
	int ct=0;
	out<<"Case #1:"<<endl;
	cout<<"Case #1:"<<endl;
	vector <int> cj;
	for(int i=0;i<16;i++){
		if(i==0||i==15) cj.push_back(1);
		else cj.push_back(0);
	}
	while(ct<J){
		vector <int> answer;
		int pass=1;
		for( int di=2;di<=10;di++){
			long long int test=divi(cj,di,primlist);
			if(test==0){
				pass=0;
				break;
			}
			else answer.push_back(test);
		}
		if(pass==1){
			for(int y=0;y<16;y++){
				out<<cj[y];
				cout<<cj[y];
			}
			out<<" ";
			cout<<" ";
			for(int di=0;di<=8;di++){
				out<<answer[di]<<" ";
				cout<<answer[di]<<" ";
			}
			out<<endl;
			cout<<endl;
			ct++;
		}
		cj=nextcj(cj,16);	
	}
}
