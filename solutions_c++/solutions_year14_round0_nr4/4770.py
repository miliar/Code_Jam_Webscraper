#include<iostream>
#include<algorithm>
using namespace std;

double mi[1005];
double ken[1005];

int main() {
	int T,N;
	int k;
	int i,j;
	cin>>T;
	freopen("output.txt","a",stdout);
	for(k=1;k<=T; k++) {
		cin>>N;
		for(i=0; i<N; i++) {
			cin>>mi[i];
		}
		for(i=0; i<N; i++) {
			cin>>ken[i];
		}
		sort(mi, mi+N);
		sort(ken,ken+N);
		int deceit=0,normal=0;

		int mi_begin = 0, ken_begin =0;
		int mi_end = N-1, ken_end = N-1;
		
		while(mi_begin <= mi_end && ken_begin <= ken_end) {
			if(mi[mi_begin] < ken[ken_begin]) {
				ken_end --;
			} else {
				ken_begin++;
				deceit++;
			}
			mi_begin ++;
		}
		mi_begin = 0, ken_begin =0;
		mi_end = N-1, ken_end = N-1;
		while(mi_begin <= mi_end && ken_begin <= ken_end) {
			if(mi[mi_begin] < ken[ken_begin]) {
				normal ++;
				mi_begin ++;
			}
			ken_begin++;
			//
		}
		cout<<"Case #"<<k<<": "<<deceit<<" "<<N-normal<<endl;


	}
    return 0;
}