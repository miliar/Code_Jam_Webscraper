#include <iostream>
#include <string>
using namespace std;

int T;

int ans[10];
int occur[26];
string inp;

void solve()
{
	for(int i=0;i<10;++i){
		ans[i]=0;
	}
	for(int i=0;i<26;++i){
		occur[i]=0;
	}

	int len = inp.length();
	for(int i=0;i<len;++i){
		occur[inp[i]-'A'] += 1;
	}

	while(len>0){
		if(occur['Z'-'A'] > 0){
			++ans[0];
			len -= 4;
			occur['Z'-'A'] -= 1;
			occur['E'-'A'] -= 1;
			occur['R'-'A'] -= 1;
			occur['O'-'A'] -= 1;
		}
		else{
			break;
		}
	}


	while(len>0){
		if(occur['W'-'A'] > 0){
			++ans[2];
			len -= 3;
			occur['T'-'A'] -= 1;
			occur['W'-'A'] -= 1;
			occur['O'-'A'] -= 1;
		}
		else{
			break;
		}
	}

	while(len>0){
		if(occur['U'-'A'] > 0){
			++ans[4];
			len -= 4;
			occur['F'-'A'] -= 1;
			occur['O'-'A'] -= 1;
			occur['U'-'A'] -= 1;
			occur['R'-'A'] -= 1;
		}
		else{
			break;
		}
	}

	while(len>0){
		if(occur['X'-'A'] > 0){
			++ans[6];
			len -= 3;
			occur['S'-'A'] -= 1;
			occur['I'-'A'] -= 1;
			occur['X'-'A'] -= 1;
		}
		else{
			break;
		}
	}

	while(len>0){
		if(occur['G'-'A'] > 0){
			++ans[8];
			len -= 5;
			occur['E'-'A'] -= 1;
			occur['I'-'A'] -= 1;
			occur['G'-'A'] -= 1;
			occur['H'-'A'] -= 1;
			occur['T'-'A'] -= 1;
		}
		else{
			break;
		}
	}

	while(len>0){
		if(occur['R'-'A'] > 0){
			++ans[3];
			len -= 5;
			occur['T'-'A'] -= 1;
			occur['H'-'A'] -= 1;
			occur['R'-'A'] -= 1;
			occur['E'-'A'] -= 1;
			occur['E'-'A'] -= 1;
		}
		else{
			break;
		}
	}

	while(len>0){
		if(occur['F'-'A'] > 0){
			++ans[5];
			len -= 4;
			occur['F'-'A'] -= 1;
			occur['I'-'A'] -= 1;
			occur['V'-'A'] -= 1;
			occur['E'-'A'] -= 1;
		}
		else{
			break;
		}
	}

	while(len>0){
		if(occur['I'-'A'] > 0){
			++ans[9];
			len -= 4;
			occur['N'-'A'] -= 1;
			occur['I'-'A'] -= 1;
			occur['N'-'A'] -= 1;
			occur['E'-'A'] -= 1;
		}
		else{
			break;
		}
	}

	while(len>0){
		if(occur['V'-'A'] > 0){
			++ans[7];
			len -= 5;
			occur['S'-'A'] -= 1;
			occur['E'-'A'] -= 1;
			occur['V'-'A'] -= 1;
			occur['E'-'A'] -= 1;
			occur['N'-'A'] -= 1;
		}
		else{
			break;
		}
	}

	while(len>0){
		if(occur['O'-'A'] > 0){
			++ans[1];
			len -= 3;
			occur['O'-'A'] -= 1;
			occur['N'-'A'] -= 1;
			occur['E'-'A'] -= 1;
		}
		else{
			break;
		}
	}
//	assert(len==0);
//	cout<<"len "<<len<<endl;
}

int main()
{
	cin>>T;
	for(int xx=1; xx<=T; ++xx){
		cin>>inp;
		solve();
		cout<<"Case #"<<xx<<": ";
		for(int i=0;i<10;++i){
			for(int j=0;j<ans[i];++j){
				cout<<i;
			}
		}
		cout<<endl;
	}
	return 0;
}
