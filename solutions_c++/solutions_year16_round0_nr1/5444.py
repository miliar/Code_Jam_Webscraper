#include <bits/stdc++.h>
using namespace std;
typedef long long int li;

li ii;


void up(vector<li> & hash, li n)
{
	while(n != 0){
		hash[n%10] = 1;
		n /= 10;
	}
}

bool cc(vector<li> & hash)
{
	li i;
//	for(i=0;i<=9;++i) cout<<hash[i]<<" ";cout<<endl;
	for(i=0;i<=9;++i){
		if(hash[i] == 0) return 0;
	}
	return 1;
}

void fu()
{
	li n,i=2,m;
	cin >> n; m = n;
	vector<li> hash(10,0);
    if(n==0) {
    	cout << "Case #" << ii <<": ";
    	puts("INSOMNIA");
    }
    else{
    	while(1){
    		up(hash,m);
    		if(cc(hash)){
    			cout << "Case #" << ii <<": ";
    			cout<<m<<endl;
    		    break;
    		}
    		m += n;
  //  		if(m==11)  break;
    		//cout << m <<endl;
    	}
    }
}




int main()
{
	li test;
	cin >> test;
	for(ii = 1; ii<=test;++ii) fu();
}