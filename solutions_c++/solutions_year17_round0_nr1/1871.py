#include<iostream>
#include<string>
using namespace std;
int main(){
	int TT;
	cin>>TT;
	string s;
	int k;
	for(int T=1;T<=TT;++T){
	        int t=0;
	        cin>>s;
	        cin>>k;
	        int i=0;
	        int c=0;
	        for(i=0;i<s.length()-k+1;++i){
	            if(s[i]=='-'){
	                ++c;
	                for(int j=0;j<k;++j){
	                    if(s[i+j]=='-')
	                        s[i+j]='+';
	                    else if(s[i+j]=='+')
	                        s[i+j]='-';
	                }
	            }
	        }
	        for(;i<s.length();++i){
	            if(s[i]=='-'){
	                c=-1;
	            }
	        }
	        if(c>=0)
		    cout<<"Case #"<<T<<": "<<c<<"\n";
	        else
		    cout<<"Case #"<<T<<": IMPOSSIBLE\n";
	}
	return 0;
}
