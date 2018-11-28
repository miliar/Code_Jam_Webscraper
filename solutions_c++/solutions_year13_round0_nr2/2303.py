#include <fstream>
#include <iostream>
#include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
#define cin fin
#define cout fout

int main()
{
	int n;
	cin>>n;
	for(int x=1;x<=n;x++){
		char a[110][110];
		int p,q;
		cin>>p>>q;
		for(int i=0;i<p;i++) for(int j=0;j<q;j++) cin>>a[i][j];
		bool can=1;
		for(int i=0;i<p;i++) for(int j=0;j<q;j++){
			bool tmp1=1,tmp2=1;
			for(int k=0;k<p;k++) if(a[k][j]>a[i][j]) tmp1=0;
			for(int k=0;k<q;k++) if(a[i][k]>a[i][j]) tmp2=0;
			if(tmp1==0 && tmp2==0) can=0;
		}
		cout<<"Case #"<<x<<": ";
		if(can) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
}