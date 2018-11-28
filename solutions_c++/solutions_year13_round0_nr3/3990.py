#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void setup();
bool palindrome(long long int n);
long long int reversenum(long long int num);

long long int i;
int j;
int xx=1;
long long int z;
long long int x;
long long int y;
int T;

vector <long long int> palsquares(10000);
vector <int> answer(10001);
int main(){
	setup();
	
	FILE *fin = fopen ("C-large-1.in","r");
	fscanf(fin, "%d",&T);
	ofstream out("C-large-1.out");
	for(i=1;i<=T;i++){
	fscanf(fin, "%lld",&x);
	fscanf(fin, "%lld",&y);

		for(j=1;j<50;j++){
			z=palsquares[j];
			if(palsquares[j]>=x && palsquares[j]<=y){
				answer[i]++;
			}
		}
		out << "Case #" << i << ": " << answer[i] << endl;
	}
	

	return 0;

}


void setup()
{
long long int ii;
	for(i=0;i<=10000000;i++){
		if(palindrome(i)){
			ii=i*i;
			if(palindrome(ii)){
				palsquares[xx]=ii;
				xx++;
			}
	
		}
	}

}
bool palindrome(long long int n)
{
	
	z=reversenum(n);
	if(n==z){
		return 1;
	}
	return 0;
}

long long int reversenum(long long int num)
{
        long long int inv= 0;

        while (num>0)
        {
                inv = inv * 10 + (num%10);
                num = num/ 10;
        }

        return inv;
}
