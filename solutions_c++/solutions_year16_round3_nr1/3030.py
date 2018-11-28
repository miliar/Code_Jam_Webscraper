#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cassert>
#include <cmath>
#include <algorithm>
//#include <vector>
using namespace std;

int T,N;

ofstream out("output.txt");

/*int cmp(void const *a, void const *b)
{
	struct struttura first= *(struct pippo *)a;
	struct struttura second= *(struct pippo *)b;
	if(first.num>second.num)
	return 1;
	if(first.num<second.num)
	return -1;
	return 0;
}*/



struct a{
	int indice;
	int num;
};

bool acompare(a lhs, a rhs) { return lhs.num < rhs.num; }

void risolvi(struct a v[],int N) {
	sort(v, v+N, acompare);
	/*int conta;
	for(int i=N-1;i>=0;i--){
		int j=i-1;
		sort(v, v+N, acompare);
		while(v[j].num<v[i].num){
			conta=1;
			for(int k=N-1;k>j;k--){
				
				char c=v[k].indice+65;
				out<<c;
				v[k].num--;
				if(conta%2==0)
					out<<" ";
				conta++;
			}
			if(conta%2==0)
				out<<" ";
		}
		if(conta%2==0)
			out<<" ";
		conta=1;
		for(int k=N-1;k>j;k--){
				
			char c=v[k].indice+65;
			out<<c;
			v[k].num--;
			if(conta%2==0)
				out<<" ";
			conta++;
		}
	}*/
	bool flag=true;
	char c;
	int conta=0;
	while(flag) {
		flag=false;
		for(int i=N-1;i>=0;i--) {
			if(v[i].num>1){
				v[i].num--;
				c=v[i].indice+65;
				out<<c;
				if(conta%2!=0)
					out<<" ";
				flag=true;
				conta++;
			}
		}
	}
	if(N%2!=0) {
		c=v[N-1].indice+65;
		out<<c;
		out<<" ";
		conta=0;
		for(int i=N-2;i>=0;i--) {
			c=v[i].indice+65;
			out<<c;
			if(conta%2!=0)
				out<<" ";
			conta++;
		}
	}
	
	else {
		conta=0;
		for(int i=N-1;i>=0;i--) {
			c=v[i].indice+65;
			out<<c;
			if(conta%2!=0)
				out<<" ";
			conta++;
		}
	}
	out<<endl;
}

int main()
{
	struct a v[30];
	ifstream in("input.txt");
	assert(in);
	
	in>>T;
	for (int i=0;i<T;i++) {
		in>>N;
		for(int j=0;j<N;j++){
			in>>v[j].num;
			v[j].indice=j;
		}
		out<<"Case #"<<i+1<<": ";
		risolvi(v,N);
	}
	/*for(int j=0;j<N;j++)
		cout<<v[j].indice<<":"<<v[j].num<<endl;*/

	/*cout<<endl<<endl;
	for(int j=0;j<N;j++)
		cout<<v[j].indice<<":"<<v[j].num<<endl;*/
	cout<<endl<<endl;
	system("PAUSE");
	return 0;
}
