#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;

    for(int i = 0;i< n;i++)
    {
        map<char,int> m;

        string s;
        cin>>s;
        int len = s.length();
        for(int j = 0;j< len;j++)
        {
            m[s[j]]++;
        }
        int a[10000];
        int id = 0;

            while(m['Z'] >= 1)
            {
                m['Z']--;
                m['E']--;
                m['R']--;
                m['O']--;
                a[id++] = 0;
            }
            while(m['W']>=1)
            {
                m['W']--;
                m['T']--;
                m['O']--;
                a[id++] = 2;
            }
            while(m['U']>=1)
            {
                m['F']--;
                m['O']--;
                m['U']--;
                m['R']--;
                a[id++] = 4;
            }
              while(m['F']>=1)
            {
                m['F']--;
                m['I']--;
                m['V']--;
                m['E']--;
                a[id++] = 5;
            }
              while(m['X']>=1)
            {
                m['S']--;
                m['I']--;
                m['X']--;

                a[id++] = 6;
            }
              while(m['V']>=1)
            {
                m['S']--;
                m['E']--;
                m['V']--;
                m['E']--;
                m['N']--;
                a[id++] = 7;
            }
              while(m['G']>=1)
            {
                m['E']--;
                m['I']--;
                m['G']--;
                m['H']--;
                m['T']--;
                a[id++] = 8;
            }
              while(m['O']>=1)
            {
                m['O']--;
                m['N']--;
                m['E']--;

                a[id++] = 1;
            }
              while(m['N']>=1)
            {
                m['N']--;
                m['I']--;
                m['N']--;
                m['E']--;
                a[id++] = 9;
            }
              while(m['R']>=1)
            {

                m['R']--;
                a[id++] = 3;
            }
            sort(a,a+id);
            cout<<"Case #"<<i+1<<": ";
            for(int i = 0;i< id;i++)
                cout<<a[i];
            cout<<endl;









    }
}
