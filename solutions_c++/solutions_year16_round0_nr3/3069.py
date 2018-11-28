#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
class sol{
private:
bool* primes;
vector<int> prime;
public:
sol(){
//1-33333333
//primes=new bool[33333333];
//3 5 7-33333333
primes=new bool[16666666];
for(int i=0;i<16666666;i++){
	primes[i]=true;
}
long long now=1;
for(int i=0;i<16666666;i++){
	now+=2;
	if(primes[i]){
		prime.push_back(now);
		for(long long j=now*now;j<=33333333;j+=2*now){
			primes[(j-1)/2-1]=false;
		}
	}
}
}
~sol(){
delete []primes;
}
string checkCJ(int num){
	long long now;
	string result="";
	for(int i=8;i>=0;i--){
		bool isp=true;
		now=convert(num,i);
		if(now%2==0){
			isp=false;
			result+=" 2";
		}
		else{
		for(int v:prime){
			if(v>=now)
				break;
			if(now%v==0){
				isp=false;
				result+=" "+to_string(v);
				break;
			}
		}
		}
		if(isp)
			return "";
	}
	return to_string(now)+result;
}
long long convert(int n,int op){
	int base;
	switch(op){
		case 0:base=10;break;
		case 1:base=9;break;
		case 2:base=8;break;
		case 3:base=7;break;
		case 4:base=6;break;
		case 5:base=5;break;
		case 6:base=4;break;
		case 7:base=3;break;
		default:return n;
	}
	long long result=1;
	long long b=base;
	n>>=1;
	while(n){
		result+=(n&1)*b;
		b*=base;
		n>>=1;
	}
	return result;
}
string to_string(long long v){
	string result="";
	while(v){
		result=char('0'+(v%10))+result;
		v/=10;
	}
	return result;
}
};
int main(){
ifstream is("C-small-attempt1.in");
ofstream os("Output.txt");

sol s;
int num,n,j;
is>>num;
for(int i=1;i<=num;i++){
	is>>n>>j;
	os<<"Case #"<<i<<":\n";
	int minv=(1<<n-1)+1;
	int maxv=0x7FFFFFFF>>(31-n);
	int count=0;
	while(count<j){
		string str=s.checkCJ(minv);
		if(str!=""){
			os<<str<<"\n";
			count++;
		}
		minv+=2;
	}
}
is.close();
os.close();
}