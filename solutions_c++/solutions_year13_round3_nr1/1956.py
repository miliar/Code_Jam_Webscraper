#include<iostream>
#include<stdio.h>
#include<set>
#include<fstream>
#include<stdlib.h>
using namespace std;
int main()
{
    ofstream output("output1.txt") ;
    ifstream input("A-small-attempt0.in") ;
    set<char> s ;
    s.insert('a') ;
    s.insert('e') ;
    s.insert('i') ;
    s.insert('o') ;
    s.insert('u') ;
    int c,t=1,n,a,b,l;
    string sa ;
    bool first ;
    getline(input,sa) ;
    c = atoi(sa.c_str()) ;
    //cout<<"c = "<<c<<endl ;
    while(c--)
    {
        string st,sr,su;
        first = true ;
        getline(input,st) ;
        int j=0;
        while(st[j] != ' ')
        {
            sr += st[j] ;
            j++ ;
        }
        //cout<<"sr = "<<sr<<endl ;
        j++ ;
        while(j<st.length())
        {
            su += st[j] ;
            j++ ;
        }
        st = sr;
        n = atoi(su.c_str()) ;
        //cout<<"n = "<<n<<endl ;
        int sum = 0 ;
        l = st.length() ;
        a= 0;
        for(int i=0;i<l;i++)
        {
            if(s.find(st[i]) == s.end())
                a++ ;
            else
                a= 0;
            if(a==n && first == true)
            {
                sum += (l-i)*(i-n+2) ;
                b = i-n ;
                first = false ;
                a-- ;
            }
            else if(a==n && first == false)
            {
                sum += (l-i)*(i-n-b) ;
                b = i-n ;
                a-- ;
            }
        }
        output<<"Case #"<<t<<": "<<sum<<endl ;
        t++ ;
    }
}
