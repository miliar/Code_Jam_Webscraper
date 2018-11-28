//By SCJ
#include<iostream>
using namespace std;
int main()
{
ios::sync_with_stdio(0);
cin.tie(0);
	int T;cin>>T;
	for(int no=1;no<=T;++no)
	{
		string s;cin>>s;
		int a[128],ans[10];
		for(int i=0;i<128;++i) a[i]=0;
		for(int i=0;i<10;++i) ans[i]=0;
		for(int i=0;i<s.size();++i) a[s[i]]++;
		//cout<<a['E']<<endl;
		int t=a['Z'];
		ans[0]+=t;a['Z']-=t;a['E']-=t;a['R']-=t;a['O']-=t;
		t=a['W'];
		ans[2]+=t;a['T']-=t;a['W']-=t;a['O']-=t;
		t=a['G'];
		ans[8]+=t;a['E']-=t;a['I']-=t;a['G'];a['H']-=t;a['T']-=t;

		t=a['X'];
		ans[6]+=t;a['S']-=t;a['I']-=t;a['X']-=t;
		t=a['S'];
		ans[7]+=t;a['S']-=t;a['E']-=2*t;a['V']-=t;a['N']-=t;
		t=a['H'];
		ans[3]+=t;a['T']-=t;a['H']-=t;a['R']-=t;a['E']-=2*t;

		t=a['R'];
		ans[4]+=t;a['F']-=t;a['O']-=t;a['U']-=t;a['R']-=t;
		t=a['O'];
		ans[1]+=t;a['O']-=t;a['N']-=t;a['E']-=t;
		t=a['V'];
		ans[5]+=t;a['F']-=t;a['I']-=t;a['V']-=t;a['E']-=t;
		t=a['E'];
		ans[9]+=t;
		cout<<"Case #"<<no<<": ";
		//for(int i=0;i<9;++i) cout<<i<<' '<<ans[i]<<'\n';
		for(int i=0;i<10;++i)
		{
			for(int j=0;j<ans[i];++j) cout<<i;
		}
		cout<<'\n';
	}

}
