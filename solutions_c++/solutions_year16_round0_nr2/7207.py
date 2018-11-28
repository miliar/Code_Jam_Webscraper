#include <iostream>
#include <string.h>

using namespace std;


int solve(char*);
void flip(char*,int);

int main(int argc, char const *argv[])
{
	
	int n,i;
	int t[100];
	char stack[100][1000];
	cin>>n;
	for(i=0;i<n;i++) {
		cin>>stack[i];
	}
	for(i=0;i<n;i++) {
		cout<<"Case #"<<i+1<<": "<<solve(stack[i])<<endl;
	}

	return 0;
}

int solve(char s[1000]) {
	int i,j,nexti, flips=0;
	int n = strlen(s);
	for(i=0;i<n;i=nexti) {
		for(j=i;s[i] == s[j] && j<n;j++);
		flip(s,j-1); flips++;
		nexti = j;
	}
	if(s[0]=='-') { flip(s,n-1); flips--;}
	return flips;
}

void flip(char s[1000],int n) {
	char t[1000];
	int i;
	for(i=0;i<=n;i++) {
		switch(s[i]) {
			case '-': t[i] = '+'; break;
			case '+': t[i] = '-'; break;
		}	
	} 
	t[i] = '\0';
	strrev(t);
	for(i=0;i<=n;i++) s[i] = t[i];
}