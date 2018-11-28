
#include<iostream>
#include<string>
#include<algorithm>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int a[100];
    int t,i,j;
    string s;
    cin>>t;
    for( i = 1; i <= t; i++ )
    {
        string ans;
        cin>>s;
        for( j = 65; j <= 90; j++ )
            a[j] = 0;
        for( j = 0; j < s.length(); j++)
            a[(s[j])]++;
        if( a['Z'] != 0 )
        {
            j = a['Z'];
            a['Z']=0;
            while(j--)
            {
                ans.append(1,'0');
                a['E']--;
                a['R']--;
                a['O']--;
            }
        }
        if( a['W'] != 0 )
        {
            j = a['W'];
            a['W']=0;
            while(j--)
            {
                a['T']--;
                a['O']--;
                ans.append(1,'2');
            }
        }
        if( a['U'] != 0 )
        {
            j = a['U'];
            a['U']=0;
            while(j--)
            {
                a['R']--;
                a['O']--;
                a['F']--;
                ans.append(1,'4');
            }
        }
        if( a['X'] != 0 )
        {
            j = a['X'];
            a['X']=0;
            while(j--)
            {
                a['S']--;
                a['I']--;
                ans.append(1,'6');
            }
        }
        if( a['G'] != 0 )
        {
            j = a['G'];
            a['G']=0;
            while(j--)
            {
                a['E']--;
                a['I']--;
                a['H']--;
                a['T']--;
                ans.append(1,'8');
            }
        }
        if( a['O'] != 0 )
        {
            j = a['O'];
            a['O']=0;
            while(j--)
            {
                a['E']--;
                a['N']--;
                ans.append(1,'1');
            }
        }
        if( a['R'] != 0 )
        {
            j = a['R'];
            a['R']=0;
            while(j--)
            {
                a['T']--;
                a['H']--;
                a['E']--;
                a['E']--;
                ans.append(1,'3');
            }
        }
        if( a['S'] != 0 )
        {
            j = a['S'];
            a['S']=0;
            while(j--)
            {
                a['N']--;
                a['V']--;
                a['E']--;
                a['E']--;
                ans.append(1,'7');
            }
        }
        if( a['F'] != 0 )
        {
            j = a['F'];
            a['F']=0;
            while(j--)
            {
                a['I']--;
                a['V']--;
                a['E']--;
                ans.append(1,'5');
            }
        }
        if( a['I'] != 0 )
        {
            j = a['I'];
            a['I']=0;
            while(j--)
            {
                a['N']--;
                a['N']--;
                a['E']--;
                ans.append(1,'9');
            }
        }
        sort(ans.begin(),ans.end());
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}

