#include<iostream>
#include<stdio.h>
#include<string.h>
#include<fstream>
using namespace std;

int charToInt(char &ch){
    return (int)ch-(int)'0';
}

int sol(string&s){
    //cout<<"\n\n\n";
    int req=0, total=0;
    for(int i=0; i<s.length(); i++){
        //cout<<"\ni="<<i<<"   t="<<total<<"  r="<<req;
        if(total<i){
            req+=i-total;
            total=i;
        }
        total+=charToInt(s[i]);
    }
        //cout<<"\nt="<<total<<"  r="<<req;
    return req;
}

int main()
{
    int T, t=1;
    ifstream f2("A-small-practice.in");
    remove("A-small-practice.out");
    ofstream f3("A-small-practice.out", ios::app);
    f2>>T;
    while(t<=T)
    {
        int smax;
        string s;
        f2>>smax>>s;
        int ans=sol(s);
        f3<<"Case #"<<t++<<": "<<ans<<endl;
    }
    return 0;
}

