#include<iostream>
#include<string>
#include<math.h>
using namespace std;

int isPallin(int n)
{
    char s[1000];
    sprintf(s, "%d", n);
    for(int i=0, j=strlen(s)-1; i<j; i++,j--){
	if(s[i] != s[j]) return 0;
    }
    return 1;
}

int main()
{
    int t, a, b, i;
    char s[1000];
    cin>>t;
    for(int c = 1; c<=t; c++){
	int count=0;
	cin>>a>>b;
	for(i=a; i<=b; i++){
	    if(isPallin(i)){
		int j = sqrt(i);
		if(j*j == i){
		    if(isPallin(j)){
			count++;
		    }
		}
	    }
	}
	cout<<"Case #"<<c<<": "<<count<<endl;
    }
    return 0;
}
