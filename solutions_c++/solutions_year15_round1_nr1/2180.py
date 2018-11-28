#include<iostream>
#include<fstream>

using namespace std;

ifstream fin("input.in");
ofstream fout("output.txt");

void results(int i){
	int N;
	int arr[1002]={0},diff=0,max=-1;
	int m1=0,m2=0;
	fin>>N;
	m1=0;
	m2=0;
	fin>>arr[0];
	for(int j=1;j<N;j++){
		fin>>arr[j];
		diff=arr[j-1]-arr[j];
		if(diff>0)
			m1=m1+diff;
		if(diff>max)
			max=diff;
	}
	for(int j=0;j<N-1;j++){
		if(arr[j]<max)
			m2=m2+arr[j];
		else
			m2=m2+max;
	}
	fout<<"Case #"<<i<<": "<<m1<<" "<<m2<<endl;
}

int main()
{
	int tc;
	fin>>tc;
	for(int i=1;i<=tc;i++){
		results(i);
	}
	return 0;
}