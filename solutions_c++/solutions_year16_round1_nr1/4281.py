#include <iostream>
#include <list>
using namespace std;

int main() {
	int t;
	string s;
	char fc;
	cin>>t;
	for(int j=1; j<=t; j++){
	    cin>>s;
	    list<char> c;
	    fc =s[0];
	    c.push_front(fc);
	    for(int i=1; i<s.size(); i++){
	        //cout<<s[i]<<" ";
	        //cout<<fc<<" pos: ";
	        if(s[i]<fc){
	            c.push_back(s[i]);
	            //cout<<"back"<<endl;
	        }
	        else{
	            c.push_front(s[i]);
	            fc=s[i];
	            //cout<<"front"<<endl;
	        }
	    }
	    cout<<"Case #"<<j<<": ";
	    list<char>::iterator i;
	    for(i=c.begin(); i != c.end(); ++i)cout<<*i;
	    cout<<endl;
	    
	}
	return 0;
}
