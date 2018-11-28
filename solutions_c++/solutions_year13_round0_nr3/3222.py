//Karol Rozycki
#include<cstdio>
#include<string>
#include<sstream>
#include<vector>
#include<algorithm>
#define MAX 1010
using namespace std;

vector<long long int> V;

bool is_palindrome(int x){
	stringstream ss;
	ss << x;
	string number = ss.str();
	int len = number.length();
	for(int i=0;i<len;i++){
		if(number[i]!=number[len-i-1]){
			return false;
		}
	}
	return true;
}

int main(){
	long long int si=1e7;si++;
	for(int i=0;i<=si;i++){
		if(is_palindrome(i)&&is_palindrome(i*i)){
			V.push_back(i*i);
		}
	}
	int z;
	scanf("%i",&z);
	for(int g=1;g<=z;g++){
		long long int a,b;
		scanf("%lli %lli",&a,&b);
		printf("Case #%i: %lli\n",g,(long long int)(upper_bound(V.begin(),V.end(),b)-lower_bound(V.begin(),V.end(),a)));
	}
	return 0;
}


