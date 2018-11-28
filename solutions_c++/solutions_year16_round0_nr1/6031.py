#include<iostream>
#include<cstdio>
#define gc getchar
using namespace std;

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

int main(){

	freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

	int test,n,count,i,x,d,t=0;
	scanint(test);
	while(t<test){
		scanint(n);
		int digits[10] = {0};
		count=10;
		i=1;
		x=n;
		while(count && x!=0){
			d = x%10;
			x=x/10;
			 if(digits[d]==0){
			 	digits[d]=1;
			 	count--;
			 }
			if(x==0 && count){
				i++;
				x=i*n;
			}
		}
		if(!count)
			cout<<"Case #"<<t+1<<": "<<i*n<<endl;
		else
			cout<<"Case #"<<t+1<<": "<<"INSOMNIA"<<endl;

		t++;
	}

return 0;
}
