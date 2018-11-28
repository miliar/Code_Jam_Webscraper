#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <list>
using namespace std;
typedef long long LL;
#define F(i,n) for (int i = 0; i < (int)(n); i++)



main(){

	FILE *fin = freopen("A-large.in", "r", stdin);
	assert (fin != NULL);
	//cout << "A open ";
	FILE *fout = freopen("A-large.out", "w", stdout);
	//cout << "A created";
	int T; 
	string s;
	vector<int> nums(10,0), count(30,0);
	/*count
	 *0: 'O'
	 *1: 'I'
	 *2: ''
	 *
	 **/
	cin >> T;

	//cout << "Test cases: " << T;
	for(int t = 1; t <= T; t++){
		cin >> s;
		F(i,10)
			nums[i] = 0;
		F(i,30)
			count[i] = 0;
		F(i,s.length()){
			count[s[i] - 'A']++;
		}
		F(i, count['Z' - 'A']){
			nums[0]++;
			count['E' - 'A']--;
			count['R' - 'A']--;
			count['O' - 'A']--;
		}

		F(i, count['W' - 'A']){
			nums[2]++;
			count['T' - 'A']--;
			
			count['O' - 'A']--;

		}
		F(i, count['U' - 'A']){
			nums[4]++;
			count['F' - 'A']--;
			count['O' - 'A']--;
			count['R' - 'A']--;
		}
		F(i, count['X' - 'A']){
			nums[6]++;
			count['S' - 'A']--;
			count['I' - 'A']--;
		
		}
		F(i, count['S' - 'A']){
			nums[7]++;
			count['E' - 'A']-=2;
			count['V' - 'A']--;
			count['N' - 'A']--;
		}
		F(i, count['G' - 'A']){
			nums[8]++;
			count['E' - 'A']--;
			count['I' - 'A']--;
			count['H' - 'A']--;
			count['T' - 'A']--;
		}

		F(i, count['O' - 'A']){
			nums[1]++;
			count['N' - 'A']--;
			count['E' - 'A']--;
			//count['H' - 'A']--;
			//count['T' - 'A']--;
		}
		F(i, count['F' - 'A']){
			nums[5]++;
			count['I' - 'A']--;
			count['V' - 'A']--;
			count['E' - 'A']--;
			//count['T' - 'A']--;
		}
		F(i, count['H' - 'A']){
			nums[3]++;
			count['T' - 'A']--;
			count['R' - 'A']--;
			count['E' - 'A']-=2;
			//count['T' - 'A']--;
		}
		F(i, count['I' - 'A']){
			nums[9]++;
			count['N' - 'A']-=2;
			//count['I' - 'A']--;
			count['E' - 'A']--;
			//count['T' - 'A']--;
		}


		



		cout << "Case #" << t << ": ";
		F(i, 10)
			F(j,nums[i])
				cout << i;
		cout << endl;
			


	}
	exit(0);
}
