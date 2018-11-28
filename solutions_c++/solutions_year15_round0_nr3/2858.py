#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int multiplicative (char a,char b){
	int neg = 1;
	if(-a == '1' || -a == 'i' || -a == 'j' || -a == 'k'){
		neg=-neg;
		a = -a;
	}
	if(-b == '1' || -b == 'i' || -b == 'j' || -b == 'k'){
		neg=-neg;
		b= -b;
	}
	if(a == '1')
		return	neg * b;
	else if(b == '1')
		return neg * a;
	else if(a == b)
		return neg * -'1';
	else if(a == 'i')
		if(b == 'j')
			return neg * 'k';
		else
			return neg * -'j';
	else if(a == 'j')
		if(b == 'k')
			return neg * 'i';
		else
			return neg * -'k';
	else if(a == 'k')
		if(b == 'i')
			return neg * 'j';
		else
			return neg * -'i';
}

int main()
{

	short T;
	cin>>T;
	for(short t = 1; t<= T;t++){
		int L,X;
		string s;
		cin>>L>>X;
		cin>>s;
		bool test1=false,test2=false,test3=false,rem=false;
		int res1='1',res2='1',res3='1',resrem = '1';
		for(int i=0;i<L*X;i++){
			if(!test1){
				res1=multiplicative(res1,s[i%L]);
				if(res1 == 'i')
					test1=true;
			}
			else if(!test2){
				res2=multiplicative(res2,s[i%L]);
				if(res2 == 'j')
					test2=true;
			}
			else if(!test3){
				res3=multiplicative(res3,s[i%L]);
				if(res3 == 'k')
					test3=true;
			}
			else if(!rem){
				resrem=multiplicative(resrem,s[i%L]);
			}
		}
		if(resrem == '1')
			rem=true;
		cout << "Case #" << t << ": ";
		if (test1 && test2 && test3 && rem) cout << "YES";
		else cout << "NO";
		cout << endl;
		
	}
	return 0;
}