#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cmath>
using namespace std;
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int evauluate(int mymote,int *mote,int Size){
	int i=0;
	int opts = 0;
	float k;
	int prevmote;
	int minOpt = Size;
	while(i<Size){
		if(mote[i]>=mymote*2-1){
			minOpt = opts + Size-i;
		}
		if(mymote==1){
			return  opts + Size-i;
		}
		if(mote[i]<mymote){
			mymote+=mote[i];
			i++;
		}
		else{
			k = (float)(mote[i]-1)/(float)(mymote-1);
			k =(log10(k)*3.32);
			if(ceil(k)==k)
				k++;
			else
				k = ceil(k);
			opts +=k;
			prevmote = mymote;
			mymote=pow(2,k)*(mymote-1)+1;					
			if(prevmote == mymote)
				return  opts + Size-i;
			if(opts>minOpt)
				return minOpt;
		}

	}
	return opts;
}
int main(int argc, char *argv[]){

	ifstream in("B-large-practice.in");
	ofstream out("out.txt");
	int  testcases,A,N;
	int i;
	int *mote;
	in >> testcases;
	for(i=0;i<testcases;i++){
		in>>A>>N;
		cout<<i<<endl;
		mote = new int[N];
		for(int j=0;j<N;j++)
			in >> mote[j];
		qsort(mote,N,sizeof(int),compare);
		int opts = evauluate(A,mote,N);
		out<<"Case #"<<i+1<<": "<<opts<<endl;

	}
	return 1;
}