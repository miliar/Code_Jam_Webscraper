#include <iostream>
using namespace std;

int main() {
	int n,num[18],r,ans;
	int TESTCASE;
	int t,reset,i;
	cin >> TESTCASE;
	for(t=1;t<=TESTCASE;t++){
		for(reset=0;reset<=17;reset++) num[reset]=0;
		cin >> r;
		for(i=1;i<=16;i++){
			cin >> n;
			if(r==1&&i>=1&&i<=4) num[n]++;
			else if(r==2&&i>=5&&i<=8) num[n]++;
			else if(r==3&&i>=9&&i<=12) num[n]++;
			else if(r==4&&i>=13&&i<=16) num[n]++;
		}
		cin >> r;
		for(i=1;i<=16;i++){
			cin >> n;
			if(r==1&&i>=1&&i<=4) num[n]++;
			else if(r==2&&i>=5&&i<=8) num[n]++;
			else if(r==3&&i>=9&&i<=12) num[n]++;
			else if(r==4&&i>=13&&i<=16) num[n]++;
		}
		n=0; ans=0;
		for(i=1;i<=16;i++){
			if(num[i]==2){ n=i; ans++; }
		}
		cout << "Case #" << t << ": ";
		if(ans==1) cout << n << endl;
		else if(ans>1) cout << "Bad magician!" << endl;
		else cout << "Volunteer cheated!" << endl;
	}
	return 0;
}
