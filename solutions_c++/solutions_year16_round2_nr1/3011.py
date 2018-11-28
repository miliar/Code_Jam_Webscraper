#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    freopen("LA.in","rt",stdin);
	freopen("cLP.out","wt",stdout);
    int c[10];
    int t;
    cin>>t;
    string s;
    int a[200];
    for(int i=0;i<t;i++)
    {
        memset(a,0,sizeof(a));
        memset(c,0,sizeof(c));
        cin>>s;
        cout<<"Case #"<<i+1<<": ";
        for(int j=0;j<s.length();j++)
        {
            a[int(s[j])]++;
        }
        for(int j=0;j<s.length();j++)
           // cout<<a[j]<<" ";

            while(a[int('Z')]!=0&&a[int('O')]!=0&&a[int('R')]!=0&&a[int('E')]!=0)
            {
                a[int('Z')]--;
                a[int('E')]--;
                a[int('R')]--;
                a[int('O')]--;
                //cout<<"0";
                c[0]++;
            }
            while(a[int('T')]!=0&&a[int('W')]!=0&&a[int('O')]!=0)
            {
                a[int('T')]--;
                a[int('W')]--;
                a[int('O')]--;
                //a[int('O')]--;
                //two++;
                c[2]++;
            }
            while(a[int('F')]!=0&&a[int('O')]!=0&&a[int('R')]!=0&&a[int('U')]!=0)
            {
                a[int('F')]--;
                a[int('U')]--;
                a[int('R')]--;
                a[int('O')]--;
                c[4]++;
                //cout<<"4";
            }
            while(a[int('S')]!=0&&a[int('I')]!=0&&a[int('X')]!=0)
            {
                a[int('S')]--;
                a[int('I')]--;
                a[int('X')]--;
                //a[int('O')]--;
                //four++;
                c[6]++;
                //cout<<"4";
            }
            while(a[int('O')]!=0&&a[int('N')]!=0&&a[int('E')]!=0)
            {
                a[int('O')]--;
                a[int('N')]--;
                a[int('E')]--;
                //a[int('O')]--;
                //cout<<"1";*/
                c[1]++;
            }
            while(a[int('F')]!=0&&a[int('I')]!=0&&a[int('V')]!=0&&a[int('E')]!=0)
            {
                a[int('F')]--;
                a[int('E')]--;
                a[int('V')]--;
                a[int('I')]--;
                //cout<<"5";*/
                c[5]++;
            }





            while(a[int('S')]!=0&&a[int('V')]!=0&&a[int('N')]!=0&&a[int('E')]>=2)
            {
                a[int('S')]--;
                a[int('V')]--;
                a[int('E')]--;
                a[int('E')]--;
                a[int('N')]--;
                c[7]++;
            }
            while(a[int('E')]!=0&&a[int('I')]!=0&&a[int('G')]!=0&&a[int('H')]!=0&&a[int('T')]!=0)
            {
                a[int('E')]--;
                a[int('I')]--;
                a[int('G')]--;
                a[int('H')]--;
                a[int('T')]--;
                c[8]++;
            }
            while(a[int('N')]>=2&&a[int('I')]!=0&&a[int('E')]!=0)
            {
                a[int('N')]--;
                a[int('E')]--;
                a[int('I')]--;
                a[int('N')]--;
                c[9]++;
            }
            while(a[int('T')]!=0&&a[int('H')]!=0&&a[int('R')]!=0&&a[int('E')]>=2)
            {
                a[int('T')]--;
                a[int('H')]--;
                a[int('R')]--;
                a[int('E')]--;
                a[int('E')]--;
                //cout<<"3";*/
                c[3]++;
            }
            for(int k=0;k<10;k++)
            {
                for(int l=0;l<c[k];l++)
                    cout<<k;
            }
            cout<<endl;
        }

    return 0;
}
