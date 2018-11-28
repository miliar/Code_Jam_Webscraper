#include <iostream>
#include<conio.h>
#include<string.h>
#include<string>
#include<math.h>

using namespace std;

int checkSquare(double n){
    long int root=(sqrt(n));
    return n == root * root;
}

long int checkPalindrome(long double n) {
	string a= to_string(n);
	long int flag=1;
	long int x=a.length();
	//cout<<x;
	for(long int i=0;i<x/2;i++)
		if(a[i]==a[x-1-i])
			continue;
		else {flag=0;break; }

  return flag;
}

long int check() {
	long int count=0;
	long int A,B;
	cin>>A>>B;
	long int arr[10000];
	long int k=0; 
	for(long int i=A;i<=B;i++)
		if(checkSquare(i))
			arr[k++]=i;
	for(long int i=0;i<k;i++)
		if (checkPalindrome(arr[i])&&checkPalindrome(sqrt((double)arr[i])))
			count++;
	 return count;
	 getch();

}

void main()
{
	long int T;
	cin>>T;
	long int arr[10002];
	for(int i=0;i<T;i++)
		arr[i]=check();
	system("cls");
	for(int i=0;i<T;i++)
		cout<<"Case #"<<i+1<<": "<<arr[i]<<endl;
	getch();

}
