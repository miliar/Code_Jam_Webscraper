#include <bits/stdc++.h>
#include <ctime>
using namespace std;

int main(){
	// freopen("inputp1.txt","r",stdin);
	// freopen("output.txt","w",stdout);
	//float maxTime = 0;
	//clock_t tot_start = clock(), tot_end;
	int t,j,i;
	map<int, bool> found;
	cin>>t;

	//clock_t start, end;
	for(int c=1;c<=t;c++){
		cin>>i;
		cout<<"Case #"<<c<<": ";
		if(i==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
//		start = clock();
		found.clear();
		for(j=1;found.size()!=10;j++){
			int t = j*i;
			if(t>10000000){
				cout<<"paused : "<<i<<" "<<t<<endl;
				getchar();
			}
			while(t){
				found[t%10]=true;
				if(found.size()==10)
					break;				
				t=t/10;
			}
			if(found.size()==10)
				break;			
		}
		cout<<j*i<<endl;
		//end = clock();
		//maxTime = max(maxTime, (float)(end-start)/CLOCKS_PER_SEC);
	}	
	// tot_end = clock();
	// cout<<"Total time taken = "<<(float)(tot_end-tot_start)/CLOCKS_PER_SEC<<" secs"<<endl;
	// cout<<"Max time for a test case = "<<maxTime<<" secs"<<endl;
	return 0;
}