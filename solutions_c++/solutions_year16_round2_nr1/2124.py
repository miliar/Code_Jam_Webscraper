#include <iostream>
#include <vector>
using namespace std;

#define ll long long
#define vll vector<long long>

int main(){

int Te;
cin>>Te;
for(int te=1;te<=Te;te++){
	vll ar(26,0);
	string s;
	cin>>s;
	int n=s.size();
	for(int i=0;i<n;i++){
		ar[s[i]-'A']++;
	}
	vll ans(10,0);
	ans[0]=ar[25];
	ar['E'-'A']-=ar[25];
	ar['R'-'A']-=ar[25];
	ar['O'-'A']-=ar[25];
	ans[2]=ar['W'-'A'];
	ar['T'-'A']-=ans[2];
	ar['O'-'A']-=ans[2];
	ans[4]=ar['U'-'A'];
	ar['F'-'A']-=ans[4];
	ar['O'-'A']-=ans[4];
	ar['R'-'A']-=ans[4];
	ans[6]=ar['X'-'A'];
	ar['S'-'A']-=ans[6];
	ar['I'-'A']-=ans[6];
	ans[8]=ar['G'-'A'];
	ar['E'-'A']-=ans[8];
	ar['I'-'A']-=ans[8];
	ar['H'-'A']-=ans[8];
	ar['T'-'A']-=ans[8];
	ans[1]=ar['O'-'A'];
	ar['N'-'A']-=ans[1];
	ar['E'-'A']-=ans[1];
	ans[3]=ar['R'-'A'];
	ar['T'-'A']-=ans[3];
	ar['H'-'A']-=ans[3];
	ar['E'-'A']-=2*ans[3];
	ans[5]=ar['F'-'A'];
	ar['I'-'A']-=ans[5];
	ans[7]=ar['S'-'A'];
	ans[9]=ar['I'-'A'];
	cout<<"Case #"<<te<<": ";
	for(int i=0;i<10;i++){
		while(ans[i]>0){
			cout<<i;
			ans[i]--;
		}
	}
	cout<<endl;
	
}
return 0;


}