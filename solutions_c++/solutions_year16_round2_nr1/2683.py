#include<math.h>
#include<algorithm>
#include<string>
#include<map>
#include<iostream>
#include<stdio.h>
#include<vector>
#define FOR(i,l,r) for(int (i)=(l);(i)<(r);((i)++))
#define TEST(T) int T;scanf("%d",&T);getchar();int C = T;while(T--)
#define SIZE(v) ((int)(v).size())
using namespace std;
int main(){
	string s;
	vector<int> v;
	map<char,int> m1;
	TEST(T){
		printf("Case #%d: ",C-T);
		s.clear();
		m1.clear();
		v.clear();
		//scanf("%s",s);
		getline(cin,s);
		for(char c : s){
			m1[c]++;
		}
		//0
		for(int i = m1['Z']; i>0; i--){
			v.push_back(0);
			m1['Z']--;m1['E']--;m1['R']--;m1['O']--;
		}
		//6
		for(int i = m1['X']; i>0; i--){
			v.push_back(6);
			m1['S']--;m1['I']--;m1['X']--;
		}
		//8
		for(int i = m1['G']; i>0; i--){
			v.push_back(8);
			m1['E']--;m1['I']--;m1['G']--;m1['H']--;m1['T']--;
		}
		//2
		for(int i = m1['W']; i>0; i--){
			v.push_back(2);
			m1['T']--;m1['W']--;m1['O']--;
		}
		//7
		for(int i = m1['S']; i>0; i--){
			v.push_back(7);
			m1['S']--;m1['E']--;m1['V']--;m1['E']--;m1['N']--;
		}
		//5
		for(int i = m1['V']; i>0; i--){
			v.push_back(5);
			m1['F']--;m1['I']--;m1['V']--;m1['E']--;
		}
		//4
		for(int i = m1['F']; i>0; i--){
			v.push_back(4);
			m1['F']--;m1['O']--;m1['U']--;m1['R']--;
		}
		//1
		for(int i = m1['O']; i>0; i--){
			v.push_back(1);
			m1['O']--;m1['N']--;m1['E']--;
		}
		//3
		for(int i = m1['T']; i>0; i--){
			v.push_back(3);
			m1['T']--;m1['H']--;m1['R']--;m1['E']--;m1['E']--;
		}
		//9
		for(int i = m1['E']; i>0; i--){
			v.push_back(9);
			m1['N']--;m1['I']--;m1['N']--;m1['E']--;
		}
		sort(v.begin(),v.end());
		for (std::vector<int>::iterator it=v.begin(); it!=v.end(); ++it)
			printf("%d",*it);
			printf("\n");
	}
	return 0;
}
