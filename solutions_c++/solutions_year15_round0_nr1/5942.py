#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#define forn(i,n) for(int i=0;i<(int)n;i++)
#define fora(i,a,b) for(int i=a;i<(int)b;i++)
#define p(p) cout<<p<<"\n";
using namespace std;
int main(){
	long int t,curr,sum,need,max,need_curr;
	string in;
	ifstream fin;
	fin.open("large.in");
	ofstream fout;
	fout.open("output.txt");
	fin>>t;
	forn(it,t){
		fin>>max;
		fin>>in;
		sum=0;
		need=0;

		forn(i,in.length()){
			curr = int(in[i])-48;
			if(i==0){
				sum+=curr;
			}
			else{
				if(sum<i){
					need_curr = i-sum;
					need+=need_curr;
					sum+=need_curr;
				}
				sum+=curr;
			}
		}
		if(it==0){
			fout<<"Case #"<<it+1<<": "<<need;
		}
		else{
			fout<<endl<<"Case #"<<it+1<<": "<<need;
		}
	}
}