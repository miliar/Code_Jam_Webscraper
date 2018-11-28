#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<vector>
#include<sstream>
using namespace std;
int isPalindrome(int strt, int iend, string b)
{
    if(strt>iend) return 1;
    if(b[strt]==b[iend]) isPalindrome(strt+1,iend-1,b);
    else return 0;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    vector<int> a, b;
    for(int i=1; i<=32; i++)
    {
        int d;
        d = i*i;
        stringstream sem;
        sem<<i<<" "<<d;
        string s1, s2;
        sem>>s1>>s2;
        if(isPalindrome(0,s1.size()-1,s1)&&isPalindrome(0,s2.size()-1,s2))
        {
            a.push_back(i);
            b.push_back(d);
        }
    }
    int T, A, B, kase;
    cin>>T;
    kase=0;
    while(T--)
    {
        int cnt;
        cin>>A>>B;
        cnt=0;
        for(int i=0; i<5; i++)
        {
            if(b[i]>=A&&b[i]<=B) cnt++;
        }
        cout<<"Case #"<<++kase<<": "<<cnt<<endl;
    }

    return 0;
}
