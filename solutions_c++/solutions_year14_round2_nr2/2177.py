#include<iostream>
#include<cstring>
#include<bitset>

using namespace std;


int main()
{
	int numTestCases;
	int count = 0;
	int A,B,K;
	cin>>numTestCases;
	
	for(int i = 0; i < numTestCases; i++){
		count = 0;
		cin>>A;
		cin>>B;
		cin>>K;
		
		for(int j = 0 ; j < A ; j++){
			for (int k =0 ; k< B; k++){
				string s1 = bitset< 32 >(j).to_string();
				string s2 = bitset< 32 >(k).to_string();
				int l = 0;
				string s3 = "";
				while(l < s1.length()){
					
					if(s1.at(l) != s2.at(l)){
						s3 = s3 + "0";
					}
					else if(s1.at(l) == '1'){
						s3 = s3 + "1";
					}
					else if(s1.at(l) == '0'){
						s3 = s3 + "0";
					}
					l++;
				}
				
				long res = bitset< 32 >(s3).to_ulong();
				if(res < K){
						count++;
				}
			}
			
		}
	
	
	cout<<"Case #"<<(i+1)<<": "<<count<<"\n";	

	}
	return 0;
	
}


