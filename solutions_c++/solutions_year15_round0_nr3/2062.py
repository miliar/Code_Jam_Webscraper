#include<cstdio>
#include<cstdlib>

#include<iostream>

using namespace std;

#define MAXL 10024

int m[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
int str[MAXL];
int pow[8];

int mult(int u, int v){
	return (u/abs(u)) * (v/abs(v)) * m[abs(u)-1][abs(v)-1];
}
int main(){
	int T;
	cin >> T;
	for(int k=0; k<T; k++){
		int L;
		long long X;
		cin >> L >> X;

		int Prod=1;
		for(int i=0; i<L; i++){
			char ch; 
			cin >> ch;
			str[i]=ch-'i'+2;
			Prod=mult(Prod,str[i]);
		}
		pow[0]=1;
		for(int i=1;i<8; i++)
			pow[i]=mult(pow[i-1],Prod);

		cout << "Case #" << (k+1) << ": "; 
		
		if(pow[(X%8)]!=-1){
			cout << "NO\n"; 
			continue;
		}
		
		int p, n, m;
		int yes=0;
		for(m=0; m<8; m++){
			p=1;
			for(n=0; n<L; n++){
				p=mult(p,str[n]);
				if(mult(pow[m],p)==2){
					yes=1;
					break;
				}
			}
			if(yes)
				break;
		}
		int np=n, mp=m;

		if(!yes){
			cout << "NO\n";
			continue;
		}

		yes=0;
		for(m=0; m<8; m++){
			p=1;
			for(n=0; n<L; n++){
				p=mult(str[L-1-n],p);
				if(mult(p,pow[m])==4){
					yes=1;
					break;
				}
			}
			if(yes)
				break;
		}
		if(!yes){
			cout << "NO\n";
			continue;
		}

		np++;
		n++;
		if(np==L){np=0;mp++;}
		if(n==L){n=0;m++;}
		
		int tb=mp+m+(np+n+L-1)/L;
		if(tb <= X)
			cout << "YES\n";
		else
			cout << "NO\n";
	}
}
