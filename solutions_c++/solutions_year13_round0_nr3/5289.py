#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;

bool is_palind(int n){
	stringstream stm;
	string str;
	stm<<n;
	str=stm.str();
	int i,sz;
	sz=str.size();
	for(i=0;i<sz;i++)
		if(str[i] != str[sz-i-1])
			return false;
	
	return true;
}

int is_sq(long n){
	int one = n%10;	
	if(one == 0 || one == 1 || one == 4 || one == 6 || one == 9 || one == 5){
		double sqt=sqrt(n);
	
		if(ceil(sqt)==floor(sqt))
			return (int)sqt;
	}else
		return -1;
}

int main(){
	int i,j,ncses,c_n=1;
	long n1,n2;
	int sqt;
	long count;
	cin>>ncses;
	while(ncses-->0){
		count=0;
		cin>>n1>>n2;
		for(i=n1;i<=n2;i++){
			if(is_palind(i))
				if((sqt=is_sq(i))!=-1)
					if(is_palind(sqt))
						count++;
		}
		cout<<"Case #"<<c_n++<<": "<<count<<endl;
	}
	return 0;
}
