#include<iostream>
#include <string>
#include <cstdio>
#include <set>
#include <vector>
#include <math.h>  
using namespace std;
//A very boring & straightforward soln :)

// to get a set of all the possibilities of 0s/1s string
vector<string>poss;
int index, N;
//string arr[16384];

void generate (string s){
	if (s.length()==N-1)
	{
		poss.push_back(s+'1');
		//arr[index++]=s+'1';
		return;
	}

	 generate (s+'0');
	 generate (s+'1');
}

unsigned long long getInterpretation( string s, double base){
	unsigned long long ans=0;
	for( int i=0; i<N; i++){
		if(s[i]=='1')
			ans += pow(base,(N-i-1));
	}
	return ans;
}


unsigned long long Isprime ( unsigned long long n) {

     if (n < 3) {
        return 0;
    }
 
    if (n % 2 == 0){
		return 2;
	}
		
	if( n % 3 == 0) {
        return 3;
    }
 
    for (unsigned long long i = 5; i * i < n; i += 6) {
        if (n % i == 0 ){
			return i;
		}
		else if(n % (i + 2) == 0) {
            return  (i + 2);
        }
    }

    return 0;
}

int main()
{
	
	freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
	int T, J;
	cin>>T;
	for(int i=1; i<=T;i++){
	cin >>N>>J;
	generate("1");
	cout<<"Case #"<<i<<": "<<endl;
	for( int j=0; j< poss.size(); j++){
		if(J==0)
			break;
		unsigned long long divisors [10], div;
		bool flag =false;
		for( int k=2 ; k<=10; k++){
			div=Isprime(getInterpretation(poss[j],k));
			if(div==0)
				goto x;
			divisors[k-1]=div;

		}
		flag = true;
		x:
		if (flag){
			cout<<poss[j]<<" " ;
		for( int k=1 ; k<10; k++)
			cout<<divisors[k]<<" ";
		cout<<endl;
		J--;
		}

	}

	
	
}


	return 0;
}