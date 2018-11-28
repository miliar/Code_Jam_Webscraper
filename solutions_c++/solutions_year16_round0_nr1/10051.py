#include<iostream>
#include<string>
#include<functional>
#include<algorithm>
#include<set>
#include<vector>
#include<queue>
#include<deque>
#include<map>
#include<list>
#include<cmath>
#include<sstream>
#include<fstream>
using namespace std;

int main(){
	int T, i, j;
	int a, b, c;
	ifstream fin("1.txt");
	ofstream fout("a.txt");
	fin >> T;
	i = 0;
	while(i < T){
		fin>>a;
		if(i){
			fout<<endl;
		}
		if(a == 0){
			fout << "Case #" <<i + 1<<": INSOMNIA";
		}
		else{
			c = 0;
			j = 0;			
			while(c != 1023){
				j++;
				b = a * j;
				while(b!=0){
					c = c | (1 << (b%10));
					b /= 10;
				}
				
			}
			fout << "Case #" <<i + 1<<": "<< a * j;			
		}
		i++;
	}
	return 0;
} 
