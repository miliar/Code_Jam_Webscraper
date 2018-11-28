#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define Letra(x) (x-'A')
string Cads[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int Num[]={0,1,2,3,4,5,6,7,8,9};
bool Puede(string s,vector<int> Valid){
	for(int i=0;i<s.size();i++){
		int pos=Letra(s[i]);
		Valid[pos]-=1;
		if(Valid[pos]<0) return false;
	}
	return true;
}
int main(){
	int tc,cp=0;
	string s;
	cin>>tc;
	while(tc--){
		vector<int> V(30,0);
		cout<<"Case #"<<++cp<<": ";
		cin>>s;
		for(int i=0;i<s.size();i++){
			V[Letra(s[i])]+=1;
		}
		string ans="";
		while(V[Letra('Z')]>0){
			V[Letra('Z')]--;
			V[Letra('E')]--;
			V[Letra('R')]--;
			V[Letra('O')]--;
			ans=ans+'0';
		}
		while(V[Letra('X')]>0){
			V[Letra('X')]--;
			V[Letra('S')]--;
			V[Letra('I')]--;
			ans=ans+'6';
		}
		while(V[Letra('W')]>0){
			V[Letra('T')]--;
			V[Letra('W')]--;
			V[Letra('O')]--;
			ans=ans+'2';
		}
		while(V[Letra('U')]>0){
			V[Letra('F')]--;
			V[Letra('O')]--;
			V[Letra('U')]--;
			V[Letra('R')]--;
			ans=ans+'4';
		}
		while(V[Letra('O')]>0){
			V[Letra('O')]--;
			V[Letra('N')]--;
			V[Letra('E')]--;
			ans=ans+'1';
		}
		while(V[Letra('R')]>0){
			V[Letra('T')]--;
			V[Letra('H')]--;
			V[Letra('R')]--;
			V[Letra('E')]--;
			V[Letra('E')]--;
			ans=ans+'3';
		}
		while(V[Letra('T')]>0){
			V[Letra('E')]--;
			V[Letra('I')]--;
			V[Letra('G')]--;
			V[Letra('H')]--;
			V[Letra('T')]--;
			ans=ans+'8';
		}
		while(V[Letra('S')]>0){
			V[Letra('S')]--;
			V[Letra('E')]--;
			V[Letra('V')]--;
			V[Letra('E')]--;
			V[Letra('N')]--;
			ans=ans+'7';
		}
		while(V[Letra('F')]>0){
			V[Letra('F')]--;
			V[Letra('I')]--;
			V[Letra('V')]--;
			V[Letra('E')]--;
			ans=ans+'5';
		}
		while(V[Letra('N')]>0){
			V[Letra('N')]--;
			V[Letra('I')]--;
			V[Letra('N')]--;
			V[Letra('E')]--;
			ans=ans+'9';
		}
		sort(ans.begin(),ans.end());
		cout<<ans<<endl;
	}
	return 0;
}
