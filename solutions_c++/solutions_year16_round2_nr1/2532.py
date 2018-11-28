#include <iostream>
#include <string>
#include <math.h>
#include <fstream>

using namespace std;

int main(){
	int Test,cnt;
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	in>>Test;
	for (cnt=1;cnt<=Test;cnt++){
		string str;
		in>>str;
		int ch[26];
		int digit[10];
		for (int i=0;i<26;i++){
			ch[i]=0;
		}
		for (int i=0;i<10;i++){
			digit[i]=0;
		}
		for (int i=0;i<str.length();i++){
			ch[(int)str[i]-'A']+=1;
		}
		digit[0]=ch['Z'-'A'];
		ch['O'-'A']-=ch['Z'-'A'];
		ch['E'-'A']-=ch['Z'-'A'];
		ch['R'-'A']-=ch['Z'-'A'];
		ch['Z'-'A']=0;
		digit[2]=ch['W'-'A'];
		ch['T'-'A']-=ch['W'-'A'];
		ch['O'-'A']-=ch['W'-'A'];
		ch['W'-'A']=0;
		digit[4]=ch['U'-'A'];
		ch['F'-'A']-=ch['U'-'A'];
		ch['O'-'A']-=ch['U'-'A'];
		ch['R'-'A']-=ch['U'-'A'];
		ch['U'-'A']=0;
		digit[3]=ch['R'-'A'];;
		ch['T'-'A']-=ch['R'-'A'];
		ch['H'-'A']-=ch['R'-'A'];
		ch['E'-'A']-=(2*ch['R'-'A']);
		ch['R'-'A']=0;
		digit[5]=ch['F'-'A'];
		ch['I'-'A']-=ch['F'-'A'];
		ch['V'-'A']-=ch['F'-'A'];
		ch['E'-'A']-=ch['F'-'A'];
		ch['F'-'A']=0;
		digit[1]=ch['O'-'A'];
		ch['N'-'A']-=ch['O'-'A'];
		ch['E'-'A']-=ch['O'-'A'];
		ch['O'-'A']=0;
		digit[6]=ch['X'-'A'];
		ch['I'-'A']-=ch['X'-'A'];
		digit[7]=ch['V'-'A'];
		digit[8]=ch['T'-'A'];
		ch['I'-'A']-=ch['T'-'A'];
		digit[9]=ch['I'-'A'];
		out<<"Case #"<<cnt<<": ";
		for (int i=0;i<10;i++){
			for (int j=0;j<digit[i];j++){
				out<<i;
			}
		}
		out<<endl;
	}
	in.close();
	out.close();
}
