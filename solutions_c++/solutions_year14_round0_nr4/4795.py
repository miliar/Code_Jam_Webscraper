#include<iostream>
#include<string>
#include<fstream>
#include<iomanip>
#include<algorithm>
using namespace std;
ofstream fout("out.txt");
double naomi[1001];
double ken[1001];
int n;
int war(){
	//sort(naomi,naomi+n);
	//sort(ken,ken+n);
	int i=0,j=0;
	int count = 0;
	for(i=0;i<n;i++){
		for(;j<n;j++){
			if(ken[j]>naomi[i]){
				count++;
				j++;
				break;
			}
		}
	}
	return n-count;
}

int decite_war(){
	
	/*
	for(int i=0;i<n/2;i++){
		double t = ken[i];
		ken[i] = ken[n-1-i];
		ken[n-1-i] = t;
	}
	*/
	int ma = 0;
	for(int i=0;i<n;i++){
		int cnt = 0;
		for(int j=0;j<n;j++){
			if(naomi[j]>ken[(i+j)%n])
				cnt++;
		}
		ma = max(cnt,ma);
	}
	return ma;
}
int main(){
	int caseNum;
	cin>>caseNum;
	for(int ll=1;ll<=caseNum;ll++){
		cin>>n;
		for(int i=0;i<n;i++){
			cin>>naomi[i];
		}
		for(int i=0;i<n;i++){
			cin>>ken[i];
		}
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		fout<<"Case #"<<ll<<": "<<decite_war()<<" "<<war()<<endl;
	}
}