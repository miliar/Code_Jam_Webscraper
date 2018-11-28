#include<iostream>
#include<stdio.h>
#include<map>
#include<math.h>
#include<fstream>
#include<string>
#include<stdlib.h>
using namespace std;
int main()
{
    ifstream input ("C-small-attempt0.in") ;
    ofstream output ("output.txt") ;
    map<int , int> m ;
    int j,k;
    for(int i=1;i<1000;i++)
    {
        k = 0 ;
        j = i;
        while(j)
        {
           k *= 10 ;
           k += j%10 ;
           j = j/10 ;
        }
        if(i == k)
        {
            //cout<<i<<endl ;
            m[i]++ ;
        }
    }
    int cases ,a,b,sum ,t;
    string st ;
    float temp ;
    //scanf("%d",&cases) ;
    getline(input , st) ;
    cases = atoi(st.c_str()) ;
    t = cases ;
    while(cases--)
    {
        string as,bs ;
        sum = 0 ;
        int i ;
        getline(input , st) ;
        for( i=0;st[i] != ' ';i++)
            as += st[i] ;
        a = atoi(as.c_str()) ;
        for(;i<st.length();i++)
            bs += st[i] ;
        b = atoi(bs.c_str()) ;
        for(int i = a;i <= b;i++)
        {
            if(m[i] == 0)
                continue ;
            temp = sqrt(i);
            if(temp == (int)temp)
                if(m[temp] != 0)
                    sum++ ;
        }
        output<<"Case #"<<t - cases<<": "<<sum<<endl ;
    }
    return 0;
}
