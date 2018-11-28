#include<stdio.h>
#include<stdlib.h>
#include <iostream>
#include <bitset>
#include<string>
#include<sstream>
using namespace std;

#include<math.h>

#define Max_Prime 100000000
int Prime[10000000],Prime_num=0;
bool mark[Max_Prime];
void make_Prime(void)
{	
	for(int i=0;i<Max_Prime;i++)
		mark[i]=1;
	for(int i=2;i<Max_Prime;i++)
	{
		if(mark[i]==0) continue;
		for(int j=i*2;j<Max_Prime;j+=i)
			mark[j]=0;
	}
	for(int i=2;i<Max_Prime;i++)
		if(mark[i]) Prime[Prime_num++]=i;
		
	/*for(int i=0;i<Prime_num;i++)
		printf(i+1==Prime_num ? "%d\n" : "%d ",Prime[i]);*/
	//printf("Prime_num=%d\n",Prime_num);
}

int is_Prime(long long n)
{
	if(n==1 || n==0) return 0;
	for(int i=0;Prime[i]<((int)sqrt((long double)n))+1 && i<Prime_num;i++)
		if(n%Prime[i]==0) return Prime[i];
	return 0;
}

bool is_jam_coin(string &binary, long long *div)
{
    long long m;
    int d;

    for (int base = 2; base <= 10; base++)
    {
        //unsigned long m = std::bitset<16>(binary).to_ulong();
        m = _strtoi64(binary.c_str(), NULL, base);
        d = is_Prime(m);
        if (d == 0) return false;
        div[base] = d;
        //cout << m << endl;
    }
    return true;
}

void solve()
{
    int n, j;
    long long div[20];

    make_Prime();

    scanf("%d %d", &n, &j);

    for (int i = 0; i < 32768; i++)
    //for (int i = 0; i < 32; i++)
    {
        string binary = bitset<15>(i).to_string(); //to binary
        //string binary = bitset<5>(i).to_string(); //to binary
        binary = "1" + binary;
        if (binary[n-1] == '0') continue;
        //cout << binary << endl;

        if (is_jam_coin(binary, div))
        {
            cout << binary;
            for (int base = 2; base <= 10; base++)
                printf(" %d", div[base]);
            printf("\n");
        }


    }
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif

    int T;
    
    scanf("%d", &T);
    for(int i = 1; i <= T; i++)
    {
        printf("Case #%d:\n", i);
        solve();
    }
    return 0;  
}
