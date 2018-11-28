#include<iostream>
#include<sstream>
#include<cstring>
#include<fstream>
#include<cmath>
using namespace std;

long long isPalindrome(long long);
long long isSquare(long long);
stringstream ss;
ifstream File("C-small-attempt0.in");
ofstream oFile("output.io");
int main(){
	int i,k;
	long long a,b,n,cnt=0;
	File>>n;
	for(k=0;k<n;k++){
		cnt=0;
		File>>a>>b;
		for(i=a;i<=b;i++){
			if(isPalindrome(i)){
				if(isSquare(i)){
					if(isPalindrome(sqrt(i)))cnt++;
				}
			}
		}
		oFile<<"Case #"<<k+1<<": "<<cnt<<endl;
	}
    return 0;
}
long long isPalindrome(long long a){
	long long a2;
	string temp,rtemp;
	ss.clear();
	ss<<a;
	ss>>temp;
	rtemp.clear();
	for(int i=0;i<temp.length();i++){
		rtemp+=temp[temp.length()-1-i];
	}
	ss.clear();
	ss<<rtemp;
	ss>>a2;
	return (a==a2);
}
long long isSquare(long long a){
	long long at;
	at=round(sqrt(a));
	return ((at * at) == a);
}
