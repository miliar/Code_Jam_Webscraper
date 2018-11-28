#include<iostream>
#include<cstdlib>
#include<string>
#include<cstdio>
using namespace std;

int main()
{
	freopen("../Downloads/A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int smax,alrstd,t;
	cin>>t;
	int tt=t;
	string s;
	int fp,f,slen,i;

	while(t--){
		alrstd=0;
		fp=f=0;
		cin>>smax>>s;
		slen = s.length();
		for(i=0;i<slen;i++){
			fp=f;
			if((s[i]-'0')!=0&&alrstd<i){
				f=f+i-alrstd;
			}	
			alrstd = alrstd + f-fp + s[i]-'0';
		}

		cout<<"Case #"<<tt-t<<": "<<f<<endl;
	}
	return 0;
}
