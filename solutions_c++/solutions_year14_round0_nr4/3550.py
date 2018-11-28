//#include <simplecpp>
#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int greatestless(double num, double array[], int N){
	int ans=-1; double val=0;
	for (int i=0; i<N; i++) {
		if (array[i]<num) {
			if (array[i]>val) {
				val=array[i];
				ans=i;
			}
		}
	}
	return ans;
}

int main(int argc, char* argv[ ]) {
	int T, N, ntemp, addr, score1=0, score2=0;
	double ken[1000], naomi[1000], ken2[1000], naomi2[1000];
	cin>>T;
	for (int t=1; t<=T; t++) {
		score1=0; score2=0;
		cin>>N;
		for (int n=0; n<N; n++) {cin>>naomi[n]; naomi2[n]=naomi[n];}
		for (int n=0; n<N; n++) {cin>>ken[n]; ken2[n]=ken[n];}
		ntemp=N;
		for (int i=0; i<N; i++) {
			addr=greatestless(naomi[i], ken, ntemp);
			if(addr!=-1){
				score1++;
				ntemp--;
				ken[addr]=ken[ntemp];
			}
		}
		ntemp=N;
		for (int i=0; i<N; i++) {
			addr=greatestless(ken2[i], naomi2, ntemp);
			if(addr!=-1){
				score2++;
				ntemp--;
				naomi2[addr]=naomi2[ntemp];
			}
		}
		cout<<"Case #"<<t<<": "<<score1<<" "<<N-score2<<endl;
	}
}