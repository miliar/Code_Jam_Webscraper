#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int n;
	cin >> n;
	string str;	
	for(int d=0;d<n;d++){
		cout << "Case #" << d+1 << ": ";
		cin >> str;
		vector<int> number;
		int o=0;int n=0;int e=0;int t=0;int w=0;int h=0;int r=0;int f=0;int u=0;int i=0;int v=0;int x=0;int s=0;int g=0;int z=0;
		for(int j=0;j<str.length();j++){
			switch (str[j]){
				case 'O':
					o+=1;
					break;
				case 'N':
					n+=1;
					break;
				case 'E':
					e+=1;
					break;
				case 'T':
					t+=1;
					break;
				case 'W':
					w+=1;
					break;
				case 'H':
					h+=1;
					break;
				case 'R':
					r+=1;
					break;
				case 'F':
					f+=1;
					break;
				case 'U':
					u+=1;
					break;
				case 'I':
					i+=1;
					break;
				case 'V':
					v+=1;
					break;
				case 'X':
					x+=1;
					break;
				case 'S':
					s+=1;
					break;
				case 'G':
					g+=1;
					break;
				case 'Z':
					z+=1;
					break;
			}			
		}
		i-=x;
		s-=x;
		for(int q=0;q<x;q++){
			number.push_back(6);
		}
		f-=u;
		o-=u;
		r-=u;
		for(int q=0;q<u;q++){
			number.push_back(4);
		}
		t-=w;
		o-=w;
		for(int q=0;q<w;q++){
			number.push_back(2);
		}
		e-=g;
		i-=g;
		h-=g;
		t-=g;
		for(int q=0;q<g;q++){
			number.push_back(8);
		}
		e-=z;
		r-=z;
		o-=z;
		for(int q=0;q<z;q++){
			number.push_back(0);
		}
		i-=f;
		v-=f;
		e-=f;
		for(int q=0;q<f;q++){
			number.push_back(5);
		}
		s-=v;
		e-=2*v;
		n-=v;
		for(int q=0;q<v;q++){
			number.push_back(7);
		}
		n-=o;
		e-=o;
		for(int q=0;q<o;q++){
			number.push_back(1);
		}
		n-=2*i;
		e-=i;
		for(int q=0;q<i;q++){
			number.push_back(9);
		}
		for(int q=0;q<t;q++){
			number.push_back(3);
		}
		std::sort(number.begin(), number.end());
		for(int l=0;l<number.size();l++){
			cout << number[l];
		}
		cout << endl;
	}
	return 0;
}