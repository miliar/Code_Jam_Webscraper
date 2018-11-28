#include<iostream>
#include<cmath>

using namespace std;

bool a[64];
int l,an,u;
int t,n;

unsigned long long p (unsigned long long num)
{
    if (num <=1)
        return false;
    else if (num == 2)         
        return 2;
    else if (num % 2 == 0)
        return 2;
    else
    {
        unsigned long long prime = 0;
        unsigned long long max = sqrt(num);
        for(unsigned long long i = 3 ; i < max; i += 2) {
        	
        	if(num % i == 0) {
            	return i;
        	}
   		}
        return prime;
    }
}

void m(){
	int x=1;
	unsigned long long g=0;
	unsigned long long y[11];
	for(int i=2; i<=10; i++){
		g=0;
		//cout<<"       "<<l;
		for(int j=l;j>=0;j--){
			if(a[j]){
				g+=pow(i,j);
			}
		}
		y[i]=p(g);
		if(!y[i]){
			x=0;
			//cout<<i<<"  "<<g<<endl;
			break;
		}
	}
	
	if (x==1){
		an++;
		
		for(int j=l;j>=0;j--){
			cout<<a[j];
		}
		for(int j=2;j<11;j++){
			cout<<" "<<y[j];
		}
		cout<<endl;
	}
}

void b(unsigned long long x){
	a[0]=1;
	for (l=1 ; l<n-1; l++){
		a[l]=x%2;
		x/=2;	
	}
	a[l]=1;
}

int main(){
	unsigned long long a;
	int j;
	cin>>t;
	
	for (u=1; u<= t; u++){
		
		an=0;
		cin>>n>>j;
		a=pow(2,(n-2));
		cout<<"Case #"<<u<<": \n";
		for (unsigned long long k=0; k<a; k++){
				b(k);
				m();
				
				if(an>=j){
					break;
				}
			}
	}
	
	return 0;
}
