#include<cstdio>
#include<iostream>
#include<string>
#include<cmath>

#define REP(i,N) for(int (i) = 0; (i)<(N); (i)++)
using namespace std;

string solve(int x,int r,int c){
	if(x == 1)
		return "GABRIEL";
	if(x == 2){
		if(c*r %2 == 0)
			return "GABRIEL";
		return "RICHARD";
	}
	if(x == 3){
		if( r*c % 3 == 0){
			if(r >1 && c > 1)
				return "GABRIEL";
			else
				return "RICHARD";
		}else
			return "RICHARD";
	}
	if(x == 4){
		if(min(r,c) <= 2){
			return "RICHARD";
		}
		if(max(r,c) < 4){
			return "RICHARD";
		}
		if(((r==4)&&(c==3)) ||((r==3)&&(c==4))){
			return "GABRIEL";
		}
		if((c>=4&& r>= 4) && r*c %4 == 0)
			return "GABRIEL";
		else
			return "RICHARD";
	}
	if(x==5){
		if(r*c %5 != 0 || min(r,c) < 4)
			return "RICHARD";
		else
			return "GABRIEL";
	}
	if(x== 6){
		if(r*c %6 == 0 && min(r,c) >=4)
			return "GABRIEL";
		else 
			return "RICHARD";
	}
	else return "RICHARD";

		
		
}


int main()
{
	int test;
	scanf("%i",&test);
	int x, r,c;
	REP(a,test){
		scanf("%i%i%i", &x,&r,&c);
		string win = solve(x,r,c);
		cout<<"Case #"<<a+1<<": "<<win<<endl;
	}
	return 0;
}
