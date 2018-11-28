
#include <fstream>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");

int cases, pallendromes;
string low, high;

string pallendrome[100000];

void GOGOGO(string &temp, int pos, int stop, int remaining, bool CanYouEven){
	if(stop-pos < remaining || remaining < 0) return;
	if(remaining==0 && pos == stop){
		pallendrome[pallendromes] = temp;
		for(int i = temp.size() - !CanYouEven -1; i >= 0; i--){
			pallendrome[pallendromes] += temp[i];
		}
		pallendromes++;
	}else{
		temp[pos] = '1';
		for(int i = pos+1; i <= temp.size(); i++){
			GOGOGO(temp,i,stop,remaining-1,CanYouEven);
		}
	}
	for(int i = pos; i < stop; i++) temp[i] = '0';
}

bool coolCompare(string a, string b){
	if(a.size() == b.size()) return a < b;
	return a.size() < b.size();
}

string square(string num){
	string aa = "";
	for(int i = 0; i < num.size() * 2 - 1; i++){
		aa += '0';
	}
	for(int i = 0; i < num.size(); i++){
		for(int j = 0; j < num.size(); j++){
			aa[num.size()-1+j-i] += (num[i]-'0')*(num[j]-'0');
		}
	}
	return aa;
}

bool awesomeCompare(string a, string b){
	// square
	a = square(a);
	//cout<<a<<"   :   "<<b<<"\n";
	if(a.size() != b.size()) return a.size() < b.size();
	return a < b;
}

bool awesomeCompare2(string a, string b){ // return true for equality.
	// square
	a = square(a);
	//cout<<a<<"   :   "<<b<<"\n";
	if(a.size() != b.size()) return a.size() < b.size();
	return a <= b;
}

int main(){
	cin>>cases;
	// just GENERATE EVERYTHING!
	for(int i = 2; i <= 25; i++){
		string temp = "";
		for(int j = 0; j < i; j++) temp += '0';
		for(int k = 1; k <= 4; k++){
			
			GOGOGO(temp,0,i,k,true);
			GOGOGO(temp,0,i,k,false);
		}
		temp[0] = '2';
		GOGOGO(temp,i-1,i,1,false);
		GOGOGO(temp,i,i,0,true);
		GOGOGO(temp,i,i,0,false);

		temp[i-1] = '2';
		for(int k = 1; k <= 3; k++){
			GOGOGO(temp,0,i-1,k,false);
		}
	}
	pallendrome[pallendromes++] = "1";
	pallendrome[pallendromes++] = "2";
	pallendrome[pallendromes++] = "3";
	pallendrome[pallendromes++] = "11";
	pallendrome[pallendromes++] = "22";
	sort(pallendrome,pallendrome+pallendromes,coolCompare);


	// actually accually accurately solve the problems

	for(int c = 1; c <= cases; c++){
		cin>>low>>high;
		int lb = lower_bound(pallendrome,pallendrome+pallendromes,low, awesomeCompare) - pallendrome;
		int ub = lower_bound(pallendrome,pallendrome+pallendromes,high, awesomeCompare2) - pallendrome - 1;
		
		cout<<"Case #"<<c<<": "<<ub-lb+1<<"\n";
	}


	system("pause");
}