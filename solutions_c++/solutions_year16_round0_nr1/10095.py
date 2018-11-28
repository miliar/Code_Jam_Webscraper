#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int t, a, c;
	scanf("%d", &t);
	for(int o=1; o<=t; o++){
		scanf("%d",&a);
		if(a==0) printf("Case #%d: INSOMNIA\n", o);
		else{
			c = a;
			vector<int>b;
			for(int i=0; i<10; i++)
				b.push_back(0);
			while(b[0]==0 || b[1]==0 || b[2]==0 || b[3]==0 || b[4]==0 || b[5]==0 || b[6]==0 || b[7]==0 || b[8]==0 || b[9]==0){
				string s = to_string(a);
				for(unsigned int j=0; j<s.size(); j++){
					b[s[j]-48]++;
				}
				a+=c;
			}
			printf("Case #%d: %d\n", o, a-c);
		}
	}
	return 0;
}
