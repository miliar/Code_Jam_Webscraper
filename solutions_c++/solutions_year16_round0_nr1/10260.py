#include<bits/stdc++.h>
 using namespace std;


#define gc getchar_unlocked

void scanint(long long &x)
{
    register long long  c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}


void collect_digits(std::vector<int>& digits, unsigned long num) {
    if (num > 9) {
        collect_digits(digits, num / 10);
    }
    digits.push_back(num % 10);
}




int main() 
{

int t;
cin>>t;
int q=t;
while(t>0){
	t--;
	long long n;
	scanint(n);
		std::vector<long long>a;

	for(int i=0;i<10;i++)a.push_back(i);

long long  j=1;
long long  y=n;

if(n==0){cout<<"Case #"<<q-t<<":"<<"INSOMIA\n";goto label;}

	while(a.size()!=0 && n<=INT_MAX){
		std::vector<int> v;
		collect_digits(v,n);
		for(int i=0;i<v.size();i++){
			long long k=v[i];
			if( std::find(v.begin(), v.end(), k) != v.end()){
					a.erase(std::remove(a.begin(), a.end(), k), a.end());
			}
		}
		j++;
		n=y*j;

	}

	cout<<"Case #"<<q-t<<":"<<y*(j-1)<<endl;
	label:cout<<"";
}
return 0;
}