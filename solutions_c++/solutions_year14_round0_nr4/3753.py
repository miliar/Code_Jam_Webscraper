#include <iostream>
#include <set>
#include<stdio.h>

using namespace std;

int main(){
	freopen("D-large.in","r",stdin);
    freopen("outputlarge.txt", "w", stdout);
    int cases,t=1;
	scanf("%d",&cases);
	while(cases--){
		int n, n1=0, n2=0;
		scanf("%d",&n);
		set<double> s1, s2;
		for(int j=0;j<n;j++){
			double a;
			scanf("%lf",&a);
			s1.insert(a);
		}
		for(int j=0;j<n;j++){
			double a;
			scanf("%lf",&a);
			s2.insert(a);
		}
        set<double>::iterator i1 = s1.begin(), i2 = s2.begin();
		for(int i=0;i<n;i++){
			if(*i1>*i2){
				n1++;
				i2++;
			}
			i1++;
		}
		set<double>::reverse_iterator r1, r2;
		r1 = s1.rbegin();
		r2 = s2.rbegin();

		for(int i=0;i<n;i++){
			if(*r1>*r2)
				n2++;
			else
				r2++;
			r1++;
		}
		cout<<"Case #"<<t<<": "<<n1<<' '<<n2<<endl;
		t++;
	}
return 0;
}

