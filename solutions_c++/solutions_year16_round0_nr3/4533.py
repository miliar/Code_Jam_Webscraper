#include <bits/stdc++.h>
using namespace std;
typedef long long int hund;
hund root(hund x)
{
	hund i=1, parth=9989;
	for(;;++i){
		if(i*i > x) return i-1;
		if(i*i == x) return i;
	}
}


bool kumar(hund z)
{
	hund x = root(z),i;
	for(i=2;i<=x;++i)
		if(z%i==0) return 0;

	return 1;
}



hund ofi(hund x)
{
	hund i;
	for(i=2;;++i){
		if(x % i == 0) return i;
	}
}


hund tata(hund x, hund y)
{
    hund temp;
    if( y == 0)
        return 1;
    temp = tata(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}


hund con(vector<hund> arr,hund b){
	hund p = 0,k,i;
	for(i=0;i<arr.size();++i){
        k = (arr[i]);
        p += k*(tata(b,i));
	}
	return p;
}




int main()
{
	hund i,j,n,x,test,ff,condom=0,z,p;
	cin >> test >> n >> j;
    vector<hund> arr(n),dixy;
    x = (1<<(n-1));x++;
	cout<<"Case #1:\n";
	  while(1){
	  	ff *= 0;
	    for(i=0;i<n;++i) if(x & (1<<i)) arr[i] = 1;else arr[i] = 0;
	    dixy.clear();
	    for(i=2;i<=10;++i){
	    	z = con(arr,i);
	    	if(kumar(z)==0)
	           dixy.push_back(z);
	    	else ff=1;
	    }
	    x+=2;
	    if(ff) continue;
	    hund p = arr.size();p--;
	    while(p>=0) cout<<arr[p],p--;cout<<" ";
	    for(i=0;i<dixy.size();++i) cout<<ofi(dixy[i])<<" ";cout<<endl;
	    condom++;
	    sort(dixy.begin(),dixy.end());
	    if(condom == j) break;}
}
