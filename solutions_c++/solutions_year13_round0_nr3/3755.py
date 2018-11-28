#include<fstream>
#include<cmath>
using namespace std;


bool is_Palindrome(int num) {
	 int n,rev = 0;
     n = num;
     do{
		 rev = (rev*10) + (num%10);
         num = num/10;
     }while (num!=0);
	 return n==rev;
}
bool is_fairAndSquare(int num){
	int mSqrt=int(sqrt(double(num)));
	if(mSqrt*mSqrt==num){
	if(is_Palindrome(num)&&is_Palindrome(mSqrt))
			return true;
	}
	else
		return false;
}
int main(){
	ofstream fout ("C-small-attempt0.out");
	ifstream fin ("C-small-attempt0.in");

	int i,t,k;
	fin>>t;
	int n,m;
	int count;
	
		for(k=1;k<=t;k++){
				
				
				fin>>n>>m;
				count=0;
				for(i=n;i<=m;i++)
					if(is_fairAndSquare(i))
						count++;
				
				fout<<"Case #"<<k<<": "<<count<<endl;
				
		}

	return 0;
}