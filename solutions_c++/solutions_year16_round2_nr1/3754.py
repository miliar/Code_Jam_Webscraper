#include <iostream>
#include <fstream>
#include <set>
#include <math.h>

using namespace std;

bool getanswer;
int fretraget[26];
int currentfretraget[26];
bool toobig;
int fre[10][26]={0};
string letter[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
ifstream fin("input");
ofstream fout("output");



void solve(int n,int digaltraget[])
{
    /*
    cout<<n<<endl;
    for (int i=0;i<10;i++)
        cout<<digaltraget[i]<<" ";
    cout<<endl;
    */
    
    if (getanswer)
        return;
    for (int i=0;i<26;i++)
        currentfretraget[i]=0;
    for (int i=0;i<10;i++)
        for (int j=0;j<letter[i].length();j++)
        {
            currentfretraget[ letter[i][j]-'A' ]+= digaltraget[i] ;
        }
    getanswer=true;
    
    for (int i=0;i<26;i++)
    {
        if (currentfretraget[i]>fretraget[i])
        {
            getanswer=false;
            return;
        }
        if (currentfretraget[i]!=fretraget[i])
            getanswer=false;
    }
    if (getanswer)
    {
        for (int i=0;i<10;i++)
            for (int j=0;j<digaltraget[i];j++)
                fout<<i;
        fout<<endl;
    }
    if (n>=10)
    {
        return;
    }
    int ii=-1;
    while (true)
    {
        ii++;
        digaltraget[n]=ii;
        for (int i=n+1;i<=9;i++)
            digaltraget[i]=0;
        toobig=false;
        
        for (int i=0;i<26;i++)
            currentfretraget[i]=0;
        for (int i=0;i<10;i++)
            for (int j=0;j<letter[i].length();j++)
            {
                currentfretraget[ letter[i][j]-'A' ]+= digaltraget[i] ;
            }
        
        for (int i=0;i<26;i++)
        {
            if (currentfretraget[i]>fretraget[i])
            {
                toobig=true;
            }
        }
        if (toobig)
            return;
        solve(n+1,digaltraget);
/*
        if (ii>30)
            break;*/
    }
}



int main()
{
    int inputnumber,ii,n,N,J,countcopy;
    long long count;
    long long div;
    long long divs[11];
    string ss;
    int total=0;
    fin>>inputnumber;

    for (int i=0;i<10;i++)
    {
        for (int j=0; j<letter[i].length(); j++)
        {
            fre[i] [ (letter[i][j]-'A') ]++;
        }
    }
    for (int ii=1;ii<=inputnumber;ii++)
    {
        fout<<"Case #"<<ii<<": ";
        fin>>ss;
        int digaltraget[10]={0};
        
        
        for (int i=0;i<26;i++)
            fretraget[i]=0;
        
        for (int i=0;i<ss.length();i++)
        {
            fretraget[ss[i]-'A']++;
        }
        getanswer=false;
        solve(0,digaltraget);
    }
    return 0;
}