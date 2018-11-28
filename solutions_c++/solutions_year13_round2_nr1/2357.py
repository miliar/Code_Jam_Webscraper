
#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>

using namespace std; 


struct sid{
	double pos;
	double speed;
	int line;
	int fixed;
};

struct tid{
	double t;
	int m;
	int n;
};

//large to small, structure
int compareS1(const void *arg1, const void *arg2) {
	if(( (*(sid *)arg1).pos < (*(sid *)arg2).pos ))
		return 1;
	else if(( (*(sid *)arg1).pos > (*(sid *)arg2).pos ))
		return -1;
	else
		return 0;
}
//qsort((void *)si, count, sizeof(sid), compareS1);


//small to large, structure
int compareS2(const void *arg1, const void *arg2) {
	if(( (*(tid *)arg1).t > (*(tid *)arg2).t ))
		return 1;
	else if(( (*(tid *)arg1).t < (*(tid *)arg2).t ))
		return -1;
	else
		return 0;
}
//qsort((void *)ti, count, sizeof(tid), compareS2);

//small to large, double
int compareD(const void *arg1, const void *arg2) {
	if(( *(double *)arg1 > *(double *)arg2 ))
		return 1;
	else if(( *(double *)arg1 < *(double *)arg2 ))
		return -1;
	else
		return 0;
}
//qsort((void *)dary, count, sizeof(double), compareD);

//small to large, long
int compareL(const void *arg1, const void *arg2) {
	if(( *(double *)arg1 > *(double *)arg2 ))
		return 1;
	else if(( *(double *)arg1 < *(double *)arg2 ))
		return -1;
	else
		return 0;
}
//qsort((void *)dary, count, sizeof(long), compareL);

//small to large, long long
int compareLL(const void *arg1, const void *arg2) {
	if(( *(long long *)arg1 > *(long long *)arg2 ))
		return 1;
	else if(( *(long long *)arg1 < *(long long *)arg2 ))
		return -1;
	else
		return 0;
}
//qsort((void *)dary, count, sizeof(long long), compareLL);





//Greatest Common Divisor, if a or b is equal or less than 0, return -1
int Gcd(int a, int b)
{
	if(a<=0||b<=0)
		return -1;
		
	while(a!=b){
		if (a>b)
			a=a-b;
		else
			b=b-a;
	}
	return a;
}



#define MAX_LEN	1024

//get token length
int gettokenlen(char* str){
	int i;
	for(i=0;i<MAX_LEN;i++){

		if(str[i]==' '||str[i]=='\t')
			return i+1;

		if(str[i]=='\n'||str[i]=='\0')
			return i;
	}
	return 0;
}


long long A=0;
long long N=0;
long long Ni[101];
long long bb[101];


long long getcount(int n){
	int i;

	long long sum=0;

	for(i=n+1;i<N;i++){
		sum+=bb[i];
	}
	sum+=N-n-1;

	return sum;
}

long long transfer(){
	int i=0,j=0,k=0;
	int m=0,n=0;
	long long aa;
	long long mm;

	long long res=0;

	qsort((void *)Ni, N, sizeof(long long), compareLL);

	for(i=0;i<101;i++){
		bb[i]=0;
	}

	aa=A;
	for(i=0;i<N;i++){
		if(aa>Ni[i]){
			aa+=Ni[i];
		}
		else{
			if(aa>1){
				aa+=(aa-1);
				bb[i]++;
				i--;
			}
			else{
				bb[i]=N-i;
			}
		}
	}
	for(i=0;i<N-1;i++){
		mm=getcount(i);
		if(bb[i]<=mm&&bb[i]<N-i){
			res+=bb[i];
		}
		else{
			res+=(N-i);
			break;
		}
	}
	if(i==N-1){
		if(bb[i]>=1)
			res++;
	}




	return res;
}

int main() {
	long i=0,j=0,k=0;
	int T;
	long long res=0;

	char str[MAX_LEN];
	char *ps;

	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!

	fstream fin("A-small-attempt1.in", ios::in);
	fstream fout("result.txt", ios::out);


	fin >> T;
	fin.getline(str,1024);
	ps=str;

	for (i=0;i<T;i++){

		fin>>A;
		fin>>N;
		fin.getline(str,1024);
		ps=str;

		for(j=0;j<N;j++){
			fin>>Ni[j];
			//fin>>lr;
		}
		fin.getline(str,1024);
		ps=str;

		res=transfer();

		//double precision
		//fout.setf(ios::fixed);
		//fout.precision(6);

		fout << "Case #" << i+1 << ": " << res << endl;
	}



	return 0;
}
