#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T, result[100]={}, in1, in2;
	string str;
	cin>>T;
	for(int i=0;i<T;i++) {
		cin>>str;
		in2=str[0];
		for(int j=1;j<str.length();j++) {
			in1=str[j];
			if(in1=='\n') break;
			if(in1!=in2) result[i]++;
			in2=in1;
		}
		if(in2=='-') result[i]++;
	}
	for(int i=0;i<T;i++) {
		cout<<"Case #"<<i+1<<": "<<result[i]<<endl;
	}
    return 0;
}