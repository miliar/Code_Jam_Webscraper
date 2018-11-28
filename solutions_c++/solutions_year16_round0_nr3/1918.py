#include <iostream>
#include <fstream>
using namespace std;
//ifstream fin ("C-small-attempt0.in");
//ofstream fout ("C-small-attempt0.out");
ifstream fin ("C-large.in");
ofstream fout ("C-large.out");
long long pow(long long a, long long b) {
	long long x = 1, y = a;
    while(b > 0) {
        if(b&1) {
            x=(x*y);
        }
        y = (y*y);
        b /= 2;
    }
    return x;
}
bool isValid(int c[], int n){
	int i,num=c[0];
	for(i=1;i<n;++i){
		if(i&1){
			num-=c[i];
		}else{
			num+=c[i];
		}
	}
	if(num%11 == 0){
		return true;
	}
	return false;
}
void print(int c[], int n){
	int i;
	for(i=0;i<n;++i){
		fout<<c[i];
	}
	fout<<" 3 2 5 2 7 2 9 2 11\n";
}
int main(){
	int t,n,j,i,k,l,m;
	long long num;
	bool done;
	fin>>t;
	for(i=1;i<=t;++i){
		done=false;
		fin>>n>>j;
		int c[n];
		for(k=0;k<n;++k){
			c[k]=0;
		}
		c[0]=c[n-1]=1;
		k=0;
		fout<<"Case #"<<i<<": \n";
		while(k<j){
			//0 1's
			if(isValid(c,n)){
				print(c,n);
				++k;
				if(k==j){
					done=true;
					break;
				}
			}
			if(done){
				break;
			}
			//2 1's
			for(l=1;l<=n-3;++l){
				c[l]=1;
				for(m=l+1;m<=n-2;++m){
					c[m]=1;
					if(isValid(c,n)){
						print(c,n);
						++k;
						if(k==j){
							done=true;
							break;
						}
					}
					c[m]=0;
				}
				if(done){
					break;
				}
				c[l]=0;
			}
			if(done){
				break;
			}
			//4 1's
			for(l=1;l<=n-5;++l){
				c[l]=1;
				for(m=l+1;m<=n-4;++m){
					c[m]=c[m+1]=c[m+2]=1;
					if(isValid(c,n)){
						print(c,n);
						++k;
						if(k==j){
							done=true;
							break;
						}
					}
					c[m]=c[m+1]=c[m+2]=0;
				}
				if(done){
					break;
				}
				c[l]=0;
			}
			if(done){
				break;
			}
			//6 1's
			for(l=1;l<=n-7;++l){
				c[l]=1;
				for(m=l+1;m<=n-6;++m){
					c[m]=c[m+1]=c[m+2]=c[m+3]=c[m+4]=1;
					if(isValid(c,n)){
						print(c,n);
						++k;
						if(k==j){
							done=true;
							break;
						}
					}
					c[m]=c[m+1]=c[m+2]=c[m+3]=c[m+4]=0;
				}
				if(done){
					break;
				}
				c[l]=0;
			}
			if(done){
				break;
			}
		}
	}
	return 0;
}
