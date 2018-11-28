#include <iostream>
#include <cstring>

using namespace std;

char c[150][150];
int si[150][150];

int T,x,l;
string st;

int main(){
	cin >> T;

	c['1']['1']=c['i']['i']=c['j']['j']=c['k']['k']='1';
	c['1']['i']=c['i']['1']=c['j']['k']=c['k']['j']='i';
	c['1']['j']=c['j']['1']=c['i']['k']=c['k']['i']='j';
	c['1']['k']=c['k']['1']=c['i']['j']=c['j']['i']='k';

	si['i']['i']=si['j']['j']=si['k']['k']=si['i']['k']=si['j']['i']=si['k']['j']=1;

	for (int ti=1;ti<=T;ti++){
		int f[10010];
		memset(f,0,sizeof(f));
		cin >> l >> x;
		cin >>st;
		cout << "Case #"<<ti<<": ";
		string s = "";
		for (int i=1;i<=x;i++) s+=st;
		//cout << s<<endl;
		char now = '1';
		int tot=0;
		int bo=-1;
		for (int i=0;i<s.length();i++){
			char next = c[now][s[i]];
			tot+=si[now][s[i]];
			if (next=='i' && tot%2==0 && bo==-1) bo=i;
			if (next=='k' && tot%2==0) f[i]=1;
			now=next;
			//cout<<f[i];
		}
		//cout<<endl;
		//cout << bo<<endl;
		int flag=-1;
		now='1';
		tot=0;
		for (int i=s.length()-1;i>0;i--){
			char next = c[now][s[i]];
			tot+=si[s[i]][now];
			if (next=='k' && tot%2==0)
				if (f[i-1]==1 && i-1>bo){
					//cout<<i<<endl;
					int l1=bo+1,l2=i-1-bo,l3=x*l-i;
					if (l1>0 && l2>0 && l3>0){
						flag=1;
						char pp='1';
						int pp1=0,pp2=0,pp3=0;
						for (int j=0;j<=bo;j++){pp1+=si[pp][s[j]];pp=c[pp][s[j]];}
						if (!(pp=='i' && pp1%2==0) ) cout<<"!"<<endl;
						pp='1';
						for (int j=bo+1;j<i;j++){pp2+=si[pp][s[j]];pp=c[pp][s[j]];}
						if (!(pp=='j' && pp2%2==0) ) cout<<st<<"!!"<<endl;
						pp='1';
						for (int j=i;j<x*l;j++){pp3+=si[pp][s[j]];pp=c[pp][s[j]];}
						if (!(pp=='k' && pp3%2==0) ) cout<<"!!!"<<endl;
						

					}
				}
			now=next;
		}
				
		//if (bo==-1) flag=-1;

		if (flag==-1) cout<<"NO"<<endl;
			else cout<<"YES"<<endl;
	}
	return 0;
}
