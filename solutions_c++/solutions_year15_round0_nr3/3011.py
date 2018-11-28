using namespace std;
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>

typedef struct complex_variable {
	char sign;
	char symbol;
} complex;

char swap_sign (char sign) {
	if(sign == '+')
		return '-';
	else
		return '+';
}

bool equals (complex f, complex s) {
	if((f.sign == s.sign) && (f.symbol == s.symbol))
		return true;
	return false;
}

complex multiply (complex f, complex s) {
	complex p;
	if(f.sign == s.sign)
		p.sign = '+';
	else
		p.sign = '-';
	switch(f.symbol) {
		case '1':
			switch(s.symbol) {
				case '1': 
					p.symbol = '1';
					break;
				case 'i':
					p.symbol = 'i';
					break;
				case 'j': 
					p.symbol = 'j';
					break;
				case 'k':
					p.symbol = 'k';
					break;
			}
			break;
		case 'i':
		switch(s.symbol) {
				case '1': 
					p.symbol = 'i';
					break;
				case 'i':
					p.symbol = '1';
					p.sign = swap_sign(p.sign);
					break;
				case 'j': 
					p.symbol = 'k';
					break;
				case 'k':
					p.symbol = 'j';
					p.sign = swap_sign(p.sign);
					break;
			}
			break;
		case 'j': 
			switch(s.symbol) {
				case '1': 
					p.symbol = 'j';
					break;
				case 'i':
					p.symbol = 'k';
					p.sign = swap_sign(p.sign);
					break;
				case 'j': 
					p.symbol = '1';
					p.sign = swap_sign(p.sign);
					break;
				case 'k':
					p.symbol = 'i';
					break;
			}
			break;
		case 'k': 
			switch(s.symbol) {
				case '1': 
					p.symbol = 'k';
					break;
				case 'i':
					p.symbol = 'j';
					break;
				case 'j': 
					p.symbol = 'i';
					p.sign = swap_sign(p.sign);
					break;
				case 'k':
					p.symbol = '1';
					p.sign = swap_sign(p.sign);
					break;
			}
			break;	
	}
	return p;
}

int main() {
	int tc;
	cin>>tc;
	complex ii = {'+', 'i'};
	complex jj = {'+', 'j'};
	complex kk = {'+', 'k'};
	
	for(int t = 1;t<=tc;t++) {
		int l, x;
		cin>>l>>x;
		string s, str = "";
		cin>>s;
		for(int i = 0 ;i<x;i++) {
			str = str + s;
		}
		//cout<<"STRING = "<<str<<endl;
		complex p = {'+', '1'};
		int index = -1;
		bool flag = false;
		for(int i = 0;i<str.length();i++) {
			//cout<<p.sign<<p.symbol<<endl;
			//cout<<"I = "<<i<<endl;
			complex s = {'+', str[i]};
			p = multiply(p,s);
			if(equals(p,ii)) {
				index = i;
				flag = true;
				break;
			}
		}
		if(!flag) {
			printf("Case #%d: NO\n", t);
			continue;
		}
		flag = false;
		p.sign = '+';
		p.symbol = '1';
		for(int i = index + 1;i<str.length();i++) {
			//cout<<p.sign<<p.symbol<<endl;
			//cout<<"J = "<<i<<endl;
			complex s = {'+', str[i]};
			p = multiply(p,s);
			if(equals(p,jj)) {
				index = i;
				flag = true;
				break;
			}
		}
		if(!flag) {
			printf("Case #%d: NO\n", t);
			continue;
		}
		flag = false;
		p.sign = '+';
		p.symbol = '1';
		for(int i = index + 1;i<str.length();i++) {
			//cout<<p.sign<<p.symbol<<endl;
			//cout<<"K = "<<i<<endl;
			complex s = {'+', str[i]};
			p = multiply(p,s);
		}
		if(equals(p,kk))
			printf("Case #%d: YES\n", t);
		else
			printf("Case #%d: NO\n", t);
	}
	return 0;
}