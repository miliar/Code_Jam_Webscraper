#include <iostream>
#include <fstream>

using namespace std;

int deal(int p,int q)
{
    for(int i=p;i>1;i--)
        if(p%i==0 && q%i==0) return i;
    return 0;
}
int str_length(string s)
{
    int i = 0;
    while(s[i]) i++;

    return i;
}


int main()
{
    ifstream infile("A-small-attempt2.in");
    ofstream outfile("A-small-attempt2.txt");
    int t;
    string s;
    int p,q;
    int d;
    int counter;
    int l;
    int j = 0;
    double result;
    infile>>t;

    for(int i=0;i<t;i++){
        counter = 0;
        p = q = 0;
        infile>>s;
        l = str_length(s);
        j = 0;
        while(s[j]!='/'){
            p = p*10+s[j]-'0';
            j++;
        }
        j++;
        for(;j<l;j++) q = q*10+s[j]-'0';
        d = deal(p,q);
        if(d!=0){
            p = p/d;
            q = q/d;
        }

        result = double(p)/q;

        while(q%2==0 && q!=0)
            q = q/2;

        while(result<1){
            result *= 2;
            counter++;
        }

        if(q==1) outfile<<"Case #"<<i+1<<": "<<counter<<endl;
        else outfile<<"Case #"<<i+1<<": impossible"<<endl;
    }
    return 0;
}
