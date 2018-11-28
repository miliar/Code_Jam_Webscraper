#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

int main(){
	int test,k,c,s,min,temp,i=1;
	ull pos,aux;
	cin >> test;
	while(i<=test){
		cin >> k >> c >> s;
		cout << "Case #" << i << ": ";
		if(c==1){
			if(k!=s)
				cout << "IMPOSSIBLE" << endl;
			else{
				for(int j=1; j<=k; j++)
					cout << j << " ";
				cout << endl;
			}
		}
		else{
			temp = k;
			min = (k/2) + (k%2);
			pos = 0;
			aux = 0;
			if(min>s)
				cout << "IMPOSSIBLE" << endl;
			else{
				while(temp>0){
					if(temp == 1){
						cout << pos+aux+1;
						break;
					}
					cout << pos+aux+2 << " ";
					pos += 2*k;
					if(temp/4 == 0 && temp%4 == 3)
						cout << pos << " ";
					else if(temp >= 4)
						cout << pos+aux+4 << " ";
					temp -= 4;
					aux += 4;
					pos += 2*k;
				}
				cout << endl;
			}
		}
		i++;
	}
	
	return 0;
}