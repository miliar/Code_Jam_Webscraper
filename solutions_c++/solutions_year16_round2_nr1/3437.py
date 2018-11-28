#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string>

using namespace std;

string Ns[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

vector<int> Nums(11);

bool InNote(int i, const string &note) {
	for(string::const_iterator it = Ns[i].begin(); it != Ns[i].end(); it++) {
		if(count(note.begin(), note.end(),*it) < count(Ns[i].begin(), Ns[i].end(),*it)) return false;
	}
	return true;
}

vector<int> cn(vector<int> in, int CurNum, string note) {
	if(note.length()==0) { in[10]=1; return in;}
	if(CurNum>9) { in[10]=0; return in;}
	if( InNote(CurNum, note) ){
		for(string::const_iterator it = Ns[CurNum].begin(); it != Ns[CurNum].end(); it++) {
			note.erase(note.find(*it),1);
		}
		in[CurNum]++;
		vector<int> Out(11);
		Out = cn(in,CurNum,note);
		if(Out[10]) return Out;
		in[CurNum]--;
		note = note + Ns[CurNum];
	}
	return cn(in, CurNum+1,note);
}


int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		cout << "Case #" << NumCase << ": ";

		string Note;
		cin >> Note;
		for(int i=0;i<11;i++) Nums[i]=0;
		Nums = cn(Nums, 0, Note);
		for(int i=0;i<10;i++) 
			for(int j=0;j<Nums[i];j++) cout << i;

		cout << endl;
	}
	return 0;
}
