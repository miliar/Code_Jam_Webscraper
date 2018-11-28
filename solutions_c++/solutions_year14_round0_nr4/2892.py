#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main (int argc , char* argv[]){
	ifstream is(argv[1]);
	ofstream os(argv[2]);
	int cases ;
	is >> cases ;
	vector<int> scorewar ;
	vector<int> scoredeceit ;
	for(int i=0;i<cases;i++){
		int num ;
		is >> num ;
		int war = 0 ;
		int deceit = 0 ;
		vector<float> A ;
		vector<float> B ,C ;
		for(int j=0;j<num;j++){
			float temp ;
			is >>temp ;
			A.push_back(temp);
			
		}
		for(int j=0;j<num;j++){
			float temp ;
			is >>temp ;
			B.push_back(temp);
			C.push_back(temp);
		}
		sort(A.begin(),A.end());
	
		sort(B.begin(),B.end());	
		sort(C.begin(),C.end());
		/*for(int j=0;j<num;j++){
			cout<<C[j]<<" ";
		}*/
		for(int j=0;j<num;j++){			
			int Bstart = 0 ;
			bool find = false ;
			while(Bstart<B.size()){
				if(A[j]<B[Bstart]){
					B.erase(B.begin()+Bstart);
					find = true ;
					break ;
				}
				else
					Bstart++;
			}
			if(!find){
				//cout<<"case is "<<cases<<" j is "<<j<<" Bstart is "<<Bstart<<endl ; 
				war++;
				B.erase(B.begin());
			}		
		}
		//cout<<war<<endl ;
		scorewar.push_back(war) ;
		war = 0 ;
		while(A.size()>0){
			float weightB = 0 ;
			int Bstart = 0 ;
			bool find = false ;
			while(Bstart<C.size()){
				if(A[A.size()-1]<C[Bstart]){
					find = true ;
					weightB = C[Bstart] ;					
					break ;
				}
				else{
					//cout<<"case is "<<cases<<" Bstart is "<<Bstart<<endl ;
					Bstart++;
				}
			}
			if(!find){
				weightB = C[0] ;
				int t = 0 ;
				while(A[t]<weightB){
					//cout<<A[t]<<" "<<weightB<<endl ;
					t++;
				}
				deceit++;
				C.erase(C.begin());
				A.erase(A.begin()+t);
			}
			else{	 
				C.erase(C.begin()+Bstart);
				A.erase(A.begin());
			}
		}
		//cout<<deceit<<endl ;
		scoredeceit.push_back(deceit);
		deceit = 0 ;
		os << "Case #"<<i+1<<": "<<scoredeceit[i]<<" "<<scorewar[i]<<endl;
	}
	
	
}
