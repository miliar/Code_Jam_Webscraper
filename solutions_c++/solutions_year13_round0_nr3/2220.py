#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <iomanip>
#include <locale>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>

#define maxi 10000000

using namespace std;

struct fairandsquare{
long long int square;
long long int root;
};

bool ispal(string input)
{
    long long int loop;
    long long int Size=input.size();
    for(loop=0;loop<Size/2;loop++)
    {
        if(input[loop]!=input[Size-loop-1]) return false;
    }
    return true;
}

bool isintpal(fairandsquare a)
{
    long long int perS=a.square;
    long long int perR=a.root;
    ostringstream convert1,convert2;
    string Sres,Rres;
    convert1<<perS;
    Sres=convert1.str();


    if(ispal(Sres))
    {
        //cout<<"de\n";
        convert2<<perR;
        Rres=convert2.str();
        if(ispal(Rres))
        {
            //cout<<"de\n";
            return true;
        }
        else            return false;
    }
    else    return false;
}

inline bool cmpSquare(fairandsquare b,fairandsquare c)
{
    return b.square<c.square;
}


int main(void)
{
    ofstream cout ("C-large-1.out");
    ifstream cin ("C-large-1.in");
    vector<fairandsquare> n2;
    //vector<long long int>  save;
    fairandsquare temp;
    long long int i,j,k;
    long long int T,ans;
    long long int A,B;
    long long int lo,hi;

    for(i=1;i<=maxi;i++)
    {
        temp.square=i*i;
        temp.root=i;
        n2.push_back(temp);
    }
    //cout<<maxi;
    //cout<<"\n";
    long long int n2Size=n2.size();
    //for(i=0;i<n2Size;i++)
    //{
        //if(isintpal(n2[i]))
        //{
            //save.push_back(n2[i].square);
        //}
    //}
    //for(i=0;i<save.size();i++)    cout<<save[i]<<"\n";

    for(i=n2Size-1;i>=0;i--)
    {
        if(!isintpal(n2[i]))
        {
            if(i!=n2.size()-1)  swap(n2[i],n2[n2.size()-1]);
            n2.pop_back();
        }
    }
    sort(n2.begin(),n2.end(),cmpSquare);
    //for(i=0;i<n2.size();i++)    cout<<n2[i].square<<"\n";


    cin>>T;
    for(k=1;k<=T;k++)
    {
        cin>>A>>B;
        ans=0;
        for(i=0;i<n2.size();i++)
        {
            //cout<<n2[i].square<<" "<<A<<" "<<B<<"\n";
            if(A<=n2[i].square&&B>=n2[i].square)    ans++;
        }
        cout<<"Case #"<<k<<": "<<ans<<"\n";
    }

    return 0;
}
