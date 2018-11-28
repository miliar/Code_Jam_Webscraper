#include <bits/stdc++.h>
using namespace std;
int main() {
	long long int t,i,j,d,temp,mincount,premax,divs,minreq,k,ttp;
	ifstream if1;
    if1.open("B-large.in");
	if1>>t;
	vector<long long int> da;
	vector< vector<long long int> > dva;
	for(i=0;i<t;i++){
        if1>>ttp;
        da.push_back(ttp);
        vector<long long int> ttpd;
        for(j=0;j<da[da.size()-1];j++){
            if1>>ttp;
            ttpd.push_back(ttp);
        }
        dva.push_back(ttpd);
	}
	if1.close();

	ofstream of;
    of.open("output2.txt");

	for(i=0;i<t;i++){
		d=da[i];
		vector<long long int> a;
		premax=0;
		for(j=0;j<d;j++){
			temp=dva[i][j];
			a.push_back(temp);
			if(max(premax,temp)==temp){
				premax=temp;
			}
		}
		mincount=0;
		for(j=1;j<=premax;j++){
			minreq=0;
			divs=0;
			for(k=0;k<a.size();k++){
				if(j>=a[k]){
					minreq=max(minreq,a[k]);
				}
				else{
					if(a[k]%j==0){
						divs+=a[k]/j-1;
					}
					else{
						divs+=a[k]/j;
					}
					if(j==max(minreq,j)){
						minreq=j;
					}
				}
			}
				if(j==1||(minreq+divs)==min(minreq+divs,mincount)){
					mincount=minreq+divs;
				}
				//cout<<j<<" "<<divs<<" "<<minreq<<"\n";
		}
		of<<"Case #"<<i+1<<": "<<mincount<<"\n";
	}
	of.close();
	return 0;
}
