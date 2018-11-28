#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;


int getGCD(int a, int b)
{
	int r;
while ( a % b !=0)

{

r=a%b;

a=b;

b=r;

}
return r;
}


int main()
{
    
    int t;
     cin>>t;
	 for(int i=0;i<t;i++)
     {
     	string cur;
     	cin>>cur;
     	
     	string delimiter = "/";
		string Ps = cur.substr(0, cur.find(delimiter));
		string Qs = cur.substr(cur.find(delimiter) + 1);
     	
     	int P = atoi(Ps.c_str());
     	int Q = atoi(Qs.c_str());
     	
     	
     	int gcd = getGCD(Q,P);
     	
     	P = P/gcd;
     	Q = Q/gcd;
     	bool possible = true;
     	int num=0;
     	if(P%2==0) possible = false;
     	else if(P==1 && Q==1){
     		possible = true; num = 0;
     	}
     	else{
     		num=1;
     		possible = true;
     		while(2*P < Q) 
			{
				if(Q%2!=0) 
				{
					possible = false; break;
				}
				Q=Q/2;
				
				num++;
     		}
     			while(Q>1) 
				{
					if(Q%2!=0){
					
					possible = false; break;}
					else Q=Q/2;
				}
     		
     	}
     	if(possible)
     	cout<<"Case #"<<i+1<<": "<<num<<endl;
     	else
     	cout<<"Case #"<<i+1<<": impossible"<<endl;
     }
	 return 0;     
}
