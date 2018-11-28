#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;




int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		string inp;
		cin>>inp;
		int num,den;
		string n="",d="";
		bool found =false;
		for(int x=0;x<inp.length();x++){
			if(inp[x]=='/'){
				found = true;
				continue;
			}
			if(!found){
				n+=inp[x];
			}
			else d+=inp[x];
		}
		const char* a = n.c_str();
		const char* b = d.c_str();
		num = atoi(a);
		den = atoi(b);
		int res=1;
		int loop=1;
		bool imposs = false;
		int y = den;
		bool done= false;
		while(true){
			 if(((y % 2) == 0) && y > 1){ /* While x is even and > 1 */
				y /= 2;
				
				if(y<=num && !done) {res = loop;done=true;}
				if(y==num) {break;}
				loop++;
			}
			else if(y==1) break;
			else if(y%2==1) {
				imposs = true;
				break;
			}
		}
		if(!imposs) {
			cout<<"Case #"<<i+1<<": "<<res<<endl;
		}
		else cout<<"Case #"<<i+1<<": "<<"impossible"<<endl;
		
	}
}
