#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int i,t,n,j,count1,count2,maxd,temp,prev,tp1;
	ifstream if1;
    if1.open("A-large.in");
	if1>>t;
	vector<long long int> na;
	vector<vector<long long int> >  mna;
	for(i=0;i<t;i++){
        vector<long long int> emp;
        if1>>temp;
        for(j=0;j<temp;j++){
            if1>>tp1;
            emp.push_back(tp1);
        }
        na.push_back(temp);
        mna.push_back(emp);
	}
    if1.close();
	ofstream of;
    of.open("output.txt");
	for(i=0;i<t;i++){
		n=na[i];
		count1=0;
		count2=0;
		vector<long long int> a;
		maxd=0;
		for(j=0;j<n;j++){
			temp=mna[i][j];
			a.push_back(temp);
			if(j!=0){
					maxd=max(maxd,(prev-temp));
					if(prev>=temp){
						count1+=(prev-temp);
					}
			}
			prev=temp;
		}
		for(j=0;j<n-1;j++){
			if(j!=n-1){
					count2+=min(maxd,a[j]);
			}
		}



		of<<"Case #"<<i+1<<": "<<count1<<" "<<count2<<"\n";
	}
	of.close();
	return 0;
}
