#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define _fora(i,n) for(unsigned long long i = 1; i<n; i++)
#define _for(i,n) for(unsigned long long i = 0; i<n; i++)
#define _forlor(i,n) for(int i=n-1; i>=0; i--)
#define max(a,b) a<b?b:a
#define tmax 10000000

using namespace std;
unsigned long long tab[tmax];
int pal[tmax];
char chifres[20];

vector<unsigned long long> vec;

int ispal( unsigned long long c ) 
{
	int i = 0;
	while(c != 0){
		chifres[i++] = '0' + c%10;
		c = c/10;
	}
	chifres[i]='\0';
	int len  = strlen(chifres);
	_for(j,len/2){
		if(chifres[j] != chifres[len - 1 - j])
			return 0;
	}
	return 1;
}

int main(){
	freopen("in.in", "r", stdin);
	freopen("out.in", "w", stdout);

	tab[0] = 0;

	_fora(i,tmax){
		tab[i] = tab[i-1] + 2*i-1;
		pal[i] = (int) (ispal(tab[i]) + ispal(i))/2;
	}

	int T;
	cin>>T;
	long long a,b;
	_for(t,T){
		cin>>a>>b;
		int i = 0;
		while(tab[i]<a)
			i++;
		int counto = 0;
		while(tab[i] <= b){
			counto = counto + pal[i];
			i++;
		}

		cout<<"Case #"<<(t+1)<<": "<<counto<<endl;
	}

	return 0;
}