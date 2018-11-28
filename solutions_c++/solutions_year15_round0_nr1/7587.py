	#include <iostream>
	#include <cstring>
	#include <cmath>
	#include <vector>
	#define limit 1000000
	#define ll  long long int 
	using namespace std;

	int main(){
		ll num1,t,i,j,max;
		cin>>t;
		ll total = t;
		ll caseC =0;
		while(t-->0){
			string s;
			cin>>max;
			cin>>s;
			//cout<<max<<"\t"<<s<<"\n";
			int len = s.length();
			long iCount = 0,count=0,totalI=0;
			for(i=0;i<len;i++){
				iCount=0;
				if(s[i]!='0'){
					
					if(count<i){
						iCount = (i-count);
						totalI = totalI + iCount;
					}
				}
				count = count + (s[i]-48);
				if(iCount!=0){
					count = count + iCount;	
				}
			}

			caseC++;
			if(caseC==total){
				cout<<"Case #"<< caseC << ": "<< totalI;
			}
			else{
				cout<<"Case #"<< caseC << ": "<< totalI<<"\n";	
			}
			
		}
		return 0;
	}



