#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cstring>

using namespace std;

int l,x;
string ijk, result;
char dp[10006][10006];

char mul(char a, char b)
{
	//-i -> a; -j -> b; -k -> c; -1 -> d

	if(a=='1' && b=='1') return '1';
	if(a=='1') return b;
	if(b=='1') return a;

	if(a=='d' && b=='i') return 'a';
	if(a=='d' && b=='j') return 'b';
	if(a=='d' && b=='k') return 'c';
	if(a=='d' && b=='d') return '1';
	if(a=='d' && b=='a') return 'i';
	if(a=='d' && b=='b') return 'j';
	if(a=='d' && b=='c') return 'k';

	if(a==b) return 'd';

	if(a=='i' && b=='j') return 'k';
	if(a=='i' && b=='k') return 'b';
	if(a=='i' && b=='a') return '1';
	if(a=='i' && b=='d') return 'a';
	if(a=='i' && b=='b') return 'c';
	if(a=='i' && b=='c') return 'j';

	if(a=='a' && b=='j') return 'c';
	if(a=='a' && b=='k') return 'j';
	if(a=='a' && b=='i') return '1';
	if(a=='a' && b=='d') return 'i';
	if(a=='a' && b=='b') return 'k';
	if(a=='a' && b=='c') return 'b';


	if(a=='j' && b=='i') return 'c';
	if(a=='j' && b=='k') return 'i';
	if(a=='j' && b=='b') return '1';
	if(a=='j' && b=='d') return 'b';
	if(a=='j' && b=='a') return 'k';
	if(a=='j' && b=='c') return 'a';

	if(a=='b' && b=='i') return 'k';
	if(a=='b' && b=='k') return 'a';
	if(a=='b' && b=='j') return '1';
	if(a=='b' && b=='d') return 'j';
	if(a=='b' && b=='a') return 'c';
	if(a=='b' && b=='c') return 'i';


	if(a=='k' && b=='i') return 'j';
	if(a=='k' && b=='j') return 'a';
	if(a=='k' && b=='c') return '1';
	if(a=='k' && b=='d') return 'c';
	if(a=='k' && b=='a') return 'b';
	if(a=='k' && b=='b') return 'i';

	if(a=='c' && b=='i') return 'b';
	if(a=='c' && b=='j') return 'i';
	if(a=='c' && b=='k') return '1';
	if(a=='c' && b=='d') return 'k';
	if(a=='c' && b=='a') return 'j';
	if(a=='c' && b=='b') return 'a';
}

void precompute()
{
	for(int i=2;i<=(l*x);i++)
		for(int j=0;j<=(l*x)-i;j++)
			dp[i][j] = mul(ijk[j%l], dp[i-1][j+1]); 
}

// bool dijkstra()
// {
// 	char r1,r2,r3;
// 	for(int i =0;i<l-2;i++)
// 	{
// 		int remX=x;
// 		r1=dp[i+1][0];
// 		while(r1!='i')
// 		{
// 			if(remX==1 || (x-remX)>3)
// 				break;
// 			r1 = mul(dp[l][0],r1);
// 			remX--;
// 		}
// 		if(r1!='i') continue;

// 		for(int j=i+1;j<l-1;j++)
// 		{
// 			r2=dp[j-i][j];
// 			while(r2!='j')
// 			{
// 				if(remX==1 || (x-remX)>3)
// 					break;
// 				r2 = mul(mul(dp[l-j][j],dp[l][0]),dp[j+1][0]);
// 				remX--;
// 			}
// 			if(r2!='j') continue;

// 			r3=dp[l-j-1][j+1];
// 			while(r3!='k')
// 			{
// 				if(remX==1 || (x-remX)>3)
// 					break;
// 				r3 = mul(r3,dp[l][0]);
// 				remX--;
// 			}

// 			if(r3 == 'k') return true;
// 		}
// 	}

// 	return false;
// }

bool dijkstra2()
{
	int size=l*x;
	char r1='1',r2,r3;
	for(int i=0;i<size-2;i++)
	{
		if(dp[i+1][0]!='i') continue;
		for(int j=i+1;j<size-1;j++)
		{
			if(dp[j-i][i+1]!='j') continue;
			if(dp[size-j-1][j+1]=='k') return true;
		}
	}

	return false;
}

// void duplicate()
// {
// 	for(int i=0;i<x;i++)
// 		ijkM += ijk;
// }

int main(int argc, char* argv[])
{
	fstream file;
	file.open(argv[1]);
	int t;
	file>>t;
	for(int i=0;i<t;i++)
	{
		file >> l >> x >> ijk;
		if((l * x)<3)
			result = "NO";
		else
		{
			for(int j=0;j<=(l*x)+1;j++)
			{
				dp[1][j]=ijk[j%l];
				dp[0][j]='1';
			}
		
			precompute();
			// duplicate();
			result = dijkstra2()?"YES":"NO";
		}
		
		printf("Case #%d: %s\n",i+1,result.c_str());
	}

	file.close();

}