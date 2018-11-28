#include <iostream>
#include <string>

using namespace std;

//0=Z, 2=W, 6=X, 4=U, 1=O, 5=F, 3=R, 8=T, 7=V, 9=I
int main(){
	int T;
	string temp;
	cin>>T;
	getline(cin, temp);
	for(int i=1;i<=T;i++){
		int a[26]={0,};
		int num[10]={0,};
		int n;
		int j,k;
		getline(cin, temp);
		for(j=0;j<temp.size();j++){
			a[temp[j]-'A']++;
		}
		cout<<"Case #"<<i<<": ";
		n=a['Z'-'A'];
		for(j=0;j<n;j++) num[0]++;
		a['Z'-'A']-=n;
		a['E'-'A']-=n;
		a['R'-'A']-=n;
		a['O'-'A']-=n;
		n=a['W'-'A'];
		for(j=0;j<n;j++) num[2]++;
		a['T'-'A']-=n;
		a['W'-'A']-=n;
		a['O'-'A']-=n;
		n=a['X'-'A'];
		for(j=0;j<n;j++) num[6]++;
		a['S'-'A']-=n;
		a['I'-'A']-=n;
		a['X'-'A']-=n;
		n=a['U'-'A'];
		for(j=0;j<n;j++) num[4]++;
		a['F'-'A']-=n;
		a['O'-'A']-=n;
		a['U'-'A']-=n;
		a['R'-'A']-=n;
		n=a['O'-'A'];
		for(j=0;j<n;j++) num[1]++;
		a['O'-'A']-=n;
		a['N'-'A']-=n;
		a['E'-'A']-=n;
		n=a['F'-'A'];
		for(j=0;j<n;j++) num[5]++;
		a['F'-'A']-=n;
		a['I'-'A']-=n;
		a['V'-'A']-=n;
		a['E'-'A']-=n;
		n=a['R'-'A'];
		for(j=0;j<n;j++) num[3]++;
		a['T'-'A']-=n;
		a['H'-'A']-=n;
		a['R'-'A']-=n;
		a['E'-'A']-=2*n;
		n=a['T'-'A'];
		for(j=0;j<n;j++) num[8]++;
		a['E'-'A']-=n;
		a['I'-'A']-=n;
		a['G'-'A']-=n;
		a['H'-'A']-=n;
		a['T'-'A']-=n;
		n=a['V'-'A'];
		for(j=0;j<n;j++) num[7]++;
		a['S'-'A']-=n;
		a['E'-'A']-=2*n;
		a['V'-'A']-=n;
		a['N'-'A']-=n;
		n=a['I'-'A'];
		for(j=0;j<n;j++) num[9]++;
		a['N'-'A']-=n;
		a['I'-'A']-=n;
		a['N'-'A']-=n;
		a['E'-'A']-=n;
		for(j=0;j<10;j++){
			for(k=0;k<num[j];k++){
				cout<<j;
			}
		}
		cout<<endl;
	}
	return 0;
}

