#include<stdio.h>
#include<iostream>
#include<string>
#include<algorithm>
#include<map>
#include<fstream>
#include<vector>
#define ll long long
#define pb push_back
#define mp make_pair
using namespace std;

int main(){

	ifstream fin;
	ofstream fout;
	fin.open("in.txt");
	fout.open("out.txt");
	int t;
	fin >> t;
	int x,r,c;
	for(int k =1 ; k <= t ; k++){
		fin >> x >> r >> c;
		if((r*c)%x != 0 || r*c < x){
			fout << "Case #" << k << ": RICHARD" << endl;	
			continue;	
		}
		else if(r ==1 || c==1){
			if(x > 2){
				fout << "Case #" << k << ": RICHARD" << endl;	
				continue;
			}
			else{
				fout << "Case #" << k << ": GABRIEL" << endl;	
				continue;
			}
		}	
		else if(r==2 || c==2){
			if(x == 3){
				if(r ==2 && c==2){
					fout << "Case #" << k << ": RICHARD" << endl;	
					continue;
				}	
				else{
					fout << "Case #" << k << ": GABRIEL" << endl;	
					continue;
				}
								
			}
			else if(x == 4){
				if(r ==2 && c==2){
					fout << "Case #" << k << ": RICHARD" << endl;	
					continue;
				}
				else if((r ==2 && c ==4 ) || (r == 4 && c == 2)){
					fout << "Case #" << k << ": RICHARD" << endl;	
					continue;
				}	
				else{
					fout << "Case #" << k << ": GABRIEL" << endl;	
					continue;
				}
			}
			else{
				fout << "Case #" << k << ": GABRIEL" << endl;	
				continue;
			}		
		}
		else{
			fout << "Case #" << k << ": GABRIEL" << endl;	
			continue;
		}
	}
	
return 0;
}
