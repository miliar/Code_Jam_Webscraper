#include "QuaternionNumber.h"
#include "QuaternionString.h"
#include "string_repeat.h"
#include <iostream>
#include <string>
#include <cassert>
using std::string;
using std::cin;
using std::cout;
using std::endl;

int main(){
	int T;
	cin>>T;
	for (int i=0;i<T;i++){
		int L;
		int X;
		cin>>L;
		cin>>X;
		string is;
		cin>>is;
		assert(is.size()==L);
		string rs = repeat(is,X);
		QuaternionString qs(rs);
		assert(qs.size()==L*X);
		int split1=0;
		int split2=1;
		if (qs.size()>=2)
		while (split1<qs.size() && split2<qs.size()){
			if (qs.multiply(0,split1-1)==QI&&qs.multiply(split1,split2-1)==QJ && qs.multiply(split2,qs.size()-1)==QK){
				break;
			}
			split2++;
			if (split2>=qs.size()){
				split1++;
				split2=split1+1;
			}
		}
		cout<<"CASE #"<<i+1<<": "<< ((split2<qs.size())?"YES":"NO")<<endl;
	}
}
