#include<bits/stdc++.h>
using namespace std;
int main(){
	FILE *f=fopen("inp.txt","r");
	FILE *f1=fopen("out.txt","w+");
	int t;
	fscanf(f,"%d",&t);
	for(int te=1;te<=t;te++){
		long long int n;
		fscanf(f,"%lld",&n);
		fprintf(f1,"Case #%d: ",te);
		if(n==0){
               fprintf(f1,"INSOMNIA\n");
		} else {
			long long int n1=n;
			bool v[10];
			memset(v,false,sizeof(v));
			int c=0;
			while(c<10){
			    long long int x=n;
	            while(x>0){
	                if(v[x%10]==false) 
	                	c++;
	                v[x%10]=true;x/=10;
			    }
			    n+=n1;
			}
			fprintf(f1,"%lld\n",n-n1);
		}
	}
	return 0;
}