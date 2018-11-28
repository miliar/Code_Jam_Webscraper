#include<iostream>
#include<string>

using namespace std;

int negf;

char prod(char a,char b) {
	if(a=='1') {
		if(b=='1')	return '1';
		if(b=='i')	return 'i';
		if(b=='j')	return 'j';
		if(b=='k')	return 'k';
	}
	if(a=='i') {
		if(b=='1')	return 'i';
		if(b=='i') {
			negf=1-negf;
			return '1';
		}
		if(b=='j')	return 'k';
		if(b=='k') {
			negf=1-negf;
			return 'j';
		}
	}
	if(a=='j') {
		if(b=='1')	return 'j';
		if(b=='i'){
			negf=1-negf;
			return 'k';
		}
		if(b=='j'){
			negf=1-negf;
			return '1';
		}
		if(b=='k')	return 'i';
	}
	if(a=='k') {
		if(b=='1')	return 'k';
		if(b=='i')	return 'j';
		if(b=='j'){
			negf=1-negf;
			return 'i';
		}
		if(b=='k'){
			negf=1-negf;
			return '1';
		}
	}
}
int main() {
	int k,t,i,j,l,x,flag,m;
	string s,st;
	char cur;
	cin >> t;
	for(k=1;k<=t;k++) {
		cin >> l >> x;
		cin >> s;
		st="";
		for(i=0;i<x;i++)	st+=s;
		cur='1';
		flag=0;
		negf=0;
		for(i=0;i<l*x;i++) {
			cur=prod(cur,st[i]);	
		}
		if(cur!='1' || !negf){
			cout << "Case #" << k << ": NO\n";
			continue;
		}
		cur='1';
		negf=0;
		for(i=0;i<l*x;i++) {
			cur=prod(cur,st[i]);	
			if(cur=='i' && !negf) {
				cur='1';
				for(j=i+1;j<l*x;j++) {
					cur=prod(cur,st[j]);
					if(cur=='j' && !negf) {
						cur='1';
						for(m=j+1;m<l*x;m++) {
							cur=prod(cur,st[m]);
						}
						if(cur=='k' && !negf){
							flag=1;
							break;
						}
						cur='j';
						negf=0;
					}
					if(flag)	break;
				}
				if(flag)	break;
				cur='i';
				negf=0;
			}
			if(flag)	break;
		}
		if(!flag)	cout << "Case #" << k << ": NO\n";
		else	cout << "Case #" << k << ": YES\n";
	}
	return 0;
}
