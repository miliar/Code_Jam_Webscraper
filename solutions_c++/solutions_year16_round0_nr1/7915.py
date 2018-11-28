#include <iostream>
#include<cstdio>
using namespace std;
int readInt () {
	bool minu = false;
	int result1 = 0;
	char ch;
	ch = getchar();
	while (true) {
		if (ch == '-') break;
		if (ch >= '0' && ch <= '9') break;
		ch = getchar();
	}
	if (ch == '-') minu = true; else result1 = ch-'0';
	while (true) {
		ch = getchar();
		if (ch < '0' || ch > '9') break;
		result1 = result1*10 + (ch - '0');
	}
	if (minu)
		return -result1;
	else
		return result1;
}
int main() {
	// your code goes here
	int t, N, i = 0, count=0;
	t=readInt();
	int v[10]={0,0,0,0,0,0,0,0,0,0};
	while(i++ < t){
		N=readInt();
		int k=0;
		while(k<10)
		{ v[k]=0;
		  k++;
		}
		if(N == 0){
			cout << "Case #" << i << ": " << "INSOMNIA"<<endl;
			
		}
		else
		{ 
		int all = 0, mlt = 1,  val;
		while(all == 0){ //for loop
			val = N * mlt;
			mlt++;
			while(val > 0){
				v[val%10] = 1;
				val /= 10;
			}
            all = 1;
			for(int m=0; m<10;m++) {
				if(v[m]==0)
                all =0;
                
			}
		}
		
		cout << "Case #" << i << ": " << N*(mlt-1)<<endl;
		
	}}
	return 0;
}