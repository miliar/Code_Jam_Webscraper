#include<bits/stdc++.h>
using namespace std;
#define fs first
#define sc second
#define INF 1000000000
#define P 1000000007
#define pb push_back
#define mp make_pair
typedef long long Int;
typedef pair<Int,Int> pii;
typedef vector<Int> vi;
typedef vector<pii> vii;
 /* code is of miller robin*/

Int mulmod(Int a,Int b,Int c)
{
    Int x = 0,y=a%c;
    while(b > 0){
        if(b%2 == 1)
            x = (x+y)%c;
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}
Int modexp(Int a,Int b,Int m)
{
    Int ans=1;
    while (b)
    {
        if (b%2)
            ans=mulmod(ans,a,m);
        a=mulmod(a,a,m);
        b/=2;
    }
    return ans;
}
bool Miller(Int p,int iteration){
    if(p<2){
        return 0;
    }
    if(p!=2 && p%2==0){
        return 0;
    }
    Int s=p-1;
    while(s%2==0){
        s/=2;
    }
    for(int i=0;i<iteration;i++){
        Int a=rand()%(p-1)+1,temp=s;
        Int mod=modexp(a,temp,p);
        while(temp!=p-1 && mod!=1 && mod!=p-1){
            mod=mulmod(mod,mod,p);
            temp *= 2;
        }
        if(mod!=p-1 && temp%2==0){
            return 0;
        }
    }
    return 1;
}
bool check(Int x,Int N)
{
	for(int i=2;i<=10;i++)
	{
		Int temp=0;
		for(int j=0;j<N;j++)
		{
			if(x&(1<<j))
			{
				temp+=pow(i,j);
			}
		}
	//	cout<<temp<<endl;
		if(Miller(temp,20))
			return false;
	}
return true;
}

Int print_odd(Int N)
{
	for(Int i=3;i<=sqrt(N);i+=2)
	{
		if(N%i==0)
		{
			return i;
		}
	}

}

void print_fun(Int x,Int N)
{
	for(int j=N-1;j>=0;j--)
		{
			if(x&(1<<j))
			{
				cout<<'1';
			}
			else
			cout<<'0';
		}
		cout<<" ";
		for(int i=2;i<=10;i++)
		{
			Int temp=0;
			for(int j=N-1;j>=0;j--)
			{
				if(x&(1<<j))
				{
					temp+=pow(i,j);
				}
			}
			if(temp%2==0&&i!=10)
				cout<<"2 ";
			else if(temp%2==0&&i==10)
				cout<<"2";
			else
			{
				Int s=print_odd(temp);
				if(i!=10)
					cout<<s<<" ";
				else
					cout<<s;
			}
		}
}

Int Compute(Int N,Int J)
{
	int count=0;
	for(Int k=0;k<pow(2,N-2);k++)
	{
		Int i=k;
		i=i<<1;
		i=i|1;
		i=i|(1<<(N-1));
		if(check(i,N))
		{
			cout<<endl;
			count++;
			print_fun(i,N);
			if(count==J)
				return 0;
		}

	}
}

int main()
{

	Int T,N,J;
	cin>>T;
	for(int k=1;k<=T;k++)
	{
		cin>>N>>J;
		cout<<"Case #"<<k<<":";
		Compute(N,J);
	}

	return 0;
}
/*
1000000000000001 3 2 5 2 7 2 3 2 7
1010000000000001 13 11 3 4751 173 3 53 109 3
1110000000000001 3 2 5 2 7 2 3 2 11
1001000000000001 73 5 3 19 19 3 5 19 3
1011000000000001 3 2 5 2 7 2 3 2 11
1100100000000001 3 2 5 2 7 2 3 2 7
1001100000000001 3 2 5 2 7 2 3 2 11
1101100000000001 5 1567 15559 6197 5 5 1031 7 83
1111100000000001 3 2 3 2 7 2 3 2 3
1010010000000001 3 2 5 2 7 2 3 2 7
1101010000000001 3 7 13 3 5 43 3 73 7
1111010000000001 5 2 3 2 37 2 5 2 3
1000110000000001 3 2 5 2 7 2 3 2 11
1010110000000001 23 17 11 23 5 299699 43 239 59
1110110000000001 3 2 3 2 7 2 3 2 3
1101110000000001 17 2 3 2 73 2 17 2 3
1011110000000001 3 2 3 2 7 2 3 2 3
1100001000000001 3 2 5 2 7 2 3 2 11
1001001000000001 3 2 5 2 7 2 3 2 7
1111001000000001 3 2 3 2 7 2 3 2 3
1010101000000001 3 7 13 3 5 17 3 53 7
1110101000000001 5 2 3 2 37 2 5 2 3
1001101000000001 11 5 281 101 5 67 5 13 19
1101101000000001 3 2 3 2 7 2 3 2 3
1011101000000001 17 2 3 2 1297 2 11 2 3
1111101000000001 59 113 7 157 19 1399 7 43 107
1000011000000001 3 2 5 2 7 2 3 2 11
1100011000000001 23 19 11 105491 5 47 11117 1787 127
1110011000000001 3 2 3 2 7 2 3 2 3
1101011000000001 5 2 3 2 37 2 5 2 3
1011011000000001 3 2 3 2 7 2 3 2 3
1100111000000001 3 2 3 2 7 2 3 2 3
1010111000000001 5 2 3 2 37 2 5 2 3
1001111000000001 3 2 3 2 7 2 3 2 3
1101111000000001 31 557 7 19 23 1129 7 5441 241
1011111000000001 7 19 43 17 55987 23 7 7 31
1111111000000001 3 2 5 2 7 2 3 2 7
1100000100000001 167 2 11 2 58427 2 23 2 839
1010000100000001 3 2 5 2 7 2 3 2 11
1001000100000001 5 2 7 2 1933 2 29 2 157
1000100100000001 3 2 5 2 7 2 3 2 7
1110100100000001 3 2 3 2 7 2 3 2 3
1001100100000001 7 1667 179 13 5 11 23 7 311
1101100100000001 11 2 3 2 13 2 47 2 3
1011100100000001 3 2 3 2 7 2 3 2 3
1100010100000001 3 1259 421 3 5 8893 3 67 17
1110010100000001 5 2 3 2 37 2 5 2 3
1001010100000001 3 5 13 3 5 43 3 73 7
1100110100000001 47 2 3 2 11 2 204311 2 3
1010110100000001 3 2 3 2 7 2 3 2 3
*/