#include <iostream>
#include <stdlib.h>

using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

long int c[26];
int a[1000];

int main(){
	long long int i,j,l,t,n,x;
	string s;
	cin>>t;
	for(x=1;x<=t;x++){

		for(i=0;i<26;i++)
			c[i]=0;

		cin>>s;
		l = s.length();

		for(i=0;i<l;i++){
			c[s[i]-'A']++;
		}

		j=0;
		i=0;
		cout<<"Case #"<<x<<": ";
		while(j<l) {
			if(c[6]>0 && c[8]>0 && c[4]>0 && c[7]>0 && c[19]>0){
				a[i++]=8;
				c[6]--; c[8]--; c[4]--; c[7]--; c[19]--;
				j+=5;
			}	
			else if(c[25]>0 && c[4]>0 && c[17]>0 && c[14]>0){
				a[i++]=0;
				c[25]--; c[4]--; c[17]--; c[14]--;
				j+=4;
			}	
			else if(c[22]>0 && c[19]>0 && c[14]>0){
				a[i++]=2;
				c[22]--; c[19]--; c[14]--;
				j+=3;
			}
			else if(c[23]>0 && c[8]>0 && c[18]>0){
				a[i++]=6;
				c[23]--; c[8]--; c[18]--;
				j+=3;
			}
			else if(c[20]>0 && c[5]>0 && c[14]>0 && c[17]>0){
				a[i++]=4;
				c[20]--; c[5]--; c[14]--; c[17]--;
				j+=4;
			}
			else if(c[21]>0 && c[5]>0 && c[8]>0 && c[4]>0){
				a[i++]=5;
				c[21]--; c[5]--; c[8]--; c[4]--;
				j+=4;
			}	
			else if(c[18]>0 && c[21]>0 && c[4]>1 && c[13]>0){
				a[i++]=7;
				c[18]--; c[21]--; c[4]-=2; c[13]--;
				j+=5;
			}			
			else if(c[19]>0 && c[17]>0 && c[7]>0 && c[4]>1){
				a[i++]=3;
				c[19]--; c[17]--; c[7]--; c[4]-=2;
				j+=5;
			}			
			else if(c[14]>0 && c[13]>0 && c[4]>0){
				a[i++]=1;
				c[14]--; c[13]--; c[4]--;
				j+=3;
			}			
			else { //if(c[13]>1 && c[8]>0 && c[4]>0){
				a[i++]=9;
				c[13]-=2; c[8]--; c[4]--;
				j+=4;
			}
		}
		qsort (a, i, sizeof(int), compare);
		for(j=0;j<i;j++)
			cout<<a[j];
		cout<<endl;
	}
	return 0;
}