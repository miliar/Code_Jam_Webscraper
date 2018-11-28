#include <bits/stdc++.h>

using namespace std;

int t;

int main(){
	int c,ans;
	string s;
	cin>>c;
	vector<int>a,tmp,aux;
	bool proof;
	while(c--){
		ans = 0;
		cin>>s;
		for(int i=0;i<s.size();i++)
			if(s[i]=='+')
				a.push_back(1);
			else
				a.push_back(0);		
		while(true){
			proof = true;
			for(int i=0;i<a.size();i++)
				if(!a[i])
					proof = false;
			if(proof)
				break;	
			tmp.push_back(!a[0]);
			for(int i=1;i<a.size();i++)
				if(a[i]==a[0])
					tmp.push_back(!a[i]);
				else
					i = a.size()+1;
			for(int i=tmp.size()-1;i>=0;i--)
				aux.push_back(tmp[i]);
			for(int i=0;i<aux.size();i++)
				a[i] = aux[i];
			ans++;
			tmp.clear();
			aux.clear();
		}
		printf("Case #%d: %d\n",++t,ans);
		a.clear();
	}
	return(0);
}
