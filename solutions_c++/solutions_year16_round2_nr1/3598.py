#include <iostream>
#include <string>
using namespace std;

string s;
int arr[26];
int num[10];

int met(char c){
		char yy = c;
		int uu = yy-'0';
		uu -= 17;
		
		return uu;
}

int mymet(string s1,int gh){
	for(int i=0;i<s1.length();i++){
		int yyy = met(s1.at(i));
		
		arr[yyy] -= gh;
	}
}

int main() {
	// your code goes here
	int t;
	cin >> t;
	string ss[10] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
	for(int k1=1;k1<=t;k1++){
		cin >> s;
		for(int i=0;i<26;i++) arr[i] = 0;
		for(int i=0;i<10;i++) num[i] = 0;
		for(int i=0;i<s.length();i++){
			char cc = s.at(i);
			int temp = cc-'0';
			temp -= 17;
			arr[temp]++;
		}
		
		int uk = met('Z');
		num[0] = arr[uk];
		mymet(ss[0],num[0]);
	
			uk = met('W');
		num[2] = arr[uk];
		mymet(ss[2],num[2]);
		 uk = met('G');
		num[8] = arr[uk];
		mymet(ss[8],num[8]);
		 uk = met('X');
		num[6] = arr[uk];
		mymet(ss[6],num[6]);
		 uk = met('U');
		num[4] = arr[uk];
		mymet(ss[4],num[4]);
		uk = met('O');
		num[1] = arr[uk];
		mymet(ss[1],num[1]);
		uk = met('F');
		num[5] = arr[uk];
		mymet(ss[5],num[5]);
	 uk = met('H');
		num[3] = arr[uk];
		mymet(ss[3],num[3]);
		 uk = met('S');
		num[7] = arr[uk];
		mymet(ss[7],num[7]);
		 uk = met('E');
		num[9] = arr[uk];
		mymet(ss[9],num[9]);
		cout << "Case #"<<k1<<": ";
		for(int i=0;i<10;i++){
			for(int j=1;j<=num[i];j++)
				cout <<i;
		}
		cout << endl;
		
	}
	return 0;
}
