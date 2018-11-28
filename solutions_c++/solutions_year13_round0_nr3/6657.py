#include <fstream>

#include <cmath>

using namespace std;

bool isPalindrome(int n){
	 int num=n,rem,sum=0;    
    
   
 
    while(num!=0)
    {
        rem=num%10;
        num=num/10;
        sum=sum*10+rem;
 
    }
    if(n==sum) return true;
    else return false;
}
int main(){
	ifstream in("C-small-attempt0.in");
	ofstream out("C-small-attempt0.out");
	double intpart;
	int n;
	in>>n;
	int answers[n];
	int a, b;
	int count=0;
	double newNum;
	for(int i=0; i<n; i++){
		in>>a>>b;
		for(int k=a; k<=b; k++){
			
			if(isPalindrome(k)){
				
				newNum = sqrt(k);
				
				if (abs(newNum - (round(newNum))) < 0.000000001) 
					if(isPalindrome((int)newNum)){
						//cout<<(int)newNum<<" "<<k<<endl;
						count++;
					} 
			}
		}
		answers[i]=count;
		count=0;
		
	}
	//	Sleep(10000);
	for(int i=0; i<n; i++)
		out<<"Case #"<<i+1<<": "<<answers[i]<<endl;
}
