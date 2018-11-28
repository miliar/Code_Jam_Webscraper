#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iterator>
#include <queue>

#define vecintinit          vector<int>
#define veclintinit         vector<lint>
#define vecllintinit        vector<llint>
#define vecpintintinit      vector< pair<int,int> >
#define vecplintlintinit    vector< pair<lint,lint> >
#define vecpllintllintinit  vector< pair<llint,llint> >
#define vecintiter          vector<int>::iterator
#define veclintiter         vector<lint>::iterator
#define vecllintiter        vector<llint>::iterator
#define vecpintintiter      vector<pair<int,int> >::iterator
#define vecplintlintiter    vector<pair<lint,lint> >::iterator
#define vecpllintllintiter  vector<pair<llint,llint> >::iterator
#define setintinit          set<int>
#define setlintinit         set<lint>
#define setllintinit        set<llint>
#define msetintinit         multiset<int>
#define msetlintinit        multiset<lint>
#define msetllintinit       multiset<llint>
#define setintiter          set<int>::iterator
#define setlintiter         set<lint>::iterator
#define setllintiter        set<llint>::iterator
#define setintriter         set<int>::reverse_iterator
#define setlintriter        set<lint>::reverse_iteartor
#define setllintriter       set<llint>::reverse_iterator
#define msetintiter         multiset<int>::iterator
#define msetlintiter        multiset<lint>::iterator
#define msetllintiter       multiset<llint>::iterator
#define msetintriter        multiset<int>::reverse_iterator
#define msetlintriter       multiset<lint>::reverse_iteartor
#define msetllintriter      multiset<llint>::reverse_iterator
#define mapintintinit           map<int,int>
#define maplintlintinit         map<lint,lint>
#define mapllintllintinit       map<llint,llint>
#define mulmapintintinit        multimap<int,int>
#define mulmaplintlintinit      multimap<lint,lint>
#define mulmapllintllintinit    multimap<llint,llint>
#define mapintintiter           map<int,int>::iterator
#define maplintlintiter         map<lint,lint>::iterator
#define mapllintllintiter       map<llint,llint>::iterator
#define mulmapintintiter        multimap<int,int>::iterator
#define mulmaplintlintiter      multimap<lint,lint>::iterator
#define mulmapllintllintiter    multimap<llint,llint>::iterator
#define mapintintriter          map<int,int>::reverse_iterator
#define maplintlintriter        map<lint,lint>::reverse_iterator
#define mapllintllintriter      map<llint,llint>::reverse_iterator
#define mulmapintintriter       multimap<int,int>::reverse_iterator
#define mulmaplintlintriter     multimap<lint,lint>::reverse_iterator
#define mulmapllintllintriter   multimap<llint,llint>::reverse_iterator

#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a>b)?b:a
using namespace std;
typedef long long int llint;
typedef long int lint;
template <typename T_>
void fastread(T_ *a)
{
    char c=0; *a=0;
    while(c<33){c=getchar();}
    while(c>33){*a=(*a<<3)+(*a<<1)+c-'0'; c=getchar();}
}

int fast_str(char *a)
{
    int len=0; char c=0;
    while(c<33){c=getchar();}//eat spaces
    while(c!='\n'){*a=c; ++len; ++a; c=getchar();}
    *a='\0';
    return len;
}

int fast_wrd(char *a)
{
    char c=0; int len=0;
    while(c<33){c=getchar();}
    while(c>33){*a=c; ++len; ++a; c=getchar();}
    *a='\0';
    return len;
}

void fast_wrt(char *a)
{
    while(*a!='\0')
    {
        putchar(*a);
        ++a;
    }
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int cards[4][4];
    set<int> myset;
    set<int> myset1;
    set<int>::iterator itr,itr1;
    int cases,rowid,temp;
    fastread(&cases);
    int casenum;
    for(casenum=1;casenum<=cases;++casenum)
    {
        myset.clear();
        myset1.clear();
        fastread(&rowid);
        --rowid;
        //get config
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                fastread(&temp);
                if(i==rowid)
                {
                    myset.insert(temp);
                }
            }
        }
        fastread(&rowid);
        --rowid;
        //get config
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                fastread(&temp);
                if(i==rowid)
                {
                    myset1.insert(temp);
                }
            }
        }
        /**
        for(itr=myset.begin();itr!=myset.end();++itr)
            cout<<*(itr)<<" ";
        cout<<endl;
        for(itr=myset1.begin();itr!=myset1.end();++itr)
            cout<<*(itr)<<" ";
        cout<<endl;
        **/

        int match=0,cardnum;
        for(itr=myset.begin();itr!=myset.end();++itr)
        {
            itr1=myset1.find(*itr);
            if(itr1!=myset1.end())//found somthing
            {
                cardnum=*(itr1);
                ++match;
            }
        }

        if(match==0)
        {
            cout<<"Case #"<<casenum<<": "<<"Volunteer cheated!"<<endl;
        }
        else if(match>1)
        {
            cout<<"Case #"<<casenum<<": "<<"Bad magician!"<<endl;
        }
        else if(match==1)
        {
            cout<<"Case #"<<casenum<<": "<<cardnum<<endl;
        }

    }

    return 0;
}
