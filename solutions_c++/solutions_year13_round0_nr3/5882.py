#include<iostream>
#include<stdio.h>
using namespace std;
main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("myfile.txt","w",stdout);
	int line;
	int harf;
	int nice[5]={1,4,9,121,484};
	int puan=5;
	int yer,i,j,k;
	scanf("%d", &line);
	for(j=0;line>j;j++)
		{
			scanf("%d", &harf);
			if(harf>1) puan--;
			if(harf>4) puan--;
			if(harf>9) puan--;
			if(harf>121) puan--;
			if(harf>484) puan--;
			scanf("%d", &harf);
			if(harf<1) puan--;
			if(harf<4) puan--;
			if(harf<9) puan--;
			if(harf<121) puan--;
			if(harf<484) puan--;
			cout<<"Case #"<<j+1<<": ";
			printf("%d", puan);
			if((j+1)!=line)
			cout<<endl;
			puan=5;
		}
return 0;
}
