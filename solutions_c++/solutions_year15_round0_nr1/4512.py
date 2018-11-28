#include <iostream> 

using namespace std;

int main ()
{
	int num_test, S;

	cin>>num_test;

	for( int i=0; i< num_test; i++){

	cin>>S;

	string ik;
	cin>>ik;

	int level=0, sol=0, sum=0;  

		for(int k=0; k<=S; k++){
			
			if(ik.at(k)!=0)
			{
				level = k - sum - sol;
				//cout<<"level = "<<level<<" sum = " << sum<< " sol = "<< sol<<" k = "<< k;

				if(level>0){
					sol+=level;
					
				}
			sum+= (int) ik.at(k) -48;
			}
			//cout<<endl;
		}

		cout<<"Case #"<<(i+1)<<": "<<sol<<endl;
	}		
	
	return 0; 
}