#include<iostream>
#include<string.h>
#include<set>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int caseNo=0;
    while(t-->0)
    {
        char s[2001];
        cin>>s;
        multiset<int> mset;
        int n=strlen(s);
        int count[26]={0};
        
        for(int i=0;i<n;i++)
        count[s[i]-'A']++;
        
        //for 0
        {
            int x=count['Z'-'A'];
            count['Z'-'A']-=x;
            count['E'-'A']-=x;
            count['R'-'A']-=x;
            count['O'-'A']-=x;
            for(int i=0;i<x;i++)
            mset.insert(0);
        }
        
        //for 2
        {
            int x=count['W'-'A'];
            count['T'-'A']-=x;
            count['W'-'A']-=x;
            count['O'-'A']-=x;
            for(int i=0;i<x;i++)
            mset.insert(2);
        }
        
        //for 4
        {
            int x=count['U'-'A'];
            count['F'-'A']-=x;
            count['O'-'A']-=x;
            count['U'-'A']-=x;
            count['R'-'A']-=x;
            for(int i=0;i<x;i++)
            mset.insert(4);
        }
        
        //for 5
        {
            int x=count['F'-'A'];
            count['F'-'A']-=x;
            count['I'-'A']-=x;
            count['V'-'A']-=x;
            count['E'-'A']-=x;
            for(int i=0;i<x;i++)
            mset.insert(5);
        }
        
        //for 6
        {
            int x=count['X'-'A'];
            count['S'-'A']-=x;
            count['I'-'A']-=x;
            count['X'-'A']-=x;
            for(int i=0;i<x;i++)
            mset.insert(6);
        }
        
        //for 7
        {
            int x=count['S'-'A'];
            count['S'-'A']-=x;
            count['E'-'A']-=x;
            count['V'-'A']-=x;
            count['E'-'A']-=x;
            count['N'-'A']-=x;
            for(int i=0;i<x;i++)
            mset.insert(7);
        }
        
        //for 8
        {
            int x=count['G'-'A'];
            count['E'-'A']-=x;
            count['I'-'A']-=x;
            count['G'-'A']-=x;
            count['H'-'A']-=x;
            count['T'-'A']-=x;
            for(int i=0;i<x;i++)
            mset.insert(8);
        }
        
        //for 9
        {
            int x=count['I'-'A'];
            count['N'-'A']-=x;
            count['I'-'A']-=x;
            count['N'-'A']-=x;
            count['E'-'A']-=x;
            for(int i=0;i<x;i++)
            mset.insert(9);
        }
        
        //for 1
        {
            int x=count['O'-'A'];
            count['O'-'A']-=x;
            count['N'-'A']-=x;
            count['E'-'A']-=x;
            for(int i=0;i<x;i++)
            mset.insert(1);
        }
        
        //for 3
        {
            int x=count['T'-'A'];
            count['T'-'A']-=x;
            count['H'-'A']-=x;
            count['R'-'A']-=x;
            count['E'-'A']-=x;
            count['E'-'A']-=x;
            for(int i=0;i<x;i++)
            mset.insert(3);
        }
        
        
        caseNo++;
        cout<<"Case #"<<caseNo<<": ";
        for(multiset<int>::iterator it=mset.begin();it!=mset.end();it++)
        cout<<*it;
        cout<<endl;
    }
    return 0;
}
