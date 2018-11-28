#include<iostream>
#include<stdio.h>
#include<cstring>
#include<cstdio>
#include<stdlib.h>
#include<sstream>
#include<list>
#include<math.h>
#include<map>
#include<set>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<fstream>
#include<vector>
#include<algorithm>
#include <queue>
#include<string>
#include<cstring>
#include <deque>
#include<stack>
using namespace std;


#define ALL(a) a.begin(),a.end()
#define CLR(a) memset(a,0,sizeof(a))
#define PB push_back
#define PI acos(-1.0)
#define SET(a) memset(a,-1,sizeof(a))
#define ALL_BITS ((1 << 31) - 1)
#define NEG_BITS(mask) (mask ^= ALL_BITS)
#define TEST_BIT(mask, i) (mask & (1 << i))
#define ON_BIT(mask, i) (mask |= (1 << i))
#define OFF_BIT(mask, i) (mask &= NEG_BITS(1 << i))
#define max3(a,b,c) max(a,max(b,c))
#define min3(a,b,c) min(a,min(b,c))
long long GCDFast(long long a,long long b){   while(b)b^=a^=b^=a%=b;  return a;   }
#define MOD 1000000007
#define MX 100010
#define pii pair<int,int>
#define LL long long
// UP, RIGHT, DOWN, LEFT, UPPER-RIGHT, LOWER-RIGHT, LOWER-LEFT, UPPER-LEFT
int dx[8] = {-1, 0, 1, 0, -1, 1,  1, -1};
int dy[8] = { 0, 1, 0,-1,  1, 1, -1, -1};

int digits[20],totalCount =0;
long long numbers[20];
#define N 200000002

bool prime_number[N];
long long prime_num[11078937];
int size;
void prime()
{
	int i = 0 ,limit = (int)sqrt((double)N), x = 0,j = 0,y;
	memset(prime_number,true,sizeof(prime_number));
	for(x = 2 ; x <= limit; x++)
	{
		if(prime_number[x] == true)
		{
			y = N/x;
			for(i = 2 ; i <= y ;i++)
				prime_number[i*x] = false;
		}
	}
		for(x = 2,i = 0 ; x <= N; x++)
		if (prime_number[x])
		{
			prime_num[i] = x;
			i++;	
		}
		size = i;
}
void calculatePrimeFactor(){
	for(int base =2; base<=10 ;base++){
		for(int i = 0 ; i <size; i++)
		if (numbers[base]%prime_num[i] == 0){
			cout<<prime_num[i]<<" ";
			break;
		}
	}
}

bool checkPrime(){
	long long x,y,flag =1,num;
	for(int base =2; base<=10 ;base++){
		if(numbers[base] <= 200000000){
			if(prime_number[numbers[base]] )//prime
			return false;
		}else{
				flag = 1;
				num = numbers[base];
				y= (int)sqrt((double)num)+1;
				if(y>200000000)
					return false;
				for(x = 0 ; x < size; x++){ 
					if( (num % prime_num[x] == 0) ){
						flag=0;//not prime but others are not sure yet
						break;
					}
				}
				if(flag)//prime  number
				return false;
		}
	}
	return true;
}

void baseConv(){
	long long i , number=0,flag = 1;
	for(int base =2; base<=10 ;base++){
		number = 0;
		for(i = 0;i < 16 ;i++){
			if(digits[i])
			number+=digits[i]*(long long)pow( (double)base,(double)(15-i) );
		}
		numbers[base] = number;
	}
	
	if (checkPrime()){
		totalCount++;
		for(i=0;i<16;i++)
			cout<<digits[i];
		cout<<" ";
		/*for(i=2;i<=10;i++)
			cout<<numbers[i]<<" ";
		cout<<"\n";*/
		calculatePrimeFactor();
		cout<<"\n";
	}
}

void calculateJamCoin()
{
    int i,n = 16,mask;
	
	for(mask=0; mask < (1<<n);mask++){
		memset(digits, 0 ,sizeof digits);
		if(totalCount == 50)
			break;
		for(i=0;i<n;i++){
		if(mask & (1<<i))
			digits[i] = 1;	
		else if( i == 0 || i == n-1)
			break;
		}
		if(i == n){
		baseConv();
		}
	}
	
    
}
int main()
{
	long long flag = 0,n,i=0,j,x,y,m,input,ans,testcase;
	int T=0,index;
	long long sum = 0,temp;
	freopen ("d:/Codejam/C-small-attempt2.in","r",stdin);
	freopen ("d:/Codejam/C-small-attempt2.out","w",stdout);
	//cin>>testcase;
	string str;
	long long number=0;
	
	
	//while(false){
	{
		cin>>n>>x>>y;
		printf("Case #%d:\n",++T);
		prime();
		calculateJamCoin();
		
		//cout<<ans<<"\n";
	}
	
	return 0;
}
