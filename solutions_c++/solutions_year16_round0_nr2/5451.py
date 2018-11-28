#include <iostream>
#include <algorithm>
#include <map>
#include <bitset>
#include <set>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <string.h>
#include <cstring>
#include <iomanip>
#include <stdio.h>
#include <sstream>
#include <bitset>
#include <locale>
#include <iostream>
#include <cmath>
#include <iomanip>
#include <math.h>
#include <bitset>
#include<sstream>
#include<string>
#include<string.h>
using namespace std;
#define ll  long long
string input;
inline char Compliment(char r)
{
    return (r=='+')?'-':'+';
}
ll Last()
{
    for(ll i=input.size()-1;i>=0;i--)
        if(input[i]=='-')
        return i;
    return -1;
}
void SWAP(ll LAST)
{
    for(ll i=0;i<=LAST/2;i++)
    {
        swap(input[i],input[LAST-i]);
        if(i!=LAST-i)
            input[i]=Compliment(input[i]);
        input[LAST- i]=Compliment(input[LAST- i]);
}
}
ll beforeN()
{
    for(ll i=0;i<input.size();i++)
        if(input[i]=='-')
        return i-1;
    return input.size()-1;
}
int main()
{
freopen("O.txt","w",stdout);
freopen("I.txt","r",stdin);

ll t,counter,LAST;
cin>>t;
for(ll i=1;i<=t;i++)
{
    cin>>input;
counter=0;
while(true)
{
    LAST=Last();
    if(LAST==-1)
        break;
    if(input[0]=='+')
      SWAP(beforeN()),counter++;//  input[0]='-',counter++;
    SWAP(LAST);
    counter++;
}
cout<<"Case #"<<i<<": "<<counter<<endl;
}
return 0;
}


