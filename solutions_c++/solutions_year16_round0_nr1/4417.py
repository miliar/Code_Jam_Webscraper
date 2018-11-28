#include "stdio.h"
using namespace std;

int main(){
	FILE *fp,*out;
	fp = fopen("A-large.in","r");
	out = fopen("Counting Sheep.txt","w");
	int T,N,temp,temp1,count,Nr;
	fscanf(fp,"%d",&T);
	for(int tc=0;tc<T;++tc){
		bool arr[10],sleep = false;
		fscanf(fp,"%d",&N);
		Nr = N;
		printf("%d\n",N);
		if(N==0){
			fprintf(out,"Case #%d: INSOMNIA\n",tc+1);
//			cout<<"Case #"<<tc+1<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		for(int i=0;i<10;++i){
			arr[i] = false;
		}
		while(!sleep){
			temp = N;
			count = 0;
			while(temp > 0){
				temp1 = temp%10;
				arr[temp1] = true;
				temp/=10;
			}
			for(int i=0;i<10;++i){
				if(arr[i]==true)
					++count;
			}
//			printf("%d %d\n",N,count);
			if(count == 10){
				sleep = true;
				break;
			}
			N+=Nr;
		}
		fprintf(out,"Case #%d: %d\n",tc+1,N);
	}

}
