#include <sstream>
#include <iostream>
#include <set>
#include <stdio.h>
using namespace std;

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("D1.out", "w", stdout);

	int T;
	cin>>T;
	for(int caseNumber=1;caseNumber<=T;caseNumber++) {
		int n,y,z;
		cin>>n;
		set<double> a,b,cina,cinb;
		cina.clear();
		cinb.clear();
		for(int i=0;i<n;i++){
			double w;
			cin>>w;
			cina.insert(w);
		}
		for(int i=0;i<n;i++){
			double w;
			cin>>w;
			cinb.insert(w);
		}
		a=cina;
		b=cinb;
		set<double>::iterator itb;
		do{
			set<double>::iterator ita = a.begin();
			double bound=(*ita);
			for (itb = b.begin();itb!=b.end();itb++){
				if(bound<(*itb)){
					a.erase(bound);
					b.erase(*itb);
					break;
				}
			}
		}while(itb!=b.end());
		z=b.size();
		
		
		a=cinb;
		b=cina;

		do{
			set<double>::iterator ita = a.begin();
			double bound=(*ita);
			for (itb = b.begin();itb!=b.end();itb++){
				if(bound<(*itb)){
					a.erase(bound);
					b.erase(*itb);
					break;
				}
			}
		}while(itb!=b.end());
		y=n-b.size();

		printf("Case #%d: ", caseNumber);
		cout<<y<<" "<<z<<endl;
	}
	return 0;
}

