#include<iostream>
#include<deque>
#include<string>
using namespace std;
int main (){
	int x;
	string str;
	cin>>x;
	int check=0;
	int ans=0;
	for(int i=1;i<=x;i++){
		cin>>str;
		deque<char> d;
		for(int j=0;j<str.size();j++){
			d.push_back(str[j]);
			
		}
		d.push_back('+');
		
		check=0;
		ans=0;
		if(d[0]=='+'){
			check=1;
		}
		for(int j=0;j<d.size()-1;j++){
			
			if(d[j]=='-'&&d[j+1]=='+'&&check==0){
				check=1;
				ans++;
				
			}else if(d[j]=='-'&&d[j+1]=='+'&&check==1){
				ans+=2;
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}
