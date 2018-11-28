#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<fstream>
#include<vector>
#include<list>
#include<algorithm>
#include<cmath>
#include<string>
#include<limits.h>
#define pb push_back
#define mp make_pair

#define ll long long 
using namespace std;


//=================================================================================//
int arr[1000];
int main(){
	ifstream fin;
	ofstream fout;
	fin.open("in.txt");
	fout.open("out.txt");
	
	int t,N ;
	int c1, c2;
	int rate;
	fin >> t;
	for(int k =1 ; k<= t ; k++){
		fin >> N;
		c1 = 0 , c2 = 0;
		rate = INT_MIN;
		for(int i = 0 ; i< N ; i++){
			fin >> arr[i];
		}
		for(int  i = 1 ; i< N ; i++){
			if(arr[i-1] > arr[i]){
				c1 += (arr[i-1] - arr[i]);
				rate = max(rate, (arr[i-1] - arr[i]));
			}
		}
		if(rate != INT_MIN){
			for(int i = 0 ; i< N-1 ; i++){
				if( (rate) > arr[i]){
					c2 += arr[i];
				}
				else{
					c2 += (rate);
				}
			}
		}
		fout << "Case #"<<k<<": " << c1<<" " <<c2<<endl;
	}
	
	fout.close();
	fin.close();
return 0;
}
