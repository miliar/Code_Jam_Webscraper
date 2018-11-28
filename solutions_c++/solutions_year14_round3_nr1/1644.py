#include <climits>
#include <iostream>
#include <vector>

using namespace std;


long int gcd(long int a,long int b){
	long int t;
	while(b != 0){
		t = b;
		b = a % b;
		a =t;
	}
	return a;
}

void  testcase(long int casex){
	string s;
	cin>>s;
	long int p=0, q=0;
	long int i=0;
	while(s[i]!= '/'){
		p= p*10+(s[i]-'0');
		i++;
	}
	i++;
	while(s[i]!= '\0'){
		q= q*10+(s[i]-'0');
		i++;
	}
	long int d = gcd(q,p);
	p = p/d;
	q= q/d;
	//cout << p <<"//"<<q<<endl;
	
	int j =0;
	bool test=true;
	while(q>1){
		if(q%2 !=0 ) test = false;
		
		if(q>p)j++;
		q=q/2;
	}
	cout << "Case #"<<casex<<": ";
	if(test && j <41) cout <<j<<endl;
	else  cout <<"impossible"<<endl;
}

int main()
{
	ios_base::sync_with_stdio(false);
	long int cases;
	cin >> cases;
	for(long int i =1; i<=cases;i++){
		testcase(i);  
	}

  return 0;
}
