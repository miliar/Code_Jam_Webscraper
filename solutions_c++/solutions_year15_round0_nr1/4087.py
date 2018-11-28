#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<fstream>
#define ll long long 
using namespace std;
int arr[2000];
string str;
int main(){
	ifstream fin;
	ofstream fout;
	fin.open("in.txt");
	fout.open("out.txt");
	int t,size,ans,carry;
	fin >> t;
	for(int k =1 ; k<= t ; k++){
		str.clear();
		ans = 0;
		carry = 0;
		fout << "Case #" << k << ": ";
		fin >> size >> str;
		arr[0] = str[0] - '0';
		for(int  i =1 ; i< size+1 ; i++){
			arr[i] = arr[i-1] + (str[i] - '0');
		}
		for(int i =0 ; i< size ; i++){
			arr[i] += carry;
			if(arr[i] < i+1){
					ans += (i+1 - arr[i]);
					carry += (i+1 - arr[i]);	
					arr[i] = i+1;
			}
		}
		fout << ans << endl;
	}
	fout.close();
	fin.close();
return 0;
}
