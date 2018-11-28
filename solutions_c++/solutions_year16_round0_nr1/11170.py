#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include<iostream>
#include<vector>
#include<math.h>
#include <stdio.h>
using namespace std;
vector<int> v;
long long a,b,c,insize,final,size,i,j,carry;
bool first;

int chk(long long x);
int main(){
	
	freopen("A.in", "r", stdin);
    freopen("OutputA.txt", "w", stdout);

	long long N,nxt,temp,T;

	cin>>T;
	for(long long k = 1; k <= T; k++){
		size = 0;
		i = 1;
		cin>>N;
		first = true;
		if(N == 0){
			cout<<"Case #"<<k<<": INSOMNIA"<<endl;
		}
		else{
			while(size!=10){
				
				temp = N*i;
				size = chk(temp);
				i++;
			}
			cout<<"Case #"<<k<<": "<< final<<endl;	
		}
		v.clear();
	}
	fclose(stdout);
return 0;
}

int chk(long long x){
	j = 1;
	//check no. of digits
	while(1){
		if(x < int(pow(10,j))){
			break;
		}
		j++;
	}

	long long Y = x;
	long long power;
	while(j){
		power = int(pow(10, j-1));
		if(j==1){
			carry = 0;
		}
		else{
			carry = Y / power;
		}
		if(carry==0){
			//append x%10;
			if(!(find(v.begin(),v.end(),Y%10)!=v.end())){
				v.push_back(Y%10);
			}
		}
		else{
			//append x/pow(10, j-1)
			if(!(find(v.begin(),v.end(),carry)!=v.end())){
				v.push_back(carry);
			}
		}
		Y = Y - carry * power;
		j--;
		//ex. 5076 -> 76 not 076
		if(Y < int(pow(10,j-1))){
			if(!(find(v.begin(),v.end(),0)!=v.end())){
				v.push_back(0);
			}
			j--;
		}
	}


	insize = v.size();
	if(insize==10){
		final = x;
	}
	return insize;
}


   