#include<iostream>
#include<algorithm>
#include<string>

using namespace std;
string a;
int tab[100000];
int result[10];
int main(){
	int index = 0;
	int z = (int)'Z', e = (int)'E', r=(int)'R', t = (int)'T', n = (int)'N', v = (int)'V', g = (int)'G', h = (int)'H', s = (int)'S', i = (int)'I', f=(int)'F', x= (int)'X', u = (int)'U', w = (int)'W', o = (int) 'O';
	while(cin>>a){
		int len = a.size();
		for(int j = 0; j < len; j++){
			tab[(int)a[j]]++;
		}
		result[0] = tab[z];
		tab[e]-=tab[z];
		tab[r]-=tab[z];
		tab[o]-=tab[z];
		tab[z] = 0;
		result[2] = tab[w];
		tab[t]-=tab[w];
		tab[o]-=tab[w];
		tab[w] = 0;
		result[4] =tab[u];
		tab[f] -= tab[u];
		tab[o] -= tab[u];
		 tab[r] -= tab[u];
		 tab[u] = 0;
		 result[6] = tab[x];
		 tab[s]-=tab[x];
		 tab[i]-=tab[x];
		 tab[x] = 0;
		 result[8] = tab[g];
		 tab[e] -= tab[g];
		 tab[i] -= tab[g];
		 tab[h] -= tab[g];
		 tab[t] -= tab[g];
		 tab[g] = 0;
		 result[1] = tab[o];
		 tab[n] -=tab[o];
		 tab[e] -= tab[o];
		 tab[o] = 0;
		 result[3] = tab[r];
		 tab[t] -= tab[r];
		 tab[h] -= tab[r];
		 tab[e] -= tab[r];
		 tab[e] -=tab[r];
		 tab[r] =0;
		 result[7] = tab[s];
		 tab[e] -= tab[s];
		 tab[v] -= tab[s];
		 tab[e] -= tab[s];
		 tab[n] -= tab[s];
		 tab[s] = 0;
		 result[5] = tab[v];
		 tab[i] -= tab[v];
		 tab[e] -= tab[v];
		 tab[f] -=tab[v];
		 tab[v] = 0;
		 result[9] = tab[i];
		 tab[n]-=tab[i];
		 tab[n]-=tab[i];
		 tab[e] -= tab[i];
		 tab[i] = 0; 
		 if(index!=0){
		cout<<"case #"<<index<<": ";
		for(int j = 0; j < 10; j++){
			for(int k = 0; k < result[j]; k++){
				cout<<j;
			}
			result[j] = 0;
		}
		cout<<endl;
		}
		index++;
	}
	return 0;
}
