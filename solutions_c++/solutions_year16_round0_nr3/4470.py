#include <bits/stdc++.h>
using namespace std;
typedef long long int li;

li root(li x)
{
	li i=1;
	for(;;++i){
		if(i*i > x) return i-1;
		if(i*i == x) return i;
	}
}


bool isprime(li z)
{
	li x = root(z),i;
	for(i=2;i<=x;++i){
		if(z%i==0) return 0;
	}
	return 1;
}



li fac(li x)
{
	li i;
	for(i=2;;++i){
		if(x % i == 0) return i;
	}
}


li power(li x, li y)
{
    li temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}


li con(vector<li> arr,li b){
	li p = 0,k,i;
	for(i=0;i<arr.size();++i){
        k = (arr[i]);
        p += k*(power(b,i));
	}
	return p;
}




int main()
{
    vector<li> sieve(100000,1);
	li i,j,n,x,test,ff,cc=0,z,p;
	for(i=2;i<=100000;++i){
		if(sieve[i]==0) continue;
		for(j=2;i*j<100000;++j){
			sieve[i*j]  = 0;
		}
	}
	cin >> test >> n >> j;
	puts("Case #1:");
    vector<li> arr(n),dac;
    x = (1<<(n-1));x++;

      for(;;x+=2){
      	ff = 0;
        dac.clear();
        for(i=0;i<n;++i){
        	if(x & (1<<i)){
               arr[i] = 1;
        	}
        	else{
        		arr[i] = 0;
        	}
        }
        for(i=2;i<=10;++i){
        	z = con(arr,i);
        	if(isprime(z)==0){
               dac.push_back(z);
        	}
        	else ff=1;
        }
        if(ff) continue;
        cc++;
        li p = arr.size();p--;
        for(;p>=0;--p) cout<<arr[p];cout<<" ";
        for(i=0;i<dac.size();++i){
        	cout<<fac(dac[i])<<" ";
        }
        cout<<endl;
        if(cc == j) break;
        
    }
}