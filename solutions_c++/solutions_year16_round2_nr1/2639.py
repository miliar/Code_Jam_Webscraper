#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>

using namespace std;

const string Digits[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

//-Z-ERO, EI-G-HT, SI-X-, -S-EVEN, FI-V-E, -F-OUR, TH-R-EE, T-W-O, -O-NE, N-I-NE 
int a[50];
int b[10];

void deal( int x, int y ){
	/*cout << "predebug" << Digits[1] << std::endl;
	cout<<"debug "<<y<<" "<<Digits[y]<<std::endl;
	for (int p=0; p<10; ++p){
	for (int i=0; i<Digits[p].size(); ++i)
		printf("%d", Digits[p][i]-'A');
	printf("\n");
	}*/
//	cout << Digits[y] <<std::endl;
	for (int i=0; i<Digits[y].size(); ++i){
//		cout << Digits[y][i]-'A';
		a[Digits[y][i]-'A']-=x;
	}
//	printf("\n");
}

void printa(){
	for (int i=0;i<26;++i)
	printf("%d", a[i]);
	printf("\n");
}

int main(){
	int T=0;
	cin>>T;
	for (int t=1; t<=T; ++t){
		string s;
		cin >> s;
		//cout << s <<endl;
		memset(a,0,sizeof(a));
		for (int i=0;i<s.size();++i)
			++a[s[i]-'A'];
		deal(0,0);
		b[0]=a['Z'-'A'];
		deal(b[0],0);
		b[8]=a['G'-'A'];
		deal(b[8],8);
		b[6]=a['X'-'A'];
		deal(b[6],6);
		b[7]=a['S'-'A'];
		deal(b[7],7);
		b[5]=a['V'-'A'];
		deal(b[5],5);
		b[4]=a['F'-'A'];
		deal(b[4],4);
		b[3]=a['R'-'A'];
		deal(b[3],3);
		b[2]=a['W'-'A'];
		deal(b[2],2);
		b[1]=a['O'-'A'];
		deal(b[1],1);
//		printa();
		b[9]=a['I'-'A'];
//		printf("OK\n");
		cout << "Case #" << t <<": ";
		for (int i=0;i<10;++i)
			for (int j=0;j<b[i];++j)
				cout<<i;
		cout<<std::endl;
	}
}
