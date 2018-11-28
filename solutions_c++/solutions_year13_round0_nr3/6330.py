#include <iostream>
#include <string>
#include <fstream>
#define SIZE 1001

using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("output.txt");

int n;

int a,b;
int cnt;

int palindrome(char *buff)
{
	int len=0;
	len = strlen(buff);
	if(len == 1) return 1;


	for(int k =0;k<len/2;k++){
		if(buff[k] != buff[len-k-1]){
			return 0;
		}
	}

	return 1;
}

int sq(int num)
{
	if(num == 1) return 1;

	for(int k=1;k<=num/2;k++){
		if(k*k == num) return k;
		if(k*k > num) return 0;
	}

	return 0;
}

void run(int m)
{
	char str[1001];
	char str2[1001];
	int pp=0;
	itoa(m,str,10);

	if(palindrome(str)){ //palüũ

		//squareüũ
		pp = sq(m);
		if(pp != 0){
			itoa(pp,str2,10);
			if(palindrome(str2)){
			cnt++;
			}
		}
	}

}

void main()
{
	int i,j;
	fin >> n;
	for(i=0;i<n;i++){
		fin >> a >> b;
		cnt=0;
		for(j=a;j<=b;j++){
			run(j);
		}

		fout << "Case #" << i+1 <<": "<< cnt << endl;;
	}
}