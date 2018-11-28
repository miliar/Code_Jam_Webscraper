#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
void solve(int c){
	string s;
	cin >> s;
	vector<int> al(26,0),num(10,0);
	int l=s.length();
	for(int i=0;i<l;++i)
		++al[s[i]-65];
	if(al[25]){				// ZERO
		num[0]=al[25];
		al[4]-=al[25];
		al[17]-=al[25];
		al[14]-=al[25];
		al[25]=0;
	}
	if(al[20]){				//FOUR
		num[4]=al[20];
		al[5]-=al[20];
		al[14]-=al[20];
		al[17]-=al[20];
		al[20]=0;
	}
	if(al[22]){				//TWO
		num[2]=al[22];
		al[19]-=al[22];
		al[14]-=al[22];
		al[22]=0;
	}
	if(al[23]){				//SIX
		num[6]=al[23];
		al[18]-=al[23];
		al[8]-=al[23];
		al[23]=0;
	}
	if(al[5]){				//FIVE
		num[5]=al[5];
		al[8]-=al[5];
		al[21]-=al[5];
		al[4]-=al[5];
		al[5]=0;
	}
	if(al[6]){				//EIGHT
		num[8]=al[6];
		al[4]-=al[6];
		al[8]-=al[6];
		al[7]-=al[6];
		al[19]-=al[6];
		al[6]=0;
	}
	if(al[19]){				//THREE
		num[3]=al[19];
		al[7]-=al[19];
		al[17]-=al[19];
		al[4]-=al[19];
		al[4]-=al[19];
		al[19]=0;
	}
	if(al[14]){				//ONE
		num[1]=al[14];
		al[13]-=al[14];
		al[4]-=al[14];
		al[14]=0;
	}
	if(al[18]){				//SEVEN
		num[7]=al[18];
		al[4]-=al[18];
		al[21]-=al[18];
		al[4]-=al[18];
		al[13]-=al[18];
		al[18]=0;
	}
	if(al[8]){				//NINE
		num[9]=al[8];
		al[13]-=al[8];
		al[13]-=al[8];
		al[4]-=al[8];
		al[8]=0;
	}
	printf("Case #%d: ",c);
	for(int i=0;i<10;++i){
		while(num[i]--) cout << i;
	}
	cout << endl;
	return;
}

int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;++i) 
		solve(i);
	return 0; 
}
/*

4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER

*/