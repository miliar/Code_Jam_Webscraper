#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
long long t, let[255];
string s;
priority_queue<int> q;
int main()
{
    ifstream cin;
    cin.open("A-large.in");
    freopen("A-large.out","w",stdout);
    cin>>t;
    for(int o=1; o<=t; o++)
    {
        char c;
        cin.get(c);
        cin>>s;
        for(int i=0; i<s.size(); i++)
        {
            let[s[i]]++;
        }
        while(let['Z']>0)
        {
            q.push(0);
            let['Z']--;
            let['E']--;
            let['R']--;
            let['O']--;
        }
        while(let['W']>0)
        {
            q.push(-2);
            let['T']--;
            let['W']--;
            let['O']--;
        }
        while(let['U']>0)
        {
            q.push(-4);
            let['F']--;
            let['O']--;
            let['U']--;
            let['R']--;
        }
        while(let['X']>0)
        {
            q.push(-6);
            let['S']--;
            let['I']--;
            let['X']--;
        }
        while(let['G']>0)
        {
            q.push(-8);
            let['E']--;
            let['I']--;
            let['G']--;
            let['H']--;
            let['T']--;
        }
        while(let['H']>0)
        {
            q.push(-3);
            let['T']--;
            let['H']--;
            let['R']--;
            let['E']--;
            let['E']--;
        }
        while(let['F']>0)
        {
            q.push(-5);
            let['F']--;
            let['I']--;
            let['V']--;
            let['E']--;
        }
        while(let['V']>0)
        {
            q.push(-7);
            let['S']--;
            let['E']--;
            let['V']--;
            let['E']--;
            let['N']--;
        }
        while(let['I']>0)
        {
            q.push(-9);
            let['N']--;
            let['I']--;
            let['N']--;
            let['E']--;
        }
        while(let['O']>0)
        {
            q.push(-1);
            let['O']--;
            let['N']--;
            let['E']--;
        }
        printf("Case #%d: ",o);
        while(!q.empty())
        {
            printf("%d",-q.top());
            q.pop();
        }
        printf("\n");
    }
    cin.close();
    return 0;
}
