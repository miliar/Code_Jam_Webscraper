#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <iterator>
#include <map>
#include <cstring>
#include <climits>
#include <time.h>

using namespace std;

#define READ() 	freopen("in.txt","r",stdin)
#define WRITE() freopen("out.txt","w",stdout)
#define sf(n) 	scanf("%d",&n)
#define lsf(n) 	scanf("%lld", &n)
#define pb(n) 	push_back(n)
#define EPS 	1e-10
#define NL 		printf("\n")
#define INF     INT_MAX
#define MAX     INT_MAX
#define MOD     1000000007
#define LL      long long

bool statusOfN[10000010];

int primes[1000001];
int primeIndex = 0;
void genPrimes(int);

void fastSeive(int n)
{
    for(long long i=3;i*i<=n;i+=2)
    {
        if(!statusOfN[i])
        {
            /// this wont work here!
//            primes[primeIndex] = i;
//            primeIndex++;
            for(long long j=i*i;j<n;j+=(2*i))
            {
                statusOfN[j] = true;
            }
        }
    }
}

void genPrimes(int n)
{
    primes[primeIndex] = 2;
    primeIndex++;
//    cout << 2 << endl;
    for(int i = 3;i<n;i+=2)
    {
        if(!statusOfN[i])
        {
//            cout << i << endl;
            primes[primeIndex] = i;
            primeIndex++;
        }
    }

//    cout << "total prime : " << primeIndex << endl;
}



long long customPow(long long x,long long p)
{
    long long Ans = 1;
    long long xx = x;

    while( p > 0)
    {
        if(p%2 == 1)Ans = (Ans) * (xx);

        xx = (xx) * (xx);

        p = p/2;
    }

    return Ans;
}

long long convertToBase10(string s,int curBase)
{
    int iCnt = 0;
    long long base10Val = 0;
    for(int i=s.size()-1;i>=0;i--)
    {
        int x = s[i]-48;
        base10Val += customPow(curBase,iCnt++) * x;
    }

    return base10Val;
}

bool chkValid(string s)
{
    int cntVal = 0;
    for(int i=2;i<11;i++)
    {
        LL val = convertToBase10(s,i);


        bool found = false;
        for(int j=0;j<primeIndex;j++)
        {
            if(val % primes[j] == 0 && val != primes[j])
            {
                found = true;
                cntVal++;
                break;
            }
        }

        if(!found)return false;

    }
    if(cntVal == 9)return true;
    else return false;
}


int main()
{
    READ();
    WRITE();
    fastSeive(10000001);
    genPrimes(10000001);

    int t,a,b;
    cin >> t >> a >> b;

    string s = "100000000000000";

    int cntFound = 0;

    vector <string> ansVec;

    for(LL bt = 0;bt < (1<<14);bt++)
    {
        string newS = s;

        for(int i=0;i<14;i++)
        {
            if(bt & (1<<i) )
            {
                newS[i+1] = '1';
            }
        }
        newS += '1';

        for(int i=1;i<7;i++)
        {
            swap(newS[i],newS[14-i]);
        }

        if(chkValid(newS))
        {
            cntFound++;
//            cout << newS << endl;
            ansVec.pb(newS);
        }

        if(cntFound == 50)break;

//        cout << newS.size() << endl;

    }

    cout << "Case #1:" << endl;

    for(int i=0;i<ansVec.size();i++)
    {
        string ansS = ansVec[i];

        cout << ansS ;

        for(int j=2;j<11;j++)
        {
            LL newVal = convertToBase10(ansS,j);

            for(int k=0;k<primeIndex;k++)
            {
                if(newVal % primes[k] == 0 && primes[k] != newVal)
                {
                    cout << " " << primes[k];
                    break;
                }
            }

        }
        cout << endl;


    }




    return 0;
}

