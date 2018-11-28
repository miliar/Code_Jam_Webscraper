#include <bits/stdc++.h>

using namespace std;

string flip(string st, int n)
{
	stack<char> aux;
	for (int i=0; i<n; i++) aux.push(st[i]=='+' ? '-' : '+');

	string out;
	while(!aux.empty()){
		out += aux.top();
		aux.pop();
	} 

	while(out.size()!=st.size()) out+=st[out.size()];

	return out;
}

int main()
{
	int t;
	cin>>t;
	for (int count=0; count<t; count++){
		printf("Case #%d: ", count+1);

		queue<string> fila;
		queue<unsigned long long int> dist;
		set<string> used;

		string ini, fin;
		cin>>ini;
		for (int i=0; i<ini.size(); i++) fin+="+";

		bool found = false;
		fila.push(ini);
		dist.push(0);
		while(!found && !fila.empty()){
			if (fila.front()==fin) found=true;
			else{
				for (int i=0; i<=fila.front().size(); i++) {
					string pu = flip(fila.front(), i);
					if (!used.count(pu)){
						fila.push(pu);
						dist.push(dist.front()+1);
						used.insert(pu);
					}
				}
				fila.pop();
				dist.pop();
			}
		}

		cout<<dist.front()<<endl;
	}
	return 0;
}