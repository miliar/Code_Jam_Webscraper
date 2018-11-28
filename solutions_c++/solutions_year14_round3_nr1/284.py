
#include <iostream>
// For strings			#include <string>
#include <fstream>
// For setprecision 	#include <iomanip>
// For getchar() 		#include <cstdio>
// For Rand, atoi       #include <cstdlib>
// For srand(time(NULL))#include <time.h>
// For built in sort, others #include <algorithm>
#include <string>
#include <vector>
// For clock            #include <ctime>
//For Binary Tree sets,multisets -  #include<set>
// For lists			#include<list>
//For queues  			#include<queue>
//For stacks  			#include<stack>
//For pairs				#include<utility>
//For maps 				#include<map>
//INCLUDE EVERYTHING #include<bit/stdc++.h>
using namespace std;

unsigned long long int gcd(unsigned long long int a, unsigned long long int b){
	if(a==0) return b;
	else if(b==0) return a;
	else if(a==1) return 1;
	else if(b==1) return 1;
	else if(a==b) return a;
	else if(a>b) return gcd(b,a%b);
	else return gcd(a,b%a);
}
int isPowerOf2(unsigned long long int a){
	int power = 0;
	while(true){
		if(a == 0) return power;
		if(a == 1) return power;
		else if (a % 2 != 0) return -1;
		else {
			power ++;
			a /= 2;
		}
	}
}

int main(){
	int tstCases;		
	cin>>tstCases;	
	for(int tst = 1; tst <= tstCases; tst++){
		string pByQ,ps,qs;
		cin>>pByQ;
		int pos = pByQ.find('/');
		ps = pByQ.substr(0,pos);
		qs = pByQ.substr(pos+1);
		//cout<<ps<<" : "<<qs<<endl;
		unsigned long long int p = 0,q = 0,g;
		
		for(int i=0;i<ps.length();i++){
			p = 10*p;
			p += ps[i] - '0';
		}

		for(int i=0;i<qs.length();i++){
			q = 10*q;
			q += qs[i] - '0';
		}
		//cout<<p<<" :: "<<q<<endl;

		g = gcd(p,q);
		p = p/g;
		q = q/g;
	
		cout<<"Case #"<<tst<<": ";
		int power = isPowerOf2(q);
		if(power != -1){
			double rat = 1.0 ,r = (double) p*1.0/q*1.0;
			int ans = 0;

			while(true){
				if(rat <= r) break;
				rat /= 2.0;
				ans ++;
			}
			cout<<ans;
		}else{
			cout<<"impossible";
		}
		cout<<endl;
	}

}
//speed up process: ios_base::sync_with_stdio(true/false);

/*
STRING
string s;
getline(cin,s); or cin>>s;(cin doesnt allow spaces)
s.substr(startpos, lenght);
s.find(char/string, startpos);
s.length();
*/

/*
FSTREAM
ofstream fo;
ifstream fi;
fi.open("input.in");
fo.open("output.in");

fo.close();
fi.close();
*/
/*ESTIMATING TIME FOR THE PROGRAM TO RUN
		clock_t startClock,finishClock;
		double timeCount;
		startClock = clock();
			//Write YOur Code Here.... include ctime,time.h
		finishClock = clock();
		timeCount = finishClock - startClock ;
		//cout<<timeCount<<endl;
*/
/*
SETTING THE NUMBER OF DECIMALS TO BE PRINTED:
cout<<fixed;
cout<<setprecision(10)<<variable;
*/

/*
INPUTTING AN EMPTY VALUE
getchar();
*/

/*
BUILT IN SORT
	#include <algorithm>
	bool myCompare(type a, type b){
		return a<b; //correspondingly to the type the condition for a to be before b
	}
	//myCompare optional
	vector <type> v;
	sort(v.begin(), v.end(), <OPTIONAL : myCompare>);
	//or list.sort(OPTIONAL FUNCTION);
*/
/*Rth Rank ELEMENT:Randomised and PIVOTISE, SWAP
void swapVectorPos(vector<int> &v, int i, int j){
	//O(1): Modifies Original array
	int tmp = v[i];
	v[i] = v[j];
	v[j] = tmp;
	return;
}
int pivotise(vector<int> &v, int pivotPos){
	//Usage : pivotise(v,10);
	//O(n): Modifies original array
	int f = 0, b = v.size() - 1;
	swapVectorPos(v,0,pivotPos);
	while(f < b){
		if(v[f+1]<=v[f]){
			swapVectorPos(v,f,f+1);
			f++;
		}
		else{
			if(v[b] > v[f]) b--;
			else {
				swapVectorPos(v,f+1,b);
				swapVectorPos(v,f,f+1);
				f++;
				b--;
			}
		}
	}
	return f;
}

//RANDOMISED ALGORITHM:
int rthRank(vector<int> a, int r){
	//Use srand,rand...
	int sz = a.size();
	int pivot = rand()%sz;
	int pivotf = pivotise(a,pivot);
	if(a.size() == 1) return a[0];
	if(pivotf == r) return a[pivotf];
	else if(pivotf < r){
		vector<int> compressed(sz - pivotf - 1);
		for(int i=0;i<compressed.size();i++)compressed[i] = a[i + pivotf+1];
		return rthRank(compressed,r - pivotf-1);
	}
	else{
		vector<int> compressed(pivotf);
		for(int i=0;i<pivotf;i++)compressed[i] = a[i];
		return rthRank(compressed,r);
	}
}*/
/*
MERGESORT usage:- a = mergesort(a,size); // a is the array of "int" of length "size";

int* merge(int a[],int m, int b[],int n){
	int* c = new int [m+n];
	int i=0,j=0;
	while(i<=m&&j<=n){
		if(i==m&&j==n) return c;
		else if(i==m)	
			{
			for(int k=m+j;k<m+n;k++){
					c[k]=b[k-m];}
					j=n;}
		else if(j==n)
		{
			for(int k=n+i;k<m+n;k++){
					c[k]=a[k-n];}
					i=m;}
		else if(a[i]<b[j]){
			c[i+j] = a[i]; i++;}
		else {
			c[i+j] = b[j]; j++;}
	}
}

int* mergesort(int* a, int n){
	if(n!=1)
	{
	int m = n/2, p = n - m;
	int* b =  new int [m];
	int* c =  new int [p];
	for(int i=0;i<m;i++){
		b[i] = a[i];
	}
	for(int i=0;i<p;i++){
		c[i] = a[i+m];
	}
	return merge(mergesort(b,m),m,mergesort(c,p),p);
	}
	else return a;
}

*/

