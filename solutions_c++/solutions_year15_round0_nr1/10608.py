#include<iostream>
using namespace std;

class standingOvation {


	public:
		void 	solve()
		{
			int testcases;
			cin>>testcases;
			long *solu = new long[testcases];
			for(int i = 0 ; i < testcases ; i++){
				int smax;
				cin>>smax;
				int *input = new int[smax+1];
				char in;
				for(int j=0;j<=smax;j++){
					cin>>in;
					input[j] = in - '0';
				}
				int sum=input[0] ,  minfrnds=0;
				for(int k = 1; k <=smax;k++){
					if( k >= sum && input[k] >0 ){
						minfrnds +=(k-sum);
						sum +=minfrnds;
					}
					sum +=input[k];

				}
				//cout<<"Case #:"<<i+1<<" "<<minfrnds<<"\n";
				solu[i] = minfrnds;
			}

			for(int i = 0 ; i < testcases ; i++)
			{
				cout<<"Case #"<<i+1<<": "<<solu[i]<<"\n";
			}
		}
};

int main(){
	standingOvation *so = new standingOvation;
	so->solve();
}
