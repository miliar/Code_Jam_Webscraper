#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>
#include <utility>
#include <queue>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define RO(i,b,a) for (int i = (b); i >= (a); i--)
#define pb push_back
#define ARR0(A) memset((A), 0, sizeof((A)))


typedef long long LL;

using namespace std;



int n,k;
int ls[1001];
void A()
{
	int t; cin>>t;scanf("%d",&t);
    string S;
	FO(i,0,t)
	{
        cin>>S;
        ARR0(ls);

        ls[0] = S[0]-'A';
        int tlen= S.length();
        FO(j,1,tlen)
        {   
            if(S[j]-'A'-ls[0]>=0)
            {
                RO(k,j+1,1)
                    ls[k] = ls[k-1];
                ls[0] = S[j]-'A';
            }
            else
                ls[j] = S[j]-'A';
        }

        cout<<"Case #"<<(i+1)<<":"<< " ";
        FO(j,0,tlen)
            cout << char(ls[j]+'A');
		//printf("Case #%d: \n",(i+1));
        cout << endl;
	}

}

int main()
{	
    ios::sync_with_stdio(false);
   	A();
    return 0;

}