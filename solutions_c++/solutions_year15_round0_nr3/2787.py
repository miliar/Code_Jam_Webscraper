//#include <iostream>
#include <fstream>
#include <string.h>
#include <utility>
using namespace std;
typedef pair<bool,char> quat;

quat solve(quat a, quat b){
	quat ans;
	char s,m;
	ans.first = a.first^b.first;
	ans.second = a.second;
	if(a.second=='i'){
		if(b.second=='i'){
			ans.first=!ans.first;
			ans.second='1';
		}
		else if(b.second=='k'){
			ans.first=!ans.first;
			ans.second='j';
		}
		else if(b.second=='j')
			ans.second='k';
		else
			ans.first^=b.first;
	}
	else if(a.second=='j'){
		if(b.second=='j'){
			ans.first=!ans.first;
			ans.second='1';
		}
		else if(b.second=='k')
			ans.second='i';
		else if(b.second=='i'){
			ans.first=!ans.first;
			ans.second='k';
		}
		else
			ans.first^=b.first;
	}
	else if(a.second=='k'){
		if(b.second=='k'){
			ans.first=!ans.first;
			ans.second='1';
		}
		else if(b.second=='j'){
			ans.first=!ans.first;
			ans.second='i';
		}
		else if(b.second=='i')
			ans.second='j';
		else
			ans.first^=b.first;
	}
	else{
		if(b.second=='i'){
			ans.second='i';
		}
		else if(b.second=='j'){
			ans.second='j';
		}
		else if(b.second=='k')
			ans.second='k';
		else
			ans.first^=b.first;
	}
	return ans;
}

int main(){
	ifstream cin("C-small-attempt1.in.txt");
	ofstream cout("outputC.txt");
	int t,l,x,te,endi,endj,length;
	bool fir,ttt;
	string str,str2;
	quat cur,cur2,cur3;
	cin >> t;
	for(int i=1;i<=t;i++){
		cin >> l >> x >> str2;
		str = "";
		te = endi = endj = ttt = 0;
		fir = true;
		length = l*x;
		cout << "Case #" << i << ": ";
		if(l==1||length<3||(l==3&&x==1&&str2!="ijk")){
			cout << "NO\n";
		}
		else if(l==3&&x==1&&str=="ijk"){
			cout << "YES\n";
		}
		else{
			while(x--)str+=str2;
			cur = quat(0,str[0]);
			while(!te){
				while(cur!=quat(0,'i')||!fir){
					endi++;
					fir = true;
					if(endi>=length-2){
						te=1;
						break;
					}
					else cur = solve(cur,quat(0,str[endi]));
				}
				cur2 = quat(0,str[endi+1]);
				endj = endi+1;
				while(cur2!=quat(0,'j')){
					endj++;
					if(endj>=length-1){
						ttt = 1;
						break;
					}
					else cur2 = solve(cur2,quat(0,str[endj]));
				}
				if(ttt == true){
					ttt = fir = false;
					continue;
				}
				cur3 = quat(0,str[endj+1]);
				for(int j=endj+2;j<length;j++){
					cur3 = solve(cur3,quat(0,str[j]));
				}
				if(cur3==quat(0,'k'))te=2;
				fir=false;
			}
			if(te==1)cout << "NO\n";
			else cout << "YES\n";
		}
	}
}