/*
A random list of integers limited by max

#include <ctime>
#include <cstdlib>
void randomList(int* a, int n, int max=1000){
		srand (time(NULL));
		for(int i=0;i<n;i++){
			a[i] = rand()%max;
		}
		return;
}

*/

/*
long long int nCr(long long int n, long long int r){
	long long int div,result = 1, denom = 1;
	for(int i=1;i<=n-r;i++){
		result *=r+i;
		denom *= i;
		div = gcd(result,denom);
		result /= div;
		denom /= div;
	}
	return result;
}
*/
/*
unsigned long long int gcd(unsigned long long int a, unsigned long long int b){
	if(a==0) return b;
	else if(b==0) return a;
	else if(a==1) return 1;
	else if(b==1) return 1;
	else if(a==b) return a;
	else if(a>b) return gcd(b,a%b);
	else return gcd(a,b%a);
}
*/
/*
unsigned long long int factors(unsigned long long int n){
	unsigned long long int tc = 1, count =1,fac = 2;
	while(n!=1){
		if(n%fac==0){
			n /= fac;
			count++;
		}
		else{
			tc *= count;
			count = 1;
			fac++;
		}
	}
	tc *= count;
	return tc;
}*/
/*
INVERSE MODULO b

long long int inverse(long long int a, long long int b){
	long long int m = b;
	long long int x = 0, y = 1, lx = 1, ly = 0,X,Y,q,A,B,Lx,Ly;
	while(b!=0){
		q = a/b;	
		A = a;
		B = b;	
		a = B;
		b = A%B;	
		X = x;
		Lx = lx;
		Y = y;
		Ly = ly;	
		x = Lx - q*X;
		lx = X;	
		y = Ly - q*Y;
		ly = Y;
	}
	if(lx < 0) lx += m;
	return lx;	
}

*/

/* LOG TIME MODULAR EXPONENTIATION

long long int logexp(long long int  a,long long int n,long long int &mod){
	if(n==0)  return 1;
	else if(n==1) return a%mod;
	long long int x = logexp(a,n/2,mod);
	if(n%2==0) return ((x%mod)*(x%mod))%mod;
	else if(n%2==1) return (a*((x%mod)*(x%mod))%mod)%mod;
}

*/
/*
int inversionPairs(vector<int> &a,int i, int j){
	//!STATUARY WARNING!//
	//THIS WILL SORT THE VECTOR AS A SIDE EFFECT!!//
	//Usage: inversionPairs(a,0,a.size()-1);//
	if(i >= j) return 0;
	int res = 0;
	int sz = j - i + 1;
	res += inversionPairs(a,i,(i+j)/2);
	res += inversionPairs(a,(i+j)/2+1,j);
	
	vector<int> v(sz);
	
	int k1=0,k2=0;
	for(int k=0;k<sz;k++){
		if(k2 + (i+j)/2 + 1 > j){
			v[k] = a[k1 + i];
			k1++;
			res += k2;
		}
		else if(k1 + i > (i+j)/2){
			v[k] = a[k2 + (i+j)/2+1];
			k2++;
		}
		else if(k1+i <= (i+j)/2 && a[k1+i] <= a[k2 + (i+j)/2+1]){
			v[k] = a[k1 + i];
			k1++;
			res += k2;
		}
		else{
			v[k] = a[k2 + (i+j)/2+1];
			k2++;
		}
	}
	for(int k=0;k<sz;k++) a[k+i] = v[k];
	
	return res;
}
*/
/*
pair<double,double> solveQuad(long long int a, long long int b, long long int c){
	double d = sqrt(b*b - 4*a*c);
	return make_pair((-b + d)/(2*a),(-b - d)/(2*a));
}

bool isInt(double d){
	return d==floor(d);
}
*/
/*
SHUFFLE A VECTOR : Requires SwapVectorPos and  random related libraries
void shuffle(vector <int> &a){
	srand(time(NULL)); //requires time.h
	for(int i=1;i<a.size();i++){
		int swap = rand()%(i+1); //requires cstdlib
		swapVectorPos(a,i,swap);
	}
	return;
}
*/
