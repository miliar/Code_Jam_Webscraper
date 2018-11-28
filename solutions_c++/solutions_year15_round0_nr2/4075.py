#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	vector<int>hi;
	int t,a,i,j,c,ma,sim,sum,save,ans;
	bool woa;
	ifstream cinn("B-small-attempt7.in");
	ofstream coutt("txt.in");
	cinn>>t;
	for(i=0;i<t;i++) {
		sum=0;
		ans=9999999;
		cinn>>a;
		for(j=0;j<a;j++) {
			cinn>>c;
			hi.push_back(c);
		}
		while(1) {
			ma=save=0;
			for(j=0;j<hi.size();j++) {
				if(ma<hi[j]) {
					save=j;
					ma=hi[j];
				}
			}
			ans=min(ans,sum+ma);
			if(ma>3) {
                if(ma==9) {
                    woa=true;
                    for(j=0;j<hi.size();j++) if(hi[j]>3&&j!=save) woa=false;
                    for(j=0;j<hi.size();j++) if(hi[j]==6) woa=true;
					if(woa) {
                        hi.push_back(3);
                        hi[save]=6; 
                    }
                    else {
                        hi.push_back(5);
                        hi[save]=4;
                    }   
                }
				else {
                    if(hi[save]%2) hi.push_back(hi[save]/2+1);
				    else hi.push_back(hi[save]/2);
				    hi[save] = hi[save]/2;
                }			
				sum++;
			}
			else break;
		}
		coutt<<"Case #"<<i+1<<": "<<ans<<endl;
		hi.resize(0);
	}
}
