#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;


ofstream outFile("../GoogleJam/output.txt");
int c[102][102];
int maxL[102];
int maxC[102];
bool sumout(long int n)
{
    int l = floor(log((float)n)/log(10))+1;
    int digits[20];
    int p=1;
    for(int i=0; i<l; ++i)
    {
        digits[i] = int(floor((n%(p*10))/p));
        if(digits[i]>3) return true;

        p *= 10;
    }
    for(int i=0; i<l; ++i)
    {
        int sum = 0;
        for(int j=0; j<=i; ++j)
        {
            sum+=digits[j]*digits[i-j];
        }
        if(sum>9) return true;
    }


    return false;
}

bool palindrome(long int n)
{
    int l = floor(log((float)n)/log(10))+1;
    //cout << "l="<<l<<endl;
    long int p = 1;
    long int P = pow(10,l);
    //cout << "p="<<p<<"   P="<<P<<endl;
    for(int i=0; i<l/2+1; ++i)
    {
        //cout << "1="<<int(floor((n%(p*10))/p))<<"   2="<<int(floor((n%(P))/(P/10)))<<endl;
        if(int(floor((n%(p*10))/p)) != int(floor((n%(P))/(P/10))))
        {
            return false;
        }

        p *= 10;
        P /= 10;
    }
    return true;
}

void eval(){
    long int A;
    long int B;
    long int rA;
    long int rB;
    cin>>A;
    cin>>B;
    rA = ceil(sqrt(A));
    rB = floor(sqrt(B));

    int count = 0;

    long int tempSquare;

    for(long int i=rA;i<=rB;++i)
    {
        if(palindrome(i) && !sumout(i))
        {
            //tempSquare = i*i;
            //if(tempSquare<=B && tempSquare>=A)
            {
                count++;
            }

        }
    }



    outFile<<count;
    cout<<count;
}

int main(){

    if(false)
    {
        cout<<(palindrome(222)?"OUI":"NON")<<endl;
        cout<<(sumout(222)?"OUT":"COOOOOL")<<endl;
        return 0;
    }
    int cases;
    string line;
    getline(cin, line);
    istringstream(line)>>cases;
    for(int i=1; i<=cases; i++){
        cout<<"Case #"<<i<<": ";
        outFile<<"Case #"<<i<<": ";
        eval();
        outFile<<endl;
        cout<<endl;
    }
    return 0;
}
