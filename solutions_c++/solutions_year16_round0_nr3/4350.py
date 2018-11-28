#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <sstream>
#include <math.h>
using namespace std;

double stringToNumber (const string &Text );
void generateCoins(int len,int num,ofstream &out);
int checkPrime(string num,int base);

int main(){
	long cases;
	long num,len;
	string temp;
	ifstream in("C-small-attempt0.in");
	ofstream out("output.txt");
	in>>cases;
	for(long i=0;i<cases;i++){
		out<<"Case #"<<(i+1)<<":"<<endl;
		in>>len;
		in>>num;
		generateCoins(len,num,out);
	}
	in.close();
	out.close();
}

void generateCoins(int len,int num,ofstream &out){
	string coin;
	int count=0;
	int div[9];
	if(len>2){
		//generates binary strings
		for(int i = 0; i < pow(2,(len-2)) && count<num; i++){
		for(int q=0;q<9;q++){
			div[q]=0;
		}
        string bin= "";
        int temp = i;
            for (int j = 0; j < (len-2); j++)
            {
                if (temp%2 == 1)
                    bin = '1'+ bin;
                else
                    bin = '0'+ bin;
                    temp = temp/2;
            }
            bin='1'+bin+'1';
            //check for divisibility
            div[0]=checkPrime(bin,2);
            for(int x=1;x<9;x++){
            	if(div[x-1]!=0){
            		div[x]=checkPrime(bin,x+2);
            	}
            }
            //display the result
            int check=0;
            for(long x=0;x<9;x++){
            	if(div[x]==0){
            		check=1;
            	}
            }
            if(check==0){
            	count++;
            	out<<bin;
            	for(long k=0;k<9;k++){
            		out<<" "<<div[k];
            	}
            	out<<endl;
            }
    	}
	}
	else{
		//in case length=2 no output
	}
}


int checkPrime(string num,int base){
	//cout<<num<<endl;
	string input=num;
	long base10=0;
	long len=input.length();
	long out=0;
	//convert to base10
	for(int i=0;i<len;i++){
		base10=base10+((input[i]-48)*pow(base,len-1-i));
	}

	//check for primality
	for(long i=2;i<=sqrt(base10);i++){
		if(base10%i==0){
			out=i;
			break;
		}
	}
	return out;
}

double stringToNumber (const string &Text )
{                               
	stringstream ss(Text);
	double result;
	return ss >> result ? result : 0;
}