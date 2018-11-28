#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull ;

int checkPrime(ull p)
{
    ull sqr = sqrt(p) ;
    for(ull i=2 ; i<=sqr ; i++) {
        //cout << "hi " ;
        if(i>100000000) {
            return 1 ;
        }
        if(p%i==0) {
            return i ;
        }
    }
    return 1 ;
}

pair<int,vector<int> > check(string s)
{
    int len=s.length() ;
    int flag=1 ;
    ull sa= 1<<31 ;
    vector<int>r ;
    for(int j=2 ; j<=10 ; j++) {
        ull value=0 ;
        ull curr=1 ;
        for(int i=len-1 ; i>=0 ; i--) {
            if(s[i]=='1') {
                value += curr ;
            }
            curr*=j ;
        }
        int retv=checkPrime(value) ;
        if(retv==1) {
            flag=0 ;
            break ;
        }
        else {
            r.push_back(retv) ;
        }
    }
    if(flag==1) {
        return make_pair(1,r) ;
    }
    return make_pair(0,r) ;
}

void printPowerSet( int set_size)
{
    ull pow_set_size = pow(2, set_size);
    ull counter, j;
    int coun=0 ;
    for(counter = 0; counter < pow_set_size; counter++)
    {
        //string s="110000000000000000" ;
        string s="1111" ;
        for(j = 0; j < set_size; j++)
        {
            if(counter & (1<<j))
                s+='1' ;
            else
            {
                s+='0' ;
            }
        }
        s+='1';
        pair<int, vector<int> >m = check(s) ;
        if(m.first==1)
        {
            cout << s ;
            coun++ ;
            //cout << coun ;
            for(int l=0 ; l<m.second.size() ; l++)
            {
                cout << " " << m.second[l] ;
            }
            cout << "\n" ;
        }
        if(coun==50)
        {
            return ;
        }
    }
    //cout<< "coubtadzdacdaf\n" ;
}

int main()
{
    freopen("C-large.in","r",stdin) ;
    freopen("outCLarge.txt","w",stdout) ;
    int test ;
    scanf("%d",&test) ;
    while(test--) {
        int n,j ;
        scanf("%d %d",&n,&j) ;
        cout<< "Case #1:\n" ;
        printPowerSet(11) ;
    }
    return 0 ;
}
