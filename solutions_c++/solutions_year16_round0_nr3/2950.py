#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<cmath>
#include<climits>
#include <fstream>
#include <string>
 
using namespace std;
#include <sstream>

template <typename T>
  string NumberToString ( T Number )
  {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }

template <typename Iter>
bool next(Iter begin, Iter end)
{
    if (begin == end)      // changed all digits
    {                      // so we are back to zero
        return false;      // that was the last number
    }
    --end;
    if ((*end & 1) == 0)   // even number is treated as zero
    {
        ++*end;            // increase to one
        return true;       // still more numbers to come
    }
    else                   // odd number is treated as one
    {
        --*end;            // decrease to zero
        return next(begin, end);   // RECURSE!
    }
}

long long convert(string num,int base){
	int k = num.length();
	long long res=0;
	for(int i=k-1;i>=0;i--){
		if(num[i]==0){
			res = res*base;
		}else{
			res = res*base + 1;
		}
	}
	return res;
}

long long int base_decimal(long long int n,long long int base) /* Function to convert binary to decimal.*/
{
    long long int decimal=0, i=0, rem;
    while (n!=0)
    {
        rem = n%10;
        n/=10;
        decimal += rem*pow(base,i);
        ++i;
    }
    return decimal;
}



bool isPrime(long long number){

    if(number < 2) return false;
    if(number == 2) return true;
    if(number % 2 == 0) return false;
    for(long long i=3; (i*i)<=number; i+=2){
        if(number % i == 0 ) return false;
    }
    return true;

}



long findleastf(long long n){
	for(long i=2;i<=sqrt(n);i++){
		if(n%i==0){
			return i;
		}
	}
}




int main(int argc, char const *argv[])
{
	/* code */
	int cases,count =0,flag,pos,k=0,n,j;
	
	ifstream infile;
	//cout<< base_decimal(10101,3);
	infile.open("cs.in");
	infile>>cases;
	ofstream outfile;
   outfile.open("out.txt");
	for(int u=1;u<=cases;u++){
		
		infile>>n>>j;
		outfile<<"Case #"<<u<<":"<<endl;
		string perm(n-2,'0');
		int number=0;
		//for all  permutations
		while(next(perm.begin(),perm.end()) && number<j){
			//cout << perm << endl;
			 flag=0;
			string s = '1' + perm +'1';
			
		for(int base=2;base<=10;base++){
			
			long long ans = base_decimal(stoll(s),base);
			//cout << s << endl;
			if(isPrime(ans)){
				//cout << ans << " prime" <<endl;
				flag=1; 
				break;
			}else{
				;
			}

		}
		//cout<<s<<endl;
		if(flag==0)
			{outfile<<s<<" ";number++;}
		for(int base=2;base<=10;base++)
		if(flag==0){
			long long ans;
			ans = base_decimal(stoll(s),base);
			outfile<<findleastf(ans)<< " ";

		}
		if(flag==0)
		outfile << endl;

	}
		

		}
	outfile.close();
	return 0;
}


