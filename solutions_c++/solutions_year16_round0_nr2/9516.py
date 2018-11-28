#include <bits/stdc++.h>



using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef queue<int> qi;
typedef queue<ii> qii;
typedef long long ll;


char flip(char a){
	if(a == '+')
		return '-';
	return '+';

}
string voltis(string s, int pos){

	for (int i = 0; i < (pos+1)/2; ++i)
	{
		
		char aux = s[i];
		s[i] = flip(s[pos-i]);
		s[pos-i] = flip(aux);
		
	}
	if((pos)%2==0){
		s[pos/2] = flip(s[pos/2]);
	}

	return s;
}
typedef map<string,int> mp;
typedef queue<string> qs;
mp mapa, resultados;
qs pan;
bool yaExiste(string s){
	if(mapa.find(s)!= mapa.end())
		return true;
	return false;
}
bool yaTermino(string s){
	for (int i = 0; i < s.size(); ++i)
	{
		if(s[i]!='+')
			return false;
	}
	return true;
}
 
int findPosChange(string s){
	char ini = s[0];
	for (int i = 1; i < s.size(); ++i)
	{
		if(s[i] == ini) continue;
		return i;
	}
	//no hay cambios
	return -1;
}
int result;
int Find(string s){


	for (int i = 0; i < s.size(); ++i)
	{
		if(yaTermino(s)) return result;
		int p = findPosChange(s);
		if(p == -1) p = s.size();
		s = voltis(s,p-1);
		result++ ;
	}
}
int main()
{
	int T;
	cin>>T;
	int CT = T;
	resultados = mp();
	while(T--){
		string S;
		cin>>S;
		cout<<"Case #"<<(CT-T)<<": ";
		result = 0;
	
		Find(S);
		cout<<result<<endl;
	}
	return 0;
}