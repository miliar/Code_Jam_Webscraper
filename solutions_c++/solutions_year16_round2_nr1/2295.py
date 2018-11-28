#include <bits/stdc++.h>
using namespace std;
string code[101];
int jumlah[10];
int jumlahhuruf[300];
int main(){
	int t;
	cin >> t;
	for(int i=0;i<t;i++){
		cin >> code[i];
	}
	for(int i=0;i<t;i++){
		int length = code[i].length();
		for (int j=0;j<length;j++){
			jumlahhuruf[code[i][j]]++;
		}
		jumlah[0]=jumlahhuruf['Z'];
		jumlahhuruf['E']-=jumlahhuruf['Z'];
		jumlahhuruf['R']-=jumlahhuruf['Z'];
		jumlahhuruf['O']-=jumlahhuruf['Z'];
		jumlah[2]=jumlahhuruf['W'];
		jumlahhuruf['T']-=jumlahhuruf['W'];
		jumlahhuruf['O']-=jumlahhuruf['W'];
		jumlah[4]=jumlahhuruf['U'];
		jumlahhuruf['F']-=jumlahhuruf['U'];
		jumlahhuruf['R']-=jumlahhuruf['U'];
		jumlahhuruf['O']-=jumlahhuruf['U'];
		jumlah[3]=jumlahhuruf['R'];
		jumlahhuruf['E']-=jumlahhuruf['R']*2;
		jumlahhuruf['T']-=jumlahhuruf['R'];
		jumlahhuruf['H']-=jumlahhuruf['R'];
		jumlah[1]=jumlahhuruf['O'];
		jumlahhuruf['E']-=jumlahhuruf['O'];
		jumlahhuruf['N']-=jumlahhuruf['O'];
		jumlah[5]=jumlahhuruf['F'];
		jumlahhuruf['E']-=jumlahhuruf['F'];
		jumlahhuruf['V']-=jumlahhuruf['F'];
		jumlahhuruf['I']-=jumlahhuruf['F'];
		jumlah[7]=jumlahhuruf['V'];
		jumlahhuruf['E']-=jumlahhuruf['V']*2;
		jumlahhuruf['S']-=jumlahhuruf['V'];
		jumlahhuruf['N']-=jumlahhuruf['V'];
		jumlah[6]=jumlahhuruf['X'];
		jumlahhuruf['S']-=jumlahhuruf['X'];
		jumlahhuruf['I']-=jumlahhuruf['X'];
		jumlah[8]=jumlahhuruf['G'];
		jumlahhuruf['E']-=jumlahhuruf['G'];
		jumlahhuruf['I']-=jumlahhuruf['G'];
		jumlahhuruf['H']-=jumlahhuruf['G'];
		jumlahhuruf['T']-=jumlahhuruf['G'];
		jumlah[9]=jumlahhuruf['I'];
		
		cout <<"Case #"<<i+1<<": ";
		for(int j=0;j<10;j++){
			for(int k=0;k<jumlah[j];k++){
				cout << j;
			}
		}
		cout << endl;
		
		memset(jumlah,0,sizeof(jumlah));
		memset(jumlahhuruf,0,sizeof(jumlahhuruf));
	}
}