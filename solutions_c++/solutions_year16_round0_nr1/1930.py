#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
int main(){
	vector<bool> isseen(10,false);
	long long int t,x,n;
	cin>>t;
	int numseen = 0;
	int q,r;
	for (int k=1;k<=t;k++){
		//read n
		cin>>n;
		numseen = 0;
		for (int j=0;j<10;j++){
			isseen[j] = false;
		}
		if (n==0){
			//print insomnia
			cout<<"Case #"<<k<<": INSOMNIA"<<endl;
		}
		else{
			for(int i=1;;i++){
				// cout<<i<<endl;
				x = n*i;
				q = x;
				while(q>0){
					r = q%10;
					if (isseen[r]){
						//nothing
					}
					else{
						isseen[r] = true;
						numseen++;
					}
					q = q/10;
				}
				if (numseen>=10){
					cout<<"Case #"<<k<<": "<<x<<endl;
					break;
				}
			}
		}

	}
	return 0;
}