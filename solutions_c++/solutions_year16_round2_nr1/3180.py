#include<iostream>
#include<cstring>
using namespace std;
int main(void){
	int t,i,q=1;
	char a[2001],num[2001];
	cin>>t;
	while(t--){
		cin>>a;
		int countz=0,countw=0,countx=0,countu=0;
		for(i=0;i<strlen(a);i++){
			if(a[i]=='Z'){
				countz++;
			}
			 if(a[i]=='W'){
				countw++;
			}
			 if(a[i]=='U'){
				countu++;
			}
			 if(a[i]=='X'){
				countx++;
			}
		}
		int countZ=0,countZE=0,countZR=0,countZO=0;
		if(countz!=0){
			for(i=0;i<strlen(a);i++){
				if(a[i]=='Z' && countZ<countz){
					a[i]='a';
					countZ++;
				}
				if(a[i]=='E' && countZE<countz){
					a[i]='a';
					countZE++;
				}
				if(a[i]=='R' && countZR<countz){
					a[i]='a';
					countZR++;
				}
				if(a[i]=='O' && countZO<countz){
					a[i]='a';
					countZO++;
				}
			}
		}
		 countZ=0,countZE=0,countZR=0,countZO=0;
		if(countw!=0){
			for(i=0;i<strlen(a);i++){
				if(a[i]=='T' && countZ<countw){
					a[i]='a';
					countZ++;
				}
				if(a[i]=='W' && countZE<countw){
					a[i]='a';
					countZE++;
				}
				if(a[i]=='O' && countZR<countw){
					a[i]='a';
					countZR++;
				}
			}
		}
		 countZ=0,countZE=0,countZR=0,countZO=0;
		if(countu!=0){
			for(i=0;i<strlen(a);i++){
				if(a[i]=='F' && countZ<countu){
					a[i]='a';
					countZ++;
				}
				if(a[i]=='O' && countZE<countu){
					a[i]='a';
					countZE++;
				}
				if(a[i]=='U' && countZR<countu){
					a[i]='a';
					countZR++;
				}
				if(a[i]=='R' && countZO<countu){
					a[i]='a';
					countZO++;
				}
			}
		}
		 countZ=0,countZE=0,countZR=0,countZO=0;
		if(countx!=0){
			for(i=0;i<strlen(a);i++){
				if(a[i]=='S' && countZ<countx){
					a[i]='a';
					countZ++;
				}
				if(a[i]=='I' && countZE<countx){
					a[i]='a';
					countZE++;
				}
				if(a[i]=='X' && countZR<countx){
					a[i]='a';
					countZR++;
				}
			}
		}
		int countF=0;
			for(i=0;i<strlen(a);i++){
				if(a[i]=='F')countF++;
			}
		
		 countZ=0,countZE=0,countZR=0,countZO=0;
		if(countF!=0){
			for(i=0;i<strlen(a);i++){
				if(a[i]=='F' && countZ<countF){
					a[i]='a';
					countZ++;
				}
				if(a[i]=='I' && countZE<countF){
					a[i]='a';
					countZE++;
				}
				if(a[i]=='V' && countZR<countF){
					a[i]='a';
					countZR++;
				}
				if(a[i]=='E' && countZO<countF){
					a[i]='a';
					countZO++;
				}
			}
		}
		int countSE=0;
			for(i=0;i<strlen(a);i++){
				if(a[i]=='V')countSE++;
			}
		
		countZ=0,countZE=0,countZR=0,countZO=0;
		 int countZN=0;
		if(countSE!=0){
			for(i=0;i<strlen(a);i++){
				if(a[i]=='S' && countZ<countSE){
					a[i]='a';
					countZ++;
				}
				if(a[i]=='E' && countZE<countSE){
					a[i]='a';
					countZE++;
				}
				if(a[i]=='V' && countZR<countSE){
					a[i]='a';
					countZR++;
				}
				if(a[i]=='E' && countZO<countSE){
					a[i]='a';
					countZO++;
				}
				if(a[i]=='N' && countZN<countSE){
					a[i]='a';
					countZN++;
				}
			}
		}
		int one=0;
		for(i=0;i<strlen(a);i++){
			if(a[i]=='O')one++;
		}
		 countZ=0,countZE=0,countZR=0;
		if(one!=0){
			for(i=0;i<strlen(a);i++){
				if(a[i]=='O' && countZ<one){
					a[i]='a';
					countZ++;
				}
				if(a[i]=='N' && countZE<one){
					a[i]='a';
					countZE++;
				}
				if(a[i]=='E' && countZR<one){
					a[i]='a';
					countZR++;
				}
			}
		}
		int nine=0;
		
			for(i=0;i<strlen(a);i++){
				if(a[i]=='N')nine++;
			}
		
		 countZ=0,countZE=0,countZR=0,countZO=0;
		 //cout<<nine<<endl;
		if(nine!=0){
			for(i=0;i<strlen(a);i++){
				if(a[i]=='N' && countZ<nine/2){
					a[i]='a';
					countZ++;
				}
				if(a[i]=='I' && countZE<nine/2){
					a[i]='a';
					countZE++;
				}
				if(a[i]=='N' && countZR<nine/2){
					a[i]='a';
					countZR++;
				}
				if(a[i]=='E' && countZO<nine/2){
					a[i]='a';
					countZO++;
				}
			}
		}
		int eight=0;
		for(i=0;i<strlen(a);i++){
			if(a[i]=='I')eight++;
		}
		countZ=0,countZE=0,countZR=0,countZO=0;
		 countZN=0;
		if(eight!=0){
			for(i=0;i<strlen(a);i++){
				if(a[i]=='E' && countZ<eight){
					a[i]='a';
					countZ++;
				}
				if(a[i]=='I' && countZE<eight){
					a[i]='a';
					countZE++;
				}
				if(a[i]=='G' && countZR<eight){
					a[i]='a';
					countZR++;
				}
				if(a[i]=='H' && countZO<eight){
					a[i]='a';
					countZO++;
				}
				if(a[i]=='T' && countZN<eight){
					a[i]='a';
					countZN++;
				}
			}
		}
		int three=0;
		for(i=0;i<strlen(a);i++){
			if(a[i]=='T')three++;
		}
		 countZ=0,countZE=0,countZR=0,countZO=0,countZN=0;
		if(three!=0){
			for(i=0;i<strlen(a);i++){
				if(a[i]=='T' && countZ<three){
					a[i]='a';
					countZ++;
				}
				if(a[i]=='H' && countZE<three){
					a[i]='a';
					countZE++;
				}
				if(a[i]=='R' && countZR<three){
					a[i]='a';
					countZR++;
				}
				if(a[i]=='E' && countZO<three){
					a[i]='a';
					countZO++;
				}
				if(a[i]=='E' && countZN<three){
					a[i]='a';
					countZN++;
				}
			}
		}
		//cout<<a<<endl;
		int j=0;
		for(i=0;i<countz;i++)num[j++]='0';
		for(i=0;i<one;i++)num[j++]='1';
		for(i=0;i<countw;i++)num[j++]='2';
		for(i=0;i<three;i++)num[j++]='3';
		for(i=0;i<countu;i++)num[j++]='4';
		for(i=0;i<countF;i++)num[j++]='5';
		for(i=0;i<countx;i++)num[j++]='6';
		for(i=0;i<countSE;i++)num[j++]='7';
		for(i=0;i<eight;i++)num[j++]='8';
		for(i=0;i<nine/2;i++)num[j++]='9';
		cout<<"Case #"<<q++<<": ";
		for(i=0;i<j;i++)cout<<num[i];
		cout<<endl;


	}
	return 0;
}