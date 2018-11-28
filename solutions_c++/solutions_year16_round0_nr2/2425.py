#include <iostream>
#include <vector>
using namespace std;

void flip(vector<int> &v, int last){
	for(int i=0;i<=last/2;++i){
		int temp = v[i];
		v[i] = v[last-i] == 1?-1:1;
		v[last-i] = temp == 1?-1:1;
	}
}

int main(){
	int t;
	int c = 0, l;
	string s;
	cin>>t;
	for(int i=1;i<=t;++i){
		cin>>s;
		c = 0;
		l = s.size();
		vector<int> stack(l);
		for(int j=0;j<l;++j){
			stack[j] = (s[j] == '+')?1:-1;
		}

		int last = l-1;
		while(last){
			if(stack[last] == 1)
				--last;
			else{
				bool b = stack[0] == 1?true:false;
				for(int j=1;j<=last;++j){ // check for equality
					if(!b){
						if(stack[j] == -1) break;
						stack[0] = 1; ++c; b = true;
					}
					else{
						if(stack[j] == -1){
							++c;
							flip(stack, j-1);
							break;
						}
					}
				}
				flip(stack, last);
				++c;
				--last;
			}
		}
		if(stack[last] == -1) ++c;
		cout<<"Case #"<<i<<": "<<c<<endl;
	}
}