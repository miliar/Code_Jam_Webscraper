#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,l,i,j;
	char s[1000],max;
	FILE *input, *output;
	input=fopen("A-large.in","r");
	if(input==NULL){
		printf("ERROR");
		exit(0);
	}
	output=fopen("output.txt","w");
	if(output==NULL){
		printf("ERROR");
		exit(0);
	}
	fscanf(input,"%d",&t);
	for(j=1;j<=t;j++){
		vector<char> v;
		fscanf(input,"%s",s);
		l=strlen(s);
		max=s[0];
		v.push_back(max);
		for(i=1;i<l;i++){
			v.push_back(s[i]);
			if(s[i]>=max){
				max=s[i];
				v.erase(v.begin()+i);
				v.insert(v.begin(),max);
			}
		}
		fprintf(output,"Case #%d: ",j);
		for(i=0;i<l;i++){
			fprintf(output,"%c",v[i]);
		}
		fprintf(output,"\n");
	}
return 0;
}

