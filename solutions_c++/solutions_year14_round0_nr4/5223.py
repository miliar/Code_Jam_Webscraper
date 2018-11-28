#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <cstdlib>
#include <string>
#include <memory.h>
#include <fstream>
using namespace std;

double naomi[1001];
double ken[1001];
//char filename[] = "D:\\Users\\lenovo\\Desktop\\test.txt";
//ofstream fout(filename,ios::app);
int main(){
	ofstream out("D:\\Users\\lenovo\\Desktop\\test.txt");
	ifstream in("D:\\Users\\lenovo\\Desktop\\D-large.in");
	cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());
	int T;
	cin>>T;
	for(int i=1;i<=T;i++){
		int N;
		cin>>N;
		for(int j=0;j<N;j++){
			cin>>naomi[j];
		}
		for(int j=0;j<N;j++){
			cin>>ken[j];
		}
		sort(naomi,naomi+N);
		sort(ken,ken+N);
		int nl=0,kl=0;
		int nr=N-1,kr=N-1;
		//
		int result1=0;
		for(int j=0;j<N;j++){
			if(ken[kl]<naomi[nl]){
				kl++;
				nr--;
			}else{
				nl++;
				kl++;
				result1++;
			}
		}
		//
		nl=0,kl=0;
		nr=N-1,kr=N-1;
		int result2=0;
		for(int j=0;j<N;j++){
			if(naomi[nl]<ken[kl]){
				nl++;
				kr--;
			}else{
				nl++;
				kl++;
				result2++;
			}
		}
		cout<<"Case #"<<i<<": ";
		//fout<<"Case #"<<i<<": ";
		cout<<result2<<" "<<N-result1<<endl;
		//fout<<result2<<" "<<N-result1<<endl;
	}
	return 0;
}