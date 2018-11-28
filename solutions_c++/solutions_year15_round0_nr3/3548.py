#include<iostream>
#include<string>
using namespace std;

typedef struct Quat{
	char q;
	int sign;
}Quat;

Quat times(Quat a,Quat b){
	Quat ret;
	if(a.q == 'i'){
		if(b.q == 'i'){
			ret.q = '1';
			ret.sign = -1;
		}
		else if(b.q == 'j'){
			ret.q = 'k';
			ret.sign = 1;
		}
		else if(b.q == 'k'){
			ret.q = 'j';
			ret.sign = -1;
		}else{}
	}else if(a.q == 'j'){
		if(b.q == 'i'){
			ret.q = 'k';
			ret.sign = -1;
		}else if(b.q == 'j'){
			ret.q = '1';
			ret.sign = -1;
		}else if(b.q == 'k'){
			ret.q = 'i';
			ret.sign = 1;
		}else{}
	}else if(a.q == 'k'){
		if(b.q == 'i'){
			ret.q = 'j';
			ret.sign = 1;
		}else if(b.q == 'j'){
			ret.q = 'i';
			ret.sign = -1;
		}else if(b.q == 'k'){
			ret.q = '1';
			ret.sign = -1;
		}else{}
	}else if(a.q == '1'){
		ret.q = b.q;
		ret.sign = b.sign;
	}

	ret.sign *= a.sign * b.sign;
	return ret;
}

bool quatCmp(Quat a, Quat b){
	if(a.q == b.q && a.sign == b.sign) return true;
	else return false;
}

int main(void){

	int T;
	int L;
	int X;
	int cursor;
	Quat now;
	Quat nex;
	char tmp;
	Quat* input;
	Quat I;
	Quat J;
	Quat K;
	Quat nul;
	Quat target;
	bool sucFlag;
	bool breakFlag;

	I.q = 'i';
	J.q = 'j';
	K.q = 'k';
	nul.q = '1';
	I.sign = 1;
	J.sign = 1;
	K.sign = 1;
	nul.sign = 1;


	cin >> T;
	for(int t=0;t<T;t++){

		cin >> L >> X;
		input = new Quat[L*X];
		for(int i=0;i<L;i++){
			cin >> tmp;
			input[i].q = tmp;
			input[i].sign = 1;
		}
		for(int i=L;i<L*X;i++){
			input[i].q = input[i%L].q;
			input[i].sign = 1;
		}	


		cursor = 1;
		now = input[cursor-1];
		nex = input[cursor];
		target = I;
		sucFlag = false;
		breakFlag = false;
		while(true){
			if(quatCmp(now,target)){
				// cout << "target update." << endl;
				if(quatCmp(target,I)) target = J;
				else if(quatCmp(target,J)) target = K;
				else if(quatCmp(target,K)) target = nul;
				
				now.q = '1';
				now.sign = 1;
			}
			if(breakFlag){
				if(quatCmp(now,nul) && quatCmp(target,nul)) sucFlag = true;
				break;
			}
			//cout << "times ";
			//cout << now.q << " " << now.sign;
			//cout << " * ";
			//cout << nex.q << " " << nex.sign << endl;
			now = times(now,nex);
			cursor++;
			if(cursor == L*X){	
				breakFlag = true;
			}
			if(!breakFlag)nex = input[cursor];
			
			//if(now.sign == 1)cout << now.q;
			//else cout << "-" << now.q;
			//for(int i=cursor;i<L*X;i++) cout << input[i].q;
			//cout << endl;

		}
		//cout << "target is " << target.q << " " << target.sign << endl;
		//cout << "   now is " << now.q    << " " <<    now.sign << endl;
		cout << "Case #" << t+1 << ": ";
		if(sucFlag) cout << "YES" << endl;
		else cout << "NO" << endl;
		delete [] input;

	}
	return 0;
}
