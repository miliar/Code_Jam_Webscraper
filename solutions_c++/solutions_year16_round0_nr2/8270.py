#include <iostream>
#include <cstring>
#include <cstdlib>

#define swap(x,y){int tmp=x;x=y;y=tmp;}

using namespace std;


void flip(char *str,int length)
{
	for(int i=0;i<length/2;i++){
		swap(str[i],str[length-1-i]);
		if(str[i]=='+')
			str[i]='-';
		else
			str[i]='+';
		
		if(str[length-1-i]=='+')
			str[length-1-i]='-';
		else
			str[length-1-i]='+';
	}
	if(length & 1){
		if(str[length/2]=='+')
			str[length/2]='-';
		else
			str[length/2]='+';
	}
}
int main(){
	char str[110]={'\0'};
	int T;
	int length,l;
	char str_plus[110]={'\0'};
	int noflips=0;
	int rmcount=0,lmcount=0,lpcount=0;
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		cin>>str;
		length=strlen(str);
		for(int j=0;j<length;j++)
			str_plus[j]='+';
		noflips=0;
		l=length;
		for(;l>0;){
			
				if(strcmp(str_plus,str)==0){
					cout<<"Case #"<<tc<<": "<<noflips<<endl;
					break;
				}
				rmcount=0;
				lmcount=0;
				lpcount=0;
				l=0;
				for(int j=length-1;j>=0;j--){
					if(str[j]=='-'){
						l=j+1;
						break;
					}
					
				}
				for(int j=l-1;j>=0;j--)
				{
					if(str[j]=='+')
						break;
					rmcount++;
					
				}
				for(int j=0;j<l;j++)
				{
					if(str[j]=='+')
						break;
					lmcount++;
				}
				for(int j=0;j<l;j++)
				{
					if(str[j]=='-')
						break;
					lpcount++;
				}
				
				if(lmcount>rmcount){
					flip(str,l);
					noflips++;
				}
				else if(lmcount==0 && lpcount<=1){
					flip(str,l-rmcount);
					noflips++;
					
				}
				else if(lpcount > 1)
				{
					flip(str,lpcount);
					noflips++;
				}
				else if(lmcount!=0 || lmcount==rmcount)
				{
					flip(str,lmcount);
					noflips++;
				}
				
		}
		for(int j=0;j<110;j++){
			str[j]='\0';
			str_plus[j]='\0';
		}
		
	}
}