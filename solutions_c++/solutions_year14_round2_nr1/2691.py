#include <iostream>
#include <fstream>
#include <list>
#include <bitset>
#include <set>
#include <stdio.h>
#include <string.h>
#include <limits.h>

using namespace std;
string* strings = new string[100];
int** strings_simp_count;
int *target_count;
string simplified;

string simplify (int n) {
	string s = strings[n];
	string simplified = "";
	for (int i=0; i<s.length(); i++) {
		if (simplified.length() == 0) {
			simplified += s[i];
			strings_simp_count[n][simplified.length()-1]++;
		} else {
			if (simplified[simplified.length()-1] != s[i]){
				simplified += s[i];
			} 
			strings_simp_count[n][simplified.length()-1]++;
		}
	}
	return simplified;
}

unsigned long long int moves_to_target (int n) {	
	unsigned long long int moves = 0;
	for (int i=0; i<simplified.length(); i++) {
		if (strings_simp_count[n][i] > target_count[i]) moves += (strings_simp_count[n][i]-target_count[i]) ;
		else moves += (target_count[i]-strings_simp_count[n][i]);	
	}
	return moves;
}

int main () {
	
	ifstream in ("A-small-attempt1.in");
	ofstream cout("small.out");
	int T;
	in>>T;
	
	for (int t=0; t<T; t++) {
	
		strings = new string[100];
		simplified = "";
		strings_simp_count = new int*[100];
		cout<<"Case #"<<t+1<<": ";
		
		int N; in>>N;
		
		bool fegla_won = false;
		
		for (int n=0; n<N; n++) {
			string temp; in>>temp;
			strings_simp_count[n]= new int[temp.length()]; memset(strings_simp_count[n], 0, sizeof(strings_simp_count[0][0]) * temp.length());
			strings[n] = temp;
			temp = simplify(n);
			if (n==0) simplified = temp;
			if (temp != simplified) {
				fegla_won = true;
			}
		}
		
		
		if (!fegla_won) {
			target_count = new int[simplified.length()];
			memset(target_count, 0, sizeof(target_count[0]) * simplified.length());
			for (int i=0; i<simplified.length(); i++) {
				for (int n=0; n<N; n++) {
					target_count[i]+=strings_simp_count[n][i];
				}
				target_count[i] = (int)(target_count[i]/N + 0.5);
			}
			
			unsigned long long int min_moves = 0;
			for (int i=0; i<N; i++) {
				min_moves += moves_to_target(i);
				//cout<<"i: "<<i<<", j: "<<j<<" "<<strings[j]<<", t:"<<strings[i]<<" cur:"<<cur<<endl;
			}
			cout<<min_moves<<"\n";
		} else {
			cout<<"Fegla Won\n";
		}
	}
	
	return 0;
}
