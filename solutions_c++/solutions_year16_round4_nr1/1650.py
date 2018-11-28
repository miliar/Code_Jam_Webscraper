#include<bits/stdc++.h>
#define MOD 1000000007

/**
 *  Author : kaspers, Delhi Technological University
 */

#define mp(x,y) make_pair(x,y)
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define pi   3.14159265358979323846264338327950288
#define set0(a) memset(a,0,sizeof(a))
#define setN(a) memset(a,-1,sizeof(a))

using namespace std;

//Util Functions
template<class T> T gcd(T a,T b){if(b==0)return a;else return gcd(b,a%b);}
template<class T> T power(T a,T b){T result=1;while(b>0){if(b&1)	result = result * a;a = a*a;b>>=1;}return result;}
template<class T> T powerMod(T a,T b,T c){T result =1%c;while(b>0){if(b&1)result = (result * a)%c;a = (a*a)%c;b>>=1;}return result;}

typedef long long ll;
string gen(string A, int N)
{
    string B="";
    int i;
    if(N == 0)
        return A;
    for(i=0; i<A.length(); i++)
    {
        if(A[i] == 'P')
        {
            B.push_back('P');
            B.push_back('R');

        }
        if(A[i] == 'S')
        {
            if(N > 2)
            {
                B.push_back('S');
                B.push_back('P');
            }
            else
            {

            B.push_back('P');
            B.push_back('S');
            }
        }
        if(A[i] == 'R')
        {
            if(N == 1)
            {
                B.push_back('R');
                B.push_back('S');
            }
            else
            {
                B.push_back('S');
                B.push_back('R');
            }

        }

    }
    return gen(B, N-1);
}
int check(string A, int R, int P, int S)
{
    int i, n;
    n = A.length();
    for(i=0; i<n; i++)
    {
        if(A[i] == 'R')
            R--;
        if(A[i] == 'P')
            P--;
        if(A[i] == 'S')
            S--;
    }
    return (!R && !P && !S);
}
void eval()
{
    int N, R, P, S;
    cin>>N>>R>>P>>S;


    string A, B, C;
    A = gen("P", N);
    B = gen("R", N);
    C = gen("S", N);

    if(check(A, R, P, S)){
        cout<<A<<"\n";
        return;
    }
    if(check(B, R, P, S)){

        cout<<B<<"\n";
        return ;
    }
    if(check(C, R, P, S))
    {
        cout<<C<<"\n";
        return;
    }
            cout<<"IMPOSSIBLE\n";
}
int main()
{       freopen("input.txt","r",stdin);
    	freopen("output.txt","w",stdout);
    	cin.sync_with_stdio(0);
        cout.sync_with_stdio(0);
        int t, j=1;
        cin>>t;
        while(t--)
        {
            cout<<"Case #"<<j++<<": ";
            eval();
        }
	return 0;
}
