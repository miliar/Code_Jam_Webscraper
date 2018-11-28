
#include<iostream>
#include<vector>
#include<math.h>
#define ull unsigned long long int
using namespace std;
vector<string> vec;
int n,j;

void generate_string(string str){
	if(str.length()>n) return ;

	if(str.length()==n && str[n-1]=='1')  {
		vec.push_back(str);
		return;
	}
	generate_string(str+'0');
	generate_string(str+'1');


}

ull decimal_number(string str,int base){
	ull ss=1,ans=0;
	for(int p=(n-1);p>=0;p--){
		if(str[p]!='0') ans = ans + ss;
		ss = ss*base;
	}
	return ans;
}

int check_prime(ull temp){
	for(long int i=2;i<=sqrt(temp)+1;i++){
		if(temp%i==0) return 0;
	}
	return 1;
}

void output(ull temp){
	for(long int i=2;i<=sqrt(temp)+1;i++){
		if(temp%i==0) {
			cout<<i<<" ";
			return ;
		}
	}
}
int main(){
        int t;cin>>t;
        for(int tt=0;tt<t;tt++){
                cin>>n>>j;
	        generate_string("1");
	        cout<<"Case #1: "<<endl;
	        for(long int i=0;i<vec.size() && j>0;i++){
	        	int k;
	        	vector<ull> vec1;
	        	for(k=2;k<=10;k++){
	        		ull temp = decimal_number(vec[i],k);
	        		if(check_prime(temp)) break;
		        	else vec1.push_back(temp);
		        }
		        if(vec1.size()==9){
		        	cout<<vec[i]<<" ";
		        	for(int i=0;i<vec1.size();i++) output(vec1[i]);
		        	cout<<endl;
                                j--;
		        }
	        }
        }
        
	return 1;
}
