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
map<pair<int, int>,int>matrix;
map<char , int > wordmap;
int main(){
	
	wordmap.insert(mp('i',2));
	wordmap.insert(mp('j',3));
	wordmap.insert(mp('k',4));
	
	matrix.insert(mp(mp(1,1),1));
	matrix.insert(mp(mp(1,2),2));
	matrix.insert(mp(mp(1,3),3));
	matrix.insert(mp(mp(1,4),4));
	matrix.insert(mp(mp(2,1),1));
	matrix.insert(mp(mp(2,2),5));
	matrix.insert(mp(mp(2,3),4));
	matrix.insert(mp(mp(2,4),7));
	matrix.insert(mp(mp(3,1),3));
	matrix.insert(mp(mp(3,2),8));
	matrix.insert(mp(mp(3,3),5));
	matrix.insert(mp(mp(3,4),2));
	matrix.insert(mp(mp(4,1),4));
	matrix.insert(mp(mp(4,2),3));
	matrix.insert(mp(mp(4,3),6));
	matrix.insert(mp(mp(4,4),5));
	
	ifstream fin;
	ofstream fout;
	fin.open("in.txt");
	fout.open("out.txt");	
	int t,L,X;
	string str;
	string temp;
	vector<int> inp;
	vector<int> ans;
	fin >> t;
	for(int k = 1 ; k<=t ; k++){
		str.clear();
		ans.clear();
		inp.clear();
		fin >> L >> X;
		fin >> str;
		temp = str;
		if(L*X < 3){
			fout << "Case #" << k << ": NO" << endl;
			continue;
		}
		for(int i = 0 ; i< X-1 ; i++){
			str = str +  temp;
		}
		for(int i = 0 ; i< str.size() ; i++){
			inp.pb(wordmap[str[i]]); 
		}
		ans.pb(inp[0]);
		for(int i = 1 ; i< inp.size() ; i++){
			if(ans[i-1] > 4){
				int tt = matrix[mp(ans[i-1] - 4 , inp[i])];
				if(tt > 4)
					ans.pb(tt - 4);
				else 
					ans.pb(tt + 4);
			}
			else{
				ans.pb(matrix[mp(ans[i-1], inp[i])]);
			}
		}
		if(ans[ans.size()-1] != 5){
			fout << "Case #" << k << ": NO" << endl;
			continue;
		}
		else{
			int flag = 0;
			for(int i = 0 ; i < ans.size() ; i++){
				if(ans[i] == 2){
					for(int kk = i+1; kk < ans.size() ; kk++){
						if(ans[kk] == 4){
							flag =1;
							break;
						}
					}
					if(flag == 1){
						break;
					}
				}
			}
			if(flag == 1){
				fout << "Case #" << k << ": YES" << endl;
			}		
			else{
				fout << "Case #" << k << ": NO" << endl;
			}
		}
	}	
return 0;
}
