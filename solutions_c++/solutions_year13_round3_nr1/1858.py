#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

int A[1000001];

bool ncc(string str){
	
	for(int i=0;i<str.size();i++)
		if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u')
			return false;
	return true;
}

int main(){
	
	int T;
	cin>>T;
	for(int testcase=1;testcase<=T;testcase++){
		int n;
		string str;
		cin>>str>>n;
		A[str.size()]=-1;
		for(int i=str.size()-1;i>=0;i--){
			
			A[i]=A[i+1];
			if(str.size()-i>=n&&ncc(str.substr(i,n))){
				A[i]=i+n-1;
			}
		}
		
		long long int result=0;
		
		for(int i=0;i<str.size();i++){
			if(A[i]==-1)
				break;
			result+=str.size()-A[i];
		}
		
		
		cout<<"Case #"<<testcase<<": "<<result<<endl;
		
	}
	return 0;
}
