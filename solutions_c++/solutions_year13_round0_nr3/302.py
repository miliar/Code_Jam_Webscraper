#include <iostream>
#include <map>
#include <stdio.h>
#include <set>
#include <stack>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <sstream>
#include <list>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <string>
#include <string.h>
#include <math.h>
using namespace std;
/**
 * @author:	Shamir14 -- Amirhossein Shapoori
 * lordamir14@gmail.com
 * ACM team: AnotherChorMangz
 * Tehran, Iran
 * Still listening to Mark Knopfler...
 * :P
 */
 
 const int maxn = 47000;
 vector <string> Bint;

 int Cmp(string &s1, string &s2){
	 int i, sz1, sz2;
	 sz1 = s1.size(); sz2 = s2.size();
	 if(sz1 != sz2)
		 return sz1 - sz2;
	 for(i = 0; i < sz1; i++)
		 if(s1[i] > s2[i]) return 1;
		 else if(s1[i] < s2[i]) return -1;
	return 0;
 }

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i, test, t, cnt;
	ifstream Big;
	string str, A, B;
	Big.open("Big.in", ifstream::in);
	while(Big >> str)
		Bint.push_back(str);

	int Up, Lo, Me, start, end;

	cin >> test;
	t = 0;
	while(test--){
		cin >> A >> B;
		cnt = 0;
		// for A
		Up = Bint.size();
		Lo = 0;

		while(Up - Lo > 1){
			Me = (Up + Lo) / 2;
			if(Cmp(A, Bint[Me]) <= 0)
				Up = Me;
			else
				Lo = Me;
		}
		start = Up;
		if(Cmp(Bint[Lo], A) == 0)
			start = Lo;


		// for B
		Up = Bint.size();
		Lo = 0;

		while(Up - Lo > 1){
			Me = (Up + Lo) / 2;
			if(Cmp(B, Bint[Me]) <= 0)
				Up = Me;
			else
				Lo = Me;
		}
		end = Lo;
		if(Cmp(Bint[Up], B) == 0)
			end = Up;

		cnt = end - start + 1;

		/*
		for(i = 0; i < Bint.size(); i++)
			if(Cmp(A, Bint[i]) <= 0 && Cmp(B, Bint[i]) >= 0)
				cnt++;*/
		cout << "Case #" << ++t << ": " << cnt << endl;
	}
	
	
	return 0;
}

