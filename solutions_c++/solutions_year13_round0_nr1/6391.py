#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>


using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }
char nc() { char a; scanf( "%c", &a ); return a; }

const char *	xw[] = { 
		"XXXX",
		"XXXT",
		"XXTX",
		"XTXX",
		"TXXX"  
};

const char *	ow[] = { 
		"OOOO",
		"OOOT",
		"OOTO",
		"OTOO",
		"TOOO"  
};

int main( )
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
				
	int T = ni();

for(int k = 0; k < T; ++k)
{
	printf("Case #%d: ", (k+1));
	
	vector<char> gameh;
	vector<char> gamev;
	
	//[Get game field]
	for(int i = 0; i < 4; ++i)
	{
	  for(int j = 0; j < 4; ++j)
	  {
	    char a = nc();
	    if('X' == a || 'O' == a || 'T' == a || '.' == a)
	    {
	      gameh.push_back(a);	      
	      
	      continue;
	    }	    
	    --j;
	  }	  
	
	}
	
	
	
	//[Transpose game field]
	for(int i = 0; i < 4; ++i)
	{
	  for(int j = 0; j < 4; ++j)
	  {
	    char a = gameh.at(j*4+i);
	    gamev.push_back(a);	    
	    
	  }
	  
	}
	
	
	
	//[Horizontal and vertical check]
	string diag1;
	string diag2;
	
	diag1.push_back(gameh.at(0));
	diag1.push_back(gameh.at(5));
	diag1.push_back(gameh.at(10));
	diag1.push_back(gameh.at(15));
	
	diag2.push_back(gameh.at(3));
	diag2.push_back(gameh.at(6));
	diag2.push_back(gameh.at(9));
	diag2.push_back(gameh.at(12));
	
	bool nstep = false;
	
	for(int i = 0; i < 4; ++i)
	{
	  string strh(gameh.begin()+i*4, gameh.begin()+4+i*4);
	  string strv(gamev.begin()+i*4, gamev.begin()+4+i*4);	  	 
	  
	  for(int j = 0; j < 5; ++j)
	  {
	    if( !strh.compare(0, sizeof(xw[j]), xw[j]) || !strv.compare(0, sizeof(xw[j]), xw[j])  || !diag1.compare(0, sizeof(xw[j]), xw[j]) || !diag2.compare(0, sizeof(xw[j]), xw[j]))
	    {
		printf("X won\n");
		i = 5;
		nstep = true;
		break;
	    }
	    else if( !strh.compare(0, sizeof(ow[j]), ow[j]) || !strv.compare(0, sizeof(ow[j]), ow[j]) || !diag1.compare(0, sizeof(ow[j]), ow[j]) || !diag2.compare(0, sizeof(ow[j]), ow[j]))
	    {
	      printf("O won\n");
	      i = 5;
	      nstep = true;
	      break;
	    }
	  }
	}
	
	if(nstep)
	{
	  continue;
	}
	
	for(int i = 0; i < gameh.size(); ++i)
	{
	  if('.' == gameh.at(i))
	  {
	    printf("Game has not completed\n");
	    nstep = true;
	    break;
	  }
	}
	
	if(nstep)
	{
	  continue;
	}
	
	printf("Draw\n");
}
	

	return 0;
}
