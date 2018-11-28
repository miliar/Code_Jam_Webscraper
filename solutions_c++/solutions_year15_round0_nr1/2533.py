#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main(){
	int case;
	int smax;
	string si;
	int aud;
	int fri;
	cin>>case;
	for(int i=1;i<=case;i++){
		cin>>smax;
		cin>>si;
		aud=0,fri=0;
		for(int s=0;s<=smax;s++){
			