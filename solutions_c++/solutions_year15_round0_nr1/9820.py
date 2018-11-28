#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<string>
#include<cstring>

using namespace std;

int main()
{
	int T=0,Smax=0;
	int S_input[100]={0};
	int output[100]={0};
	int now=0;

  char input[100]={0};
	scanf("%d",&T);

	for(int i=0;i<T;++i){
		scanf("%d",&Smax);
		scanf("%s",input);
		now=0;
		for(int j=0;j<=Smax;++j){
			if(now<j){
//				cout<<"asdf\n";
				output[i]+=j-now;
				now=j;
			}
			S_input[j]=input[j]-'0';
//			cout<<S_input[j]<<endl;
			now+=S_input[j];
		}
	}

	for(int i=0;i<T;++i){
		printf("Case #%d: %d\n",i+1,output[i]);
	}

	exit(0);
}
