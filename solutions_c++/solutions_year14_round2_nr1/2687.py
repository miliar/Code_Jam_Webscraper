#include <iostream>
#include <algorithm>
using namespace std;

string s[107],wz;
int n,t,j,k,l,ind,lit[107][107],ile,out;
bool fegla;

int abc(int r){
	if(r<0) return -r;
	return r;
}

void make_wz(){
	int i=0;
	wz.clear();
	while(i<s[0].length()){
		wz.push_back(s[0][i]);
		while(s[0][i]==s[0][i+1] && i<s[0].length()) i++;
		i++;
	}
}

void check_s(){
	for(int i=1;i<n;i++){
		j=0; ind=0;
		while(j<s[i].length()){
			if(s[i][j]!=wz[ind]){ fegla=true; break;}
			ind++;
			int sum=0;
			while(s[i][j]==s[i][j+1] && j<s[i].length()){ j++; sum++; }
			lit[i][ind-1]=sum+1;
			j++;
		}
		if(ind!=wz.length()) {fegla=true; break;}
		if(fegla) break;
	}
}

void zsumuj(){
	j=0; ind=0;
	while(j<s[0].length()){
		ind++;
		int sum=0;
	 	while(s[0][j]==s[0][j+1] && j<s[0].length()){ j++; sum++; }
		lit[0][ind-1]=sum+1;
		j++;
	}

	out=0;
	for(int i=0;i<wz.length();i++){
		int sum=0;
		for(j=0;j<n;j++) sum+=lit[j][i];
		int a=sum % n; int b=n-(sum % n);
		if(a<=b) ile=sum/n;
		else ile=sum/n+1;
		for(j=0;j<n;j++) out+=abc(lit[j][i]-ile);
	}
}
		

int main(){
	cin>>t;
	for(k=0;k<t;k++){
		cin>>n;
		for(int i=0;i<n;i++) cin>>s[i];
		make_wz();
		fegla=false;
		check_s();
		if(!fegla) zsumuj();
		cout<<"Case #"<<k+1<<": ";
		if(fegla) cout<<"Fegla Won"<<endl;
		else cout<<out<<endl;
	}
	return 0;
}
