#include<iostream>
#include<set>
using namespace std;
int main(){
int T;
long long N;
cin>>T;
for(int i=0;i<T;++i){
cin>>N;
set<int> digits;
for(int j=0;j<10;++j) digits.insert(j);
if(N==0) cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
else{
	long long k=N;
	while(k<1000000000000000000 && !digits.empty())
	{
	long long l=k;
	set<int>::iterator it;
	while(l>0){
	it=digits.find(l%10);
	if(it!=digits.end()) digits.erase(it);
	l/=10;}
	k+=N;	
	
	
	}
	cout<<"Case #"<<i+1<<": "<<k-N<<endl;	

	}//end of else

}
}
