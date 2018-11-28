#include<iostream>
#include<math.h>
using namespace std;

void takeinput();
int fair_square(int);
bool palindrome(int);
bool square(int);

int t;
int ab_array[100][2];

int main()
{
takeinput();
	for(int i=0;i<t;i++){
		int no=fair_square(i);
		cout<<"Case #" <<i+1 <<": " <<no <<endl;
	}
return 0;
}

bool square(int n)
{
double sq_root=sqrt(n);
	if( (sq_root-int(sqrt(n))==0) && palindrome(int(sqrt(n))) )
		return true;
return false;
}

bool palindrome(int n)
{
int save=n;
int new_no=0;
	while(n!=0){
	int last=n%10;
	new_no=10*new_no+last;	
	n=n/10;	
	}
	if(new_no==save)
	return true;
return false;
}

int fair_square(int cas)
{
int begin=ab_array[cas][0];  
int end=ab_array[cas][1];
int no=0;
	for(int i=begin;i<=end;i++){
		if(palindrome(i)){
			if(square(i))
				++no;
		}
	}
return no;
}

void takeinput()
{
cin>>t;
	for(int i=0;i<t;i++){
		cin>>ab_array[i][0];
		cin>>ab_array[i][1];
	}
}
