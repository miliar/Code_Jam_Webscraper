#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../../output.txt");
ifstream fin("../../../input.txt");

int lis[10000000];

int invert(int x)
{
    int ret = 0;
    while(x>0)
    {
        ret*=10;
        ret+=x%10;
        x/=10;
    }
    return ret;
}

long long make(long long n, long long base)
{
    if(n==base)
        return 0;
    if(n%10==0)
        return 1LL + make(n-1,base);
    
    long long ret = n-base;
    vector<long long> num;
    
    long long p  =n;
    
    while(p>0)
    {
        num.push_back(p%10);
        p/=10;
    }
    
    for(int i=num.size()-1; i>0; i--)
    {
        long long a,b,c;
        
        a=0;
        
        for(int j=i; j<num.size(); j++)
        {
            a*=10LL;
            a+=num[j];
        }
        
        b=0;
        
        for(int j=i-1; j>=0; j--)
        {
            b*=10LL;
            b+=num[j];
        }
        
        c = a + b;
        
        if(c<ret)
            ret=c;
        
           //cout << n << " " << a << " " << b << " " << ret << endl;
    }
    
    
    return ret;
}

long long solve(long long n)
{
    long long curr = 1;
    long long ret = 1;
    
    while(curr*10<=n)
    {
        ret+=make(curr*10-1,curr)+1;
        //cout << ret << endl;
        curr*=10;
    }
    ret+=make(n,curr);
    return ret;
    
}

void init()
{
    memset(lis,0,sizeof(lis));
    lis[0]=0;
    
    for(int i=1; i<=1000000; i++)
    {
        if(lis[i]==0)
        {
            lis[i]=lis[i-1]+1;
        }
        else if(lis[i] > lis[i-1]+1)
            lis[i]=lis[i-1]+1;
        int k = invert(i);
        if(k>i)
        {
            if(lis[k]==0 || lis[k]>lis[i]+1)
                lis[k]=lis[i]+1;
        }
        
//        if(i<1000000 && lis[i]!=solve(i))
//            cout << i <<  "ERROR " << endl;
    }
    return;
}



int main(void)
{
    int ttt;
    fin >> ttt;
    int ct = 0;
    string s;
    
    cout.precision(9);
    fout.precision(9);
    
    cout << "HELLO" <<  " " << ttt << endl;
    init();
    
    
    while(ttt>0)
    {
        ct++;
        ttt--;
        
        double f,x;
        long long n;
        
        fin >> n;
        
        
        long long ans = solve(n);
        
       
        
        cout << "Case #" << ct << ": ";
        fout << "Case #" << ct << ": ";
        
        
        cout << ans;
        fout << ans;
        
        
        
        
        
        fout << endl;
        cout << endl;
        
    }
    
    
    return 0;
}

