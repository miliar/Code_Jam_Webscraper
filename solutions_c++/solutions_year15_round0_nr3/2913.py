#include <bits/stdc++.h>
using namespace std;

char negation(char a){
	if(a=='1')return 'O';
	if(a=='i')return 'I';
	if(a=='j')return 'J';
	if(a=='k')return 'K';
	if(a=='O')return '1';
	if(a=='I')return 'i';
	if(a=='J')return 'j';
	if(a=='K')return 'k';
}

bool neg(char a){
	if(a=='O'||a=='I'||a=='J'||a=='K')return true;
	return false;
}

char posi_mult(char a,char b){
	if(a=='1') return b;
	if(b=='1') return a;
	if(a==b && a=='1')return '1'; 
	if(a==b)return 'O'; 
	if(a=='i'&&b=='j') return 'k';
	if(a=='i'&&b=='k') return 'J';
	if(a=='j'&&b=='i') return 'K';
	if(a=='j'&&b=='k') return 'i';
	if(a=='k'&&b=='i') return 'j';
	if(a=='k'&&b=='j') return 'I';
}

char mult(char a,char b){
	if(a=='1') return b;
	if(a=='O') return negation(b);
	if(b=='1') return a;
	if(b=='O') return negation(a);
	if(neg(a)&&neg(b))return posi_mult(negation(a),negation(b));
	if(!neg(a)&&!neg(b))return posi_mult(a,b);
	if(!neg(a)&&neg(b))return negation(posi_mult(a,negation(b)));
	if(neg(a)&&!neg(b))return negation(posi_mult(negation(a),b));
}

char prod[10000][10000];

int main(){
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		int l,x;
		cin>>l>>x;
		string s;
		cin>>s;
		string tmp=s;
		for(int i=1;i<x;i++){
			tmp+=s;
		}
		s=tmp;
		for(int i=0;i<s.length();i++){
			prod[i][i]=s[i];
			for(int j=i+1;j<s.length();j++){
				prod[i][j]=mult(prod[i][j-1],s[j]);
			}
		}
		/*for(int i=0;i<s.length();i++){
			for(int j=i;j<s.length();j++){
				cout<<prod[i][j]<<" ";
			}
			cout<<endl;
		}*/
		
		bool flag=false;
		bool flag1=false;
		char I='1',J='1',K='1';
		for(int i=0;i<s.length()-2;i++){
			if(prod[0][i]=='i'){
				for(int j=i+1;j<s.length()-1;j++){
					if(prod[i+1][j]=='j'){
						if(prod[j+1][s.length()-1]=='k'){
							flag=true;
							flag1=true;
							break;
						}
					}
				}
				if(flag1)break;
			}
		}
		if(flag)cout<<"Case #"<<t+1<<": YES\n";
		else cout<<"Case #"<<t+1<<": NO\n";
	}
}
