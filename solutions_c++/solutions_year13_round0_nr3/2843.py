#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <stdio.h>
#define M_SIZE 101
using namespace std;
class bigInt{

	public:
		bigInt()
		{}
		bigInt(const bigInt &rhs)
		{
			number= rhs.number;
		}
		bigInt& operator = (const bigInt &rhs){
			number= rhs.number;
			return *this;
		}
		bigInt(string s)
		{
			number = s;
		}

		void toString()
		{
			cout<<number<<endl;	
		}

		int compare(const bigInt &rhs){
			if(number.size()>rhs.number.size())
				return 1;
			if(number.size()<rhs.number.size())
				return -1;
				
			int length = number.size();
			for(int i =0;i<length;i++){
				if(number[i]!=rhs.number[i])
				{
					return number[i] - rhs.number[i];
				}
			}
		
		}

		void Increment(){
			int length = number.size();
			int carry = 1;
			for(int i=length-1;i>=0;i--)
			{
				if(number[i]=='9' && carry ==1){
					number[i]='0';
					carry =1;
					if(i==0)
					{
						number = "1"+number;
					}
				}
				else
				{
					number[i] = number[i]+carry;
					break;
				}
			}
		}
		
		bigInt square()
		{
			int i,j,temp,product,total;
			int num=0;
			int res[M_SIZE];
			memset(res,0,sizeof(res));
			int length = number.size();
			for(i=0;i<length;i++)
			{
				temp=0;
				for(j=0;j<length;j++)
				{    
					product =(number[length-1-j]-'0')*(number[length-1-i]-'0')+temp;
					if(0 == product)    
						continue;                
					num = j+i;        
					total = res[num]+product;    
					res[num] = total%10;    
					temp = total/10;
				}
				if( temp > 0 )
				{
					res[++num] += temp;
				}
			}

			bigInt result;
			for(i=num;i>=0;i--)  {
				result.number.push_back(res[i]+'0');
			}
			return result;
		}

		bigInt Double()
		{
			int i,j,temp,product,total;
			int num=0;
			int res[M_SIZE];
			memset(res,0,sizeof(res));
			int length = number.size();
			for(i=0;i<length;i++)
			{
				temp=0;

				product = 2 * (number[length-1-i]-'0')+temp;
				if(0 == product)    
					continue;                
				num = i;        
				total = res[num]+product;    
				res[num] = total%10;    
				temp = total/10;
				if( temp > 0 )
				{
					res[++num] += temp;
				}
			}

			bigInt result;
			for(i=num;i>=0;i--)  {
				result.number.push_back(res[i]+'0');
			}
			return result;
		}

		bool isSquarePalindrome(){
			return square().isPalindrome();
		}

		bool isPalindrome()
		{
			int length = number.size();
			for(int i=0;i<length/2;i++)
			{
				if(number[i]!=number[length-1-i])
					return false;
			}
			return true;
		}

	public:
		string number;

};

int main (int argc, char *argv[])
{
	int T;
	string sa,sb;
	
	cin >>T;
	
	int i=1; 
	while(i<=T){
		cin>>sa;
		cin>>sb;
		bigInt A(sa);
		bigInt B(sb);
		bigInt init(string("1"));
		bigInt d = init.Double();
		while( d.square().compare(A) < 0){
			init = d;
			d = init.Double();
		}
		while(init.square().compare(A)<0){
			init.Increment();
		}
		
		bigInt sqr;
		int counter=0;
	
		while(sqr = init.square(),sqr.compare(B)<=0)
		{ 
			if(init.isPalindrome() && sqr.isPalindrome()){
				counter ++;
			}
			
			init.Increment();
		}
		printf("Case #%d: %d\n",i,counter);
		i++;
	}
	
	
	return 0;
}
