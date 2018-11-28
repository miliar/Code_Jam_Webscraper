#include <iostream>
#include <cstring>
using namespace std;

int calculate(char* str);
void flip(char* str,int i);
void swap(char& a,char& b){
	a = a+b;
	b = a-b;
	a = a-b;
}
int main(){
	int T;
	char str[100];
	cin >> T;
	const int t = T;
	while(T--){
		cin >> str;
		cout << "Case #" << t-T << ": " <<  calculate(str) << endl;
	}
	return 0;
}

void flip(char* str,int i){
 for(int j=0;j<i/2;j++){
 	swap(str[j],str[i-j]);
 }
 for(int j=0;j<=i;j++){
 	str[j] = str[j]=='+'?'-':'+';
 }
}

int calculate(char* str){
  int n = 0,l=strlen(str);
  char temp = str[0];
  for(int i=0;i<l-1;i++){
  	if(temp!=str[i+1]){
  		flip(str,i);
  		n++;
  		temp = str[i+1];
  	}
  }
  return str[l-1]=='+'?n:n+1;
}