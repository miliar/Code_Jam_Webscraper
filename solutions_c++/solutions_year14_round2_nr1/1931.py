#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cstring>
using namespace std;
int main()
{
	int i,t,j,k,l,m,n,A[100],B[100],max;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	string str1,str2,str3,str4;
	for(i = 0; i < t; i++){
		cin>>n;
		cin>>str1>>str2;
		str3 = "";
		str4 = "";
		max = 0;
		l = 0;
		A[0] = 1;
		B[0] = 1;
		str3 += str1[0];
		for(j = 1; j < str1.length(); j++){
			if(str1[j]==str1[j-1])
			A[l]++;
			else{
				l++;
				A[l] = 1;
				str3 = str3+str1[j];
			}
		}
		l = 0;
		str4 += str2[0];
		for(j = 1; j < str2.length(); j++){
			if(str2[j]==str2[j-1])
			B[l]++;
			else{
				l++;
				B[l] = 1;
				str4 = str4+str2[j];
			}
		}
		//cout<<str3<<"  "<<str4<<endl;
		if(str3.compare(str4) == 0){
			for(j = 0; j <= l; j++){
				m = A[j]-B[j];
				if(m<0)
				m*=-1;
				max+=m;
			
			}
			cout<<"Case #"<<i+1<<": "<<max<<endl;
		
		}
		else{
			cout<<"Case #"<<i+1<<": "<<"Fegla Won"<<endl;
			
		}
	
	}
	return 0;
}
