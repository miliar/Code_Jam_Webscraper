#include <iostream>
#include<cmath>
#include <fstream>
using namespace std;

int main(void) {
	  ifstream cin("A-small-attempt0.in");
    ofstream cout("humble.out");
    int k;
    cin>>k;
	for(int i=0;i<k;++i){
		int time[17]={0}, que[16]={0},f=0, a, b, one[16],two[16];
		cin>>a;
        for(int j=0;j<16;++j) cin>>one[j];
		cin>>b;
		for(int j=0;j<16;++j) cin>>two[j];
		for(int j=0;j<4;++j) {time[one[j+4*(a-1)]]++;time[two[j+4*(b-1)]]++; }
		for(int j=1;j<=16;++j) if(time[j]==2) que[f++]=j;
		if(f==1)
			cout<<"Case #"<<i+1<<": "<<que[0]<<endl;
		else if(f>1)
		cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
		else 
			cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
    }
	return 0;
}
