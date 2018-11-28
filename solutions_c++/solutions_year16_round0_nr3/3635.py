#include <iostream>
#include <math.h>

using namespace std;

int main(){
	long long cases;
	cin>>cases;
	for(long z=0;z<cases;z++){
		cout<<"Case #"<<z+1<<":\n";
		long N,J;
		cin>>N>>J;
		long arr[17],bit[17],curr_count[17],number_j=0;
		for(int i=N-1;i>=0;i--){
			arr[i] = pow(2,i);
			bit[i] = 1;
			curr_count[i] = 1;
		}

		while(number_j<J){
			if(bit[0]==1 && bit[N-1]==1){
				long divisors[10];
				int flag = 1;
				for(int k=2;k<=10;k++)
					divisors[k] = -1;

				for(int k=2;k<=10;k++){
					long long number = 0;
					for(int i=0;i<N;i++){
						number = number + pow(k,i)*bit[i];
					}
					for(long x=2;x*x<=number;x++) {
				        if(number%x==0) {
				            divisors[k] = x;
				            break;
				        }
				    }
				    if(divisors[k]==-1){
				    	flag = 0;
				    	break;
				    }
				}
				if(flag == 1){
					number_j++;
					for(int i=N-1;i>=0;i--){
						cout<<bit[i];
					}
					for(int k=2;k<=10;k++){
						cout<<" "<<divisors[k];
					}
					cout<<"\n";
				}
			}

			for(int i=N-1;i>=0;i--){
				if(i==0)
					bit[0] = (bit[0]+1)%2;
				else{
					if(curr_count[i]==arr[i]){
						curr_count[i] = 1;
						bit[i] = (bit[i]+1)%2;
					}
					else curr_count[i]++;
				}
			}
		}
	}
	return 0;
